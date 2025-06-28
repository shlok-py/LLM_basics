# seq2seq_summarizer_pytorch.py

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import pandas as pd
from sklearn.model_selection import train_test_split
from torch.nn.utils.rnn import pad_sequence
from collections import Counter
import re

# ----------- Data Preprocessing -----------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\u0900-\u097Fa-zA-Z0-9\s]+", "", text)
    return text.strip()

class Vocab:
    def __init__(self, texts, max_vocab=5000):
        self.word2idx = {"<PAD>": 0, "<SOS>": 1, "<EOS>": 2, "<UNK>": 3}
        self.idx2word = {0: "<PAD>", 1: "<SOS>", 2: "<EOS>", 3: "<UNK>"}
        all_words = [w for text in texts for w in text.split()]
        freq = Counter(all_words).most_common(max_vocab - 4)
        for i, (word, _) in enumerate(freq, 4):
            self.word2idx[word] = i
            self.idx2word[i] = word

    def encode(self, text):
        return [self.word2idx.get(w, self.word2idx['<UNK>']) for w in text.split()]

    def decode(self, ids):
        return ' '.join([self.idx2word.get(i, '<UNK>') for i in ids])

# ----------- Dataset -----------
class SummarizationDataset(Dataset):
    def __init__(self, articles, summaries, vocab_article, vocab_summary):
        self.articles = articles
        self.summaries = summaries
        self.vocab_article = vocab_article
        self.vocab_summary = vocab_summary

    def __len__(self):
        return len(self.articles)

    def __getitem__(self, idx):
        src = torch.tensor(self.vocab_article.encode(self.articles[idx]), dtype=torch.long)
        tgt = torch.tensor([1] + self.vocab_summary.encode(self.summaries[idx]) + [2], dtype=torch.long)  # <SOS> + ... + <EOS>
        return src, tgt

def collate_fn(batch):
    src_batch, tgt_batch = zip(*batch)
    src_batch = pad_sequence(src_batch, batch_first=True, padding_value=0)
    tgt_batch = pad_sequence(tgt_batch, batch_first=True, padding_value=0)
    return src_batch, tgt_batch

# ----------- Seq2Seq Model -----------
class Encoder(nn.Module):
    def __init__(self, vocab_size, emb_size, hidden_size):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, emb_size)
        self.lstm = nn.LSTM(emb_size, hidden_size, batch_first=True)

    def forward(self, x):
        x = self.embed(x)
        outputs, (h, c) = self.lstm(x)
        return h, c

class Decoder(nn.Module):
    def __init__(self, vocab_size, emb_size, hidden_size):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, emb_size)
        self.lstm = nn.LSTM(emb_size, hidden_size, batch_first=True)
        self.out = nn.Linear(hidden_size, vocab_size)

    def forward(self, x, h, c):
        x = self.embed(x)
        output, (h, c) = self.lstm(x, (h, c))
        output = self.out(output)
        return output, h, c

# ----------- Training -----------
def train_seq2seq():
    df = pd.read_csv("data/summarization_data.csv")
    df = df.dropna().copy()
    df['headlines'] = df['headlines'].apply(clean_text)
    df['text'] = df['text'].apply(clean_text)

    art_train, art_val, sum_train, sum_val = train_test_split(df['headlines'], df['text'], test_size=0.1)

    vocab_article = Vocab(art_train.tolist())
    vocab_summary = Vocab(sum_train.tolist())

    train_ds = SummarizationDataset(art_train.tolist(), sum_train.tolist(), vocab_article, vocab_summary)
    train_dl = DataLoader(train_ds, batch_size=16, shuffle=True, collate_fn=collate_fn)

    encoder = Encoder(len(vocab_article.word2idx), 128, 256)
    decoder = Decoder(len(vocab_summary.word2idx), 128, 256)

    criterion = nn.CrossEntropyLoss(ignore_index=0)
    enc_opt = torch.optim.Adam(encoder.parameters(), lr=0.001)
    dec_opt = torch.optim.Adam(decoder.parameters(), lr=0.001)

    for epoch in range(10):
        encoder.train()
        decoder.train()
        total_loss = 0

        for src, tgt in train_dl:
            h, c = encoder(src)
            dec_input = tgt[:, :-1]
            target = tgt[:, 1:]
            output, _, _ = decoder(dec_input, h, c)

            loss = criterion(output.reshape(-1, output.size(-1)), target.reshape(-1))

            enc_opt.zero_grad()
            dec_opt.zero_grad()
            loss.backward()
            enc_opt.step()
            dec_opt.step()

            total_loss += loss.item()

        print(f"Epoch {epoch+1}, Loss: {total_loss/len(train_dl):.4f}")

if __name__ == "__main__":
    train_seq2seq()

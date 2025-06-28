<center>

# **KATHMANDU UNIVERSITY**

## **Comparison Report: CLIP and Whisper Multimodal LLMs**
![Kathmandu University Logo](../iamge/OIP.webp)
..
#### **Submitted By:**  
**Shlok Koirala**

#### **Submitted To:**  
**Ashok K Panta**

### **Department of Artificial Intelligence**  
#### School of Engineering

**Date:** 28 June, 2025

</center>

---

## Introduction
This report compares two multimodal Large Language Models (LLMs), CLIP and Whisper, focusing on their architectures, input modalities, main applications, and handling of cross-modal inputs. A comparison table and a diagram illustrating their architectures are included.

## CLIP (Contrastive Language–Image Pre-training)

### Architecture
CLIP, developed by OpenAI, consists of two main components: a vision transformer (ViT) or convolutional neural network (e.g., ResNet) for image processing and a transformer-based text encoder for text processing. These encoders generate embeddings in a shared latent space, trained using contrastive learning to align image and text representations. The model is pre-trained on 400 million image-text pairs to learn robust cross-modal representations.

### Input Types
- **Image**: Processes images (e.g., photographs, drawings) via the vision encoder.
- **Text**: Handles natural language descriptions or captions through the text encoder.

### Main Applications
- **Image Classification**: Zero-shot classification by matching images to text prompts.
- **Image-Text Retrieval**: Finding relevant images for text queries or vice versa.
- **Visual Question Answering**: Answering questions about images using text prompts.
- **Image Generation Guidance**: Used in models like DALL·E to guide image generation.

### Cross-Modal Handling
CLIP aligns image and text embeddings in a shared latent space using contrastive loss, enabling it to match images with corresponding text descriptions. For example, given an image, CLIP can rank text descriptions by similarity, or given a text prompt, it can identify relevant images. This is achieved by maximizing the cosine similarity between paired image-text embeddings while minimizing similarity for unpaired ones.

## Whisper

### Architecture
Whisper, also developed by OpenAI, is an automatic speech recognition (ASR) model based on a transformer architecture. It uses an encoder-decoder structure where the encoder processes audio inputs as log-mel spectrograms, and the decoder generates text transcriptions. Whisper is trained on 680,000 hours of multilingual audio data, including 125,000 hours of non-English data, enabling robust speech-to-text capabilities.

### Input Types
- **Audio**: Processes audio inputs (e.g., speech, music) as log-mel spectrograms.
- **Text**: Outputs transcriptions or translations as text; text inputs are used for tasks like translation prompts.

### Main Applications
- **Speech-to-Text Transcription**: Converts spoken language into text across multiple languages.
- **Speech Translation**: Translates spoken content from one language to another.
- **Voice Activity Detection**: Identifies speech segments in audio streams.
- **Accessibility Tools**: Powers real-time captioning for audio content.

### Cross-Modal Handling
Whisper primarily focuses on audio-to-text conversion, where the encoder processes audio spectrograms to extract features, and the decoder generates text outputs. It handles cross-modal inputs by mapping audio features to text tokens in a sequence-to-sequence framework. For translation tasks, Whisper can take audio in one language and output text in another, leveraging its multilingual training data to align audio and text representations.

## Comparison Table

| **Aspect**               | **CLIP**                                  | **Whisper**                              |
|--------------------------|-------------------------------------------|------------------------------------------|
| **Developer**            | OpenAI                                    | OpenAI                                   |
| **Primary Modalities**   | Image, Text                               | Audio, Text                              |
| **Architecture**         | Vision Transformer/ResNet + Text Transformer | Encoder-Decoder Transformer              |
| **Input Processing**     | Images (pixels), Text (tokens)            | Audio (log-mel spectrograms), Text (tokens) |
| **Cross-Modal Mechanism**| Contrastive learning for shared embeddings | Sequence-to-sequence audio-to-text mapping |
| **Main Applications**    | Image classification, retrieval, VQA      | Speech transcription, translation         |
| **Training Data**        | 400M image-text pairs                     | 680K hours of multilingual audio         |


## Analysis
CLIP excels in vision-language tasks, leveraging contrastive learning to align image and text embeddings, making it versatile for zero-shot learning and retrieval tasks. Whisper, designed for audio-text tasks, uses a sequence-to-sequence approach, making it highly effective for transcription and translation across languages. While CLIP handles static image-text pairs, Whisper processes temporal audio data, requiring different architectural considerations. CLIP’s strength lies in its flexibility for visual tasks, whereas Whisper dominates in audio processing with multilingual support.

## References
- Radford, A., et al. (2021). "Learning Transferable Visual Models From Natural Language Supervision." arXiv:2103.00020.
- Radford, A., et al. (2022). "Robust Speech Recognition via Large-Scale Weak Supervision." arXiv:2212.04356.
<center>

# **KATHMANDU UNIVERSITY**

## **Assignment 4.3 Report**
![Kathmandu University Logo](../iamge/OIP.webp)

#### **Submitted By:**  
**Shlok Koirala**

#### **Submitted To:**  
**Ashok K Panta**

### **Department of Artificial Intelligence**  
#### School of Engineering

**Date:** 28 June, 2025

</center>

---

## Task
**Sentiment Analysis** — Determine whether a given sentence expresses **positive** or **negative** sentiment.

---

## Step 1: Dataset

Using the **IMDb** dataset (binary sentiment classification).

Example:
> “This movie was a complete waste of time. Poor acting and worse direction.”  
**Label:** Negative

---

## Step 2: Prompt Variants and Tuning Techniques

### 🔹 Prompt 1: Basic (Zero-shot)
```text
Is the following movie review positive or negative?
Review: This movie was a complete waste of time.
Sentiment:
**Output**: Negative 
```

---

### Prompt 2: Few-shot Prompt Tuning
```text
Review: I absolutely loved this film. The acting was brilliant!  
Sentiment: Positive

Review: The plot was boring and predictable.  
Sentiment: Negative

Review: This movie was a complete waste of time.  
Sentiment:
```

**Output**: Negative

`Improvement: Clearer structure, examples help model generalize.`

---

### Prompt 3: Chain-of-Thought (CoT)
Let’s analyze the review step-by-step:

```
"This movie was a complete waste of time."
- The phrase “complete waste of time” shows strong dissatisfaction.
- The tone is negative.
Final Sentiment:

```

**Output**: Negative

`Benefit: Explains reasoning — helpful for borderline cases or noisy data.`

##  Step 3: Evaluation Summary
| Prompt Type        | Correctness   | Interpretability | Generalization | Notes                                   |
|--------------------|---------------|------------------|----------------|-----------------------------------------|
| Zero-shot          | ✅ Correct     | ❌ Low           | ❌ Limited     | Simple, fast but brittle                |
| Few-shot           | ✅ Correct     | ✅ Medium        | ✅ Better      | Learns pattern from examples           |
| Chain-of-Thought   | ✅ Correct     | ✅ High          | ✅ Robust      | Best for complex or nuanced inputs     |

## Conclusion
*  **Few-shot and CoT** prompting significantly improve LLM reliability in sentiment tasks.

* **Few-shot** excels when you have structured examples.

* **Chain-of-Thought** is more robust and transparent, especially when explainability is required.

* **Recommendation**:
Use few-shot for efficiency and CoT for interpretability in real-world sentiment classification tasks.

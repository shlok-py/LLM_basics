<center>

# **KATHMANDU UNIVERSITY**

## **Assignment 4.1 Report**
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
## 🎯 Task
**Solve a grade-school level math word problem:**

> A train travels 60 kilometers in 1.5 hours. What is the average speed of the train in kilometers per hour?

---

## 📥 Prompt Designs

### ✅ A. Direct Prompt
What is the average speed of a train that travels 60 kilometers in 1.5 hours?

---
### ✅ B. Few-Shot Prompt
Q: A car travels 100 kilometers in 2 hours. What is its average speed?
A: 100 / 2 = 50 km/h

Q: A person walks 12 kilometers in 3 hours. What is their average speed?
A: 12 / 3 = 4 km/h

Q: A train travels 60 kilometers in 1.5 hours. What is its average speed?
A:

---

### ✅ C. Chain-of-Thought (CoT) Prompt
A train travels 60 kilometers in 1.5 hours. To find the average speed, we divide the total distance by the total time.
That is, average speed = distance / time. So we compute:

---

## 🤖 LLM Outputs (ChatGPT)

| Prompt Type        | Output                                                                 |
|--------------------|------------------------------------------------------------------------|
| **Direct**         | The average speed is 40 kilometers per hour.                           |
| **Few-Shot**       | 60 / 1.5 = 40 km/h                                                      |
| **Chain-of-Thought** | Distance = 60 km, Time = 1.5 hours. Average speed = 60 / 1.5 = 40 km/h |

---

## 📊 Comparative Analysis

| Criteria                      | Direct Prompt          | Few-Shot Prompt                 | Chain-of-Thought Prompt                        |
|-------------------------------|------------------------|----------------------------------|------------------------------------------------|
| **Correctness**               | ✅ Correct             | ✅ Correct                       | ✅ Correct                                     |
| **Clarity of Reasoning**      | ❌ Just answer         | ✅ Shows equation                | ✅ Step-by-step breakdown                      |
| **Adaptability (Complex Tasks)** | ❌ Weak              | ⚠️ Medium                        | ✅ Strong for multi-step reasoning             |
| **Prompt Length**             | 🟢 Shortest            | 🟡 Medium                        | 🔴 Longest                                     |

---

## 📝 Conclusion

- ✅ **Chain-of-Thought** prompt gives the **most interpretable** and **robust** output.
- ⚠️ **Few-shot** performs well but is sensitive to example quality.
- ❌ **Direct** prompt is fast but lacks explanation or generalization power.

> **Recommendation**:  
> Use **Chain-of-Thought** prompting for reasoning tasks;  
> Use **Few-Shot** for structure-based pattern recognition tasks.

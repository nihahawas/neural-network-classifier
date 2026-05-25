# 🧠 Neural Network Classifier

An interactive machine learning web app that demonstrates **Single Layer Neural Networks** and **Multilayer Perceptron (MLP) with Backpropagation** across four real-world classification scenarios.

🔴 **Live Demo** → *(add your Streamlit Cloud link here after deploying)*

---

## 📌 Scenarios

| # | Scenario | Features | Output Classes |
|---|---|---|---|
| 1 | 🎓 Student Performance | Attendance, Avg Marks | Excellent / Average / Poor |
| 2 | 🏦 Loan Approval | Income, Credit Score | Approved / Pending / Rejected |
| 3 | 🌤️ Weather Prediction | Temperature, Humidity | Sunny / Rainy / Stormy |
| 4 | 👔 Employee Performance | Tasks Done, Attendance | High / Medium / Low |

---

## 🧠 Models

### Single Layer Neural Network (from scratch)
- Built using **NumPy only**
- Uses **Softmax** activation + **Cross-Entropy** loss
- Trained with **Gradient Descent**

### Multilayer Perceptron (MLP) with Backpropagation
- Uses **scikit-learn's** `MLPClassifier`
- Hidden layers with **ReLU / Tanh** activation
- Optimized with **Adam**

---

## 🚀 Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/neural-network-classifier.git
cd neural-network-classifier
pip install -r requirements.txt
streamlit run app.py
```

Opens at **http://localhost:8501** 🎉

---

## 📁 Project Structure

```
neural-network-classifier/
├── app.py                    # Streamlit web app
├── network-classifier.ipynb  # Jupyter Notebook walkthrough
├── requirements.txt          # Dependencies
└── README.md
```

---

## 🌐 Deploy on Streamlit Cloud

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub → select this repo
4. Set **Main file**: `app.py`
5. Click **Deploy** ✅

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![NumPy](https://img.shields.io/badge/NumPy-1.24-orange?logo=numpy)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3-green?logo=scikit-learn)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32-red?logo=streamlit)

<div align="center">

# 🧠 Neural Network Classifier App

*An interactive ML web app to visualize & compare neural network models across real-world scenarios*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![NumPy](https://img.shields.io/badge/NumPy-1.24+-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)

🔴 **[Live Demo →](https://neural-network-classifier-9hdpl8kkbgzhxgzfld9eto.streamlit.app)** &nbsp;&nbsp;|&nbsp;&nbsp; 📓 **[Notebook Walkthrough →](network-classifier.ipynb)**

<img width="1304" height="837" alt="image" src="https://github.com/user-attachments/assets/e4e7e7a8-9eed-4de5-bbb5-3914d697c945" />


</div>

---

## ✨ What It Does

This app lets you interact with two neural network architectures — built from scratch and via scikit-learn — and see real predictions across four classification scenarios. Adjust inputs with sliders, switch models with a click, and watch the prediction update instantly.

---

## 📌 Scenarios

| # | Scenario | Input Features | Output Classes |
|---|----------|---------------|----------------|
| 🎓 | **Student Performance** | Attendance %, Average Marks | `Excellent` / `Average` / `Poor` |
| 🏦 | **Loan Approval** | Annual Income, Credit Score | `Approved` / `Pending` / `Rejected` |
| 🌤️ | **Weather Prediction** | Temperature, Humidity | `Sunny` / `Rainy` / `Stormy` |
| 👔 | **Employee Performance** | Tasks Completed, Attendance % | `High` / `Medium` / `Low` |

---

## 🧠 Models

### Single Layer Neural Network *(from scratch)*
- Built with **NumPy only** — no ML frameworks
- **Softmax** activation + **Cross-Entropy** loss
- Trained using **Gradient Descent**

### MLP with Backpropagation *(scikit-learn)*
- Uses `MLPClassifier` from **scikit-learn**
- Hidden layers with **ReLU / Tanh** activation
- Optimized with **Adam**

---

## 🚀 Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/nihahawas/neural-network-classifier.git
cd neural-network-classifier

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the app
streamlit run app.py
```

> Opens at **http://localhost:8501** 🎉

---

## 📁 Project Structure

```
neural-network-classifier/
├── app.py                     # Streamlit web application
├── network-classifier.ipynb   # Jupyter Notebook walkthrough
├── requirements.txt           # Python dependencies
└── README.md
```

---

## 🌐 Deploy on Streamlit Cloud

1. Push this repo to **GitHub**
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in
3. Click **New app** → select this repository
4. Set **Main file path** to `app.py`
5. Click **Deploy** ✅

> Replace the Live Demo link at the top with your deployed URL once live.

---

## 🛠️ Tech Stack

| Tool | Role |
|------|------|
| **Python 3.10+** | Core language |
| **NumPy** | Single-layer NN from scratch |
| **scikit-learn** | MLP with backpropagation |
| **Streamlit** | Interactive web interface |

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

| Name | GitHub | LinkedIn |
|------|--------|----------|
| **Niha Hawas** | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/nihahawas) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/nihahawas45) |

---

<div align="center">
  
Made with ❤️ by **NIHA HAWAS** using Python & Streamlit
</div>

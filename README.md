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

# 📖 Technical Blog

Want to learn how this project was built?

I documented the complete development process, neural network implementation, technologies used, challenges faced, and key lessons learned.

📝 **Read the full article:**

https://codebyniha.hashnode.dev/building-a-neural-network-classifier-with-python-from-theory-to-deployment

---

## ✨ What It Does

This app lets you interact with two neural network architectures—built from scratch and using scikit-learn—and see real predictions across four classification scenarios. Adjust inputs with sliders, switch models with a click, and watch predictions update instantly through an intuitive Streamlit interface.

---

## ⭐ Project Highlights

- 🧠 Built a **Single Layer Neural Network from scratch** using NumPy.
- 🤖 Implemented a **Multi-Layer Perceptron (MLP)** using Scikit-learn.
- 🌐 Developed an interactive web application with Streamlit.
- 📊 Supports four real-world classification scenarios.
- ⚡ Compare custom neural network implementation with a library-based approach.
- 🎯 Beginner-friendly project for understanding neural networks.

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

### Single Layer Neural Network *(Built from Scratch)*

- Built entirely using **NumPy**
- Implements **Softmax Activation**
- Uses **Cross-Entropy Loss**
- Optimized with **Gradient Descent**

### Multi-Layer Perceptron *(Scikit-learn)*

- Uses **MLPClassifier**
- Hidden Layers with **ReLU / Tanh**
- Trained using **Backpropagation**
- Optimized with **Adam Optimizer**

---

## 🚀 Run Locally

```bash
# Clone repository
git clone https://github.com/nihahawas/neural-network-classifier.git

# Enter project directory
cd neural-network-classifier

# Install dependencies
pip install -r requirements.txt

# Launch Streamlit application
streamlit run app.py
```

Open your browser at:

```
http://localhost:8501
```

---

## 📁 Project Structure

```
neural-network-classifier/
├── app.py
├── network-classifier.ipynb
├── requirements.txt
└── README.md
```

---

## 🌐 Deploy on Streamlit Cloud

1. Push this repository to GitHub.
2. Visit https://share.streamlit.io
3. Create a new Streamlit application.
4. Select this repository.
5. Set the main file to **app.py**.
6. Deploy.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core Programming Language |
| NumPy | Neural Network from Scratch |
| Scikit-learn | Multi-Layer Perceptron |
| Streamlit | Interactive Web Application |

---

## 📚 Learning Outcomes

Through this project, I gained hands-on experience with:

- Neural Network Fundamentals
- Forward & Backpropagation
- Gradient Descent Optimization
- Softmax Classification
- Machine Learning Workflows
- Streamlit Application Development
- Building Neural Networks from Scratch
- Comparing Custom and Framework-based Models

---

## 🚀 Future Improvements

- 📈 Add accuracy and loss visualization
- 📊 Include confusion matrix and evaluation metrics
- 🧠 Integrate deep learning models using TensorFlow/PyTorch
- ☁️ Deploy using Docker and cloud platforms
- 🎨 Improve UI with dark/light theme support

---

## 📄 License

This project is licensed under the MIT License.

---

# 👩‍💻 About the Author

**Niha Hawas**

🎓 BSCS Student

🤖 AI & Machine Learning Enthusiast

💻 Python Developer

🌐 Networking Learner

### Connect with Me

- 💼 LinkedIn: https://linkedin.com/in/nihahawas45
- 🌐 Portfolio: https://nihahawas.github.io/personal-portfolio-website/
- ✍️ Hashnode: https://codebyniha.hashnode.dev
- 💻 GitHub: https://github.com/nihahawas

---

<div align="center">

### ⭐ If you found this project helpful, consider giving it a Star!

Made with ❤️ by **Niha Hawas**

</div>

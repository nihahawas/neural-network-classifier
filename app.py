import streamlit as st
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neural_network import MLPClassifier

# ── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Neural Network Classifier",
    page_icon="🧠",
    layout="centered"
)

# ── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
}
.stApp {
    background: #0a0a0f;
    color: #e8e8f0;
}
h1 { font-size: 2.4rem !important; font-weight: 800; color: #ffffff; }
h2 { color: #a78bfa; font-weight: 700; }
h3 { color: #c4b5fd; }
.result-box {
    background: linear-gradient(135deg, #1e1b4b, #312e81);
    border: 1px solid #4f46e5;
    border-radius: 12px;
    padding: 24px;
    text-align: center;
    margin-top: 16px;
}
.result-label {
    font-size: 2rem;
    font-weight: 800;
    color: #a5f3fc;
    font-family: 'Space Mono', monospace;
}
.result-sub {
    font-size: 0.9rem;
    color: #94a3b8;
    margin-top: 6px;
}
.stSelectbox label, .stSlider label { color: #c4b5fd !important; font-weight: 600; }
.stButton button {
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 28px;
    font-weight: 700;
    font-size: 1rem;
    width: 100%;
    transition: all 0.2s;
}
.stButton button:hover { opacity: 0.85; transform: translateY(-1px); }
.badge {
    display: inline-block;
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 0.75rem;
    color: #94a3b8;
    font-family: 'Space Mono', monospace;
    margin: 2px;
}
hr { border-color: #1e293b; }
</style>
""", unsafe_allow_html=True)


# ── Single Layer Neural Network ──────────────────────────────────────────────
class SingleLayerNN:
    def __init__(self, n_inputs, n_outputs, lr=0.1, epochs=2000):
        self.lr = lr
        self.epochs = epochs
        np.random.seed(42)
        self.W = np.random.randn(n_inputs, n_outputs) * 0.01
        self.b = np.zeros((1, n_outputs))

    def softmax(self, z):
        e = np.exp(z - np.max(z, axis=1, keepdims=True))
        return e / e.sum(axis=1, keepdims=True)

    def one_hot(self, y, n):
        oh = np.zeros((len(y), n))
        oh[np.arange(len(y)), y] = 1
        return oh

    def fit(self, X, y):
        n = len(np.unique(y))
        Y = self.one_hot(y, n)
        for _ in range(self.epochs):
            A = self.softmax(X @ self.W + self.b)
            dZ = A - Y
            self.W -= self.lr * X.T @ dZ / len(X)
            self.b -= self.lr * dZ.mean(axis=0, keepdims=True)

    def predict_proba(self, X):
        return self.softmax(X @ self.W + self.b)

    def predict(self, X):
        return np.argmax(self.predict_proba(X), axis=1)


# ── Model Training ───────────────────────────────────────────────────────────
@st.cache_resource
def get_models():
    models = {}

    # Student Performance
    X = np.array([[95,88],[70,60],[55,45],[92,85],[68,58]], dtype=float)
    y_raw = ['Excellent','Average','Poor','Excellent','Average']
    le = LabelEncoder(); y = le.fit_transform(y_raw)
    sc = StandardScaler(); Xs = sc.fit_transform(X)
    slnn = SingleLayerNN(2, 3); slnn.fit(Xs, y)
    mlp = MLPClassifier(hidden_layer_sizes=(8,4), max_iter=3000, random_state=42)
    mlp.fit(Xs, y)
    models['student'] = dict(le=le, sc=sc, slnn=slnn, mlp=mlp,
        features=['Attendance (%)', 'Average Marks'],
        ranges=[(50, 100, 80), (30, 100, 75)])

    # Loan Approval
    X = np.array([[50000,750],[30000,620],[20000,500],[52000,780],[28000,610]], dtype=float)
    y_raw = ['Approved','Pending','Rejected','Approved','Pending']
    le = LabelEncoder(); y = le.fit_transform(y_raw)
    sc = StandardScaler(); Xs = sc.fit_transform(X)
    slnn = SingleLayerNN(2, 3); slnn.fit(Xs, y)
    mlp = MLPClassifier(hidden_layer_sizes=(10,5), max_iter=3000, random_state=42)
    mlp.fit(Xs, y)
    models['loan'] = dict(le=le, sc=sc, slnn=slnn, mlp=mlp,
        features=['Monthly Income (PKR)', 'Credit Score'],
        ranges=[(10000, 100000, 40000), (300, 850, 650)])

    # Weather Prediction
    X = np.array([[22,40],[30,75],[35,85],[24,45],[29,70]], dtype=float)
    y_raw = ['Sunny','Rainy','Stormy','Sunny','Rainy']
    le = LabelEncoder(); y = le.fit_transform(y_raw)
    sc = StandardScaler(); Xs = sc.fit_transform(X)
    slnn = SingleLayerNN(2, 3); slnn.fit(Xs, y)
    mlp = MLPClassifier(hidden_layer_sizes=(8,4), activation='tanh', max_iter=3000, random_state=42)
    mlp.fit(Xs, y)
    models['weather'] = dict(le=le, sc=sc, slnn=slnn, mlp=mlp,
        features=['Temperature (°C)', 'Humidity (%)'],
        ranges=[(10, 50, 28), (10, 100, 60)])

    # Employee Performance
    X = np.array([[95,98],[70,75],[45,60],[90,95],[68,72]], dtype=float)
    y_raw = ['High','Medium','Low','High','Medium']
    le = LabelEncoder(); y = le.fit_transform(y_raw)
    sc = StandardScaler(); Xs = sc.fit_transform(X)
    slnn = SingleLayerNN(2, 3); slnn.fit(Xs, y)
    mlp = MLPClassifier(hidden_layer_sizes=(6,4), max_iter=3000, random_state=42)
    mlp.fit(Xs, y)
    models['employee'] = dict(le=le, sc=sc, slnn=slnn, mlp=mlp,
        features=['Tasks Completed', 'Attendance (%)'],
        ranges=[(10, 100, 75), (50, 100, 80)])

    return models


# ── UI ────────────────────────────────────────────────────────────────────────
st.markdown("# 🧠 Neural Network Classifier")
st.markdown("An interactive ML app built with **Single Layer NN** and **MLP Backpropagation**")
st.markdown('<span class="badge">NumPy</span><span class="badge">scikit-learn</span><span class="badge">Streamlit</span>', unsafe_allow_html=True)
st.markdown("---")

SCENARIO_MAP = {
    "🎓 Student Performance": "student",
    "🏦 Loan Approval": "loan",
    "🌤️ Weather Prediction": "weather",
    "👔 Employee Performance": "employee",
}

scenario_label = st.selectbox("**Choose a Scenario**", list(SCENARIO_MAP.keys()))
scenario = SCENARIO_MAP[scenario_label]
models = get_models()
m = models[scenario]

st.markdown("---")
st.markdown("### 📥 Enter Input Values")

col1, col2 = st.columns(2)
f1_min, f1_max, f1_def = m['ranges'][0]
f2_min, f2_max, f2_def = m['ranges'][1]

with col1:
    val1 = st.slider(m['features'][0], f1_min, f1_max, f1_def)
with col2:
    val2 = st.slider(m['features'][1], f2_min, f2_max, f2_def)

model_choice = st.radio("**Select Model**", ["Single Layer NN", "MLP (Backpropagation)"], horizontal=True)

if st.button("🔮 Predict"):
    X_input = np.array([[val1, val2]], dtype=float)
    X_scaled = m['sc'].transform(X_input)

    if model_choice == "Single Layer NN":
        pred_idx = m['slnn'].predict(X_scaled)[0]
        proba = m['slnn'].predict_proba(X_scaled)[0]
    else:
        pred_idx = m['mlp'].predict(X_scaled)[0]
        proba = m['mlp'].predict_proba(X_scaled)[0]

    label = m['le'].inverse_transform([pred_idx])[0]
    confidence = proba[pred_idx] * 100

    st.markdown(f"""
    <div class="result-box">
        <div class="result-sub">Prediction</div>
        <div class="result-label">✅ {label}</div>
        <div class="result-sub">Confidence: {confidence:.1f}% &nbsp;|&nbsp; Model: {model_choice}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### 📊 Class Probabilities")
    for cls, prob in zip(m['le'].classes_, proba):
        st.progress(float(prob), text=f"{cls}: {prob*100:.1f}%")

st.markdown("---")
st.markdown('<p style="text-align:center; color:#475569; font-size:0.8rem;">"Built with ❤️ by Niha Hawas using Python · Neural Networks from Scratch + scikit-learn"</p>', unsafe_allow_html=True)


# 🛍️ Flipkart Product Reviews Sentiment Analyzer

This project is a Machine Learning-powered web application that analyzes product reviews from Flipkart and predicts the sentiment as **Positive**, **Negative**, or **Neutral**. It's built using Python, trained with real review data, and deployed using Streamlit Cloud.

---

## 🚀 Demo

👉 **[Live App on Streamlit Cloud](https://flipkart-reviews-sentiment-analysis2.streamlit.app/)**  


![image](https://github.com/user-attachments/assets/65271bee-d075-40c8-a976-fd69fabc1a1e)
![image](https://github.com/user-attachments/assets/38c6d78e-3d5a-44d9-8236-f712344da283)



---

## 📌 Features

- 🧠 **Text Sentiment Classification** using SVM
- 🗣️ Input any product review to see predicted sentiment
- 💬 Supports nuanced neutral feedback
- 🎨 Clean UI with background image and styled results
- ☁️ Deployed on Streamlit Cloud

---

## 🧠 Model Details

- **Vectorization**: TF-IDF
- **Classifier**: Support Vector Machine (LinearSVC)
- **Label Encoding**: Positive / Negative / Neutral
- **Accuracy**: ~92% on test data
- **Data**: Real-world Flipkart review dataset with pre-labeled sentiments

---

## 📁 Project Structure

```

flipkart-sentiment-app/
│
├── app.py                  # Streamlit app
├── sentiment\_svm\_model.pkl # Trained SVM model
├── tfidf\_vectorizer.pkl    # Saved TF-IDF vectorizer
├── label\_encoder.pkl       # Label encoder
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

````

---

## 💡 Sample Inputs

| Review Text | Predicted Sentiment |
|-------------|---------------------|
| *"The product is amazing, I love it!"* | Positive ✅ |
| *"It's okay. Not bad, not great."*     | Neutral ✅ |
| *"Terrible quality, broke in two days."* | Negative ✅ |

---



## 📦 Installation & Run Locally

### 1. Clone the repository:

```bash
git clone https://github.com/yourusername/flipkart-sentiment-app.git
cd flipkart-sentiment-app
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the app:

```bash
streamlit run app.py
```

---

## 📚 Dataset Overview

* **Columns**:

  * `product_name`: Name of the product
  * `product_price`: Price in ₹
  * `Rate`: User rating (1–5)
  * `Review`: Full review text
  * `Summary`: Summary of review
  * `Sentiment`: Target label — Positive, Negative, Neutral

* **Preprocessing**:

  * Lowercasing, removing HTML and special characters
  * Cleaned `Summary` field used for training
  * Balanced dataset across 3 sentiment classes

---

## ✨ Future Improvements

* Use a transformer-based model like BERT for deeper understanding
* Add visualization of sentiment distribution
* Batch upload of multiple reviews via CSV
* Multilingual review support (e.g., Hindi, Tamil)

---

## 🙋‍♀️ About the Creator

👩‍💻 Developed by **Pavan**

🎓 B.Tech NA | Passionate about AI, ML & Real-world Projects

🌐 [LinkedIn]() • [GitHub]()

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, improve, and share!

---



 🩺 PeriodPal ML – Menstrual Cycle & Ovulation Predictor

**PeriodPal ML** is a simple machine learning-powered web app built using **Python**, **scikit-learn**, and **Streamlit**. It helps users predict their **next period start date** and **approximate ovulation window** based on historical menstrual cycle data.

---

## 📌 Features

- 🔍 Predicts the next **menstrual cycle length** using ML (Random Forest).
- 🩸 Calculates the **next period start date**.
- 🧬 Predicts **ovulation date** (approx. 14 days before next period).
- 📉 Displays model **Mean Absolute Error (MAE)** for accuracy check.
- 💻 User-friendly **Streamlit web interface**.

---

## ⚙️ Tech Stack

| Tool            | Purpose                          |
|-----------------|----------------------------------|
| Python          | Core Programming Language        |
| Pandas          | Data handling and preprocessing  |
| scikit-learn    | ML model (RandomForestRegressor) |
| Streamlit       | Web App UI                       |
| VS Code / Colab | Development Environment          |

---

## 🚀 How to Run This Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/PeriodPal-ML.git
cd PeriodPal-ML
2. Install required packages
Make sure you have Python installed, then run:

bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is not available, install manually:

bash
Copy
Edit
pip install pandas scikit-learn streamlit
3. Run the app
bash
Copy
Edit
streamlit run app.py
The app will open in your browser at http://localhost:8501.

📂 Sample Input Data Format
Upload a CSV file (cycle_data.csv) with the following structure:

cycle_start_date	cycle_length
2024-01-01	28
2024-01-29	28
2024-02-26	27

📉 Model Accuracy
Uses Random Forest Regressor

Evaluates on test set using Mean Absolute Error (MAE)

Example: MAE ≈ 0.07 days (very accurate for average predictions)

🧑‍💻 Author

Developed by: Deepanshi Patil

Feel free to contribute or raise issues!

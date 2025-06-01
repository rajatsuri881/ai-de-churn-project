# AI-Powered Customer Churn Insights Platform 🚀

This project showcases a complete end-to-end pipeline combining **Data Engineering**, **Machine Learning**, and **a lightweight AI-powered UI**. It predicts customer churn using a cleaned telecom dataset and provides actionable insights through a local Streamlit app.

---

## 📦 Project Highlights

✅ Built an ETL pipeline with Pandas & SQLite  
✅ Cleaned and transformed customer data  
✅ Engineered features and trained a logistic regression model  
✅ Visualized model performance and feature importance  
✅ Created a local Streamlit app for real-time churn prediction  
✅ [Week 3 Plan: Integrate OpenAI for natural language data querying]

---

## 📁 Project Structure

ai_de_churn_project/
├── app/ # Streamlit web app
├── data/ # (ignored in Git) Raw + cleaned CSVs
├── model/ # Saved model .pkl file
├── notebooks/ # Jupyter notebooks (ETL, ML, interpretation)
├── churn.db # Local SQLite DB (ignored)
├── README.md


---

## 📊 Dataset

- **Telco Customer Churn Dataset**  
- Original Source: [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)  
- Preprocessed Dataset for ML: [📥 Download from Google Drive] (https://drive.google.com/file/d/1R6tm0lAQKyEXDX3G3XTgnT41rWF9w752/)

*Note: `ml_ready_churn.csv` was removed from GitHub due to size limits. Use the link above to download and place it in the `data/` folder.*

---

## 🧪 How to Run Locally

### 1. Clone the Repo
```bash
git clone https://github.com/rajatsuri881/ai-de-churn-project.git
cd ai-de-churn-project

2. Create Conda Environment

conda create -n ai_de_project python=3.10
conda activate ai_de_project
pip install -r requirements.txt  # optional

3. Launch the App

cd app/
streamlit run app.py


👤 Author
Rajat Suri
📍 Seattle, WA
📧 rajatsuri.881@gmail.com


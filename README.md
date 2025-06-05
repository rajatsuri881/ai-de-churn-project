# AI-Powered Customer Churn Insights Platform 🚀

This project showcases a complete end-to-end pipeline combining **Data Engineering**, **Machine Learning**, and **a lightweight AI-powered UI**. It predicts customer churn using a cleaned telecom dataset and provides actionable insights through a local Streamlit app.

---

## 📦 Project Highlights

✅ Built an ETL pipeline with Pandas & SQLite  
✅ Cleaned and transformed customer data  
✅ Engineered features and trained a logistic regression model  
✅ Visualized model performance and feature importance  
✅ Created a local Streamlit app for real-time churn prediction  
✅ Integrated OpenAI (GPT-3.5) for natural language SQL queries using LangChain
✅ Built a chatbot to answer questions like "What is the average MonthlyCharges?"

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

🧠 Natural Language Querying (Week 3)
This project uses LangChain + GPT-3.5 to allow users to ask natural language questions over the churn database. 

Example queries:
- "What is the average MonthlyCharges?"
- "How many customers are in the database?"
- "Show me the churn rate by contract type."


---

## 🧪 How to Run Locally

### 1. Clone the Repo

git clone https://github.com/rajatsuri881/ai-de-churn-project.git
cd ai-de-churn-project

### 2. Create Conda Environment

conda create -n ai_de_project python=3.10
conda activate ai_de_project
pip install -r requirements.txt  # optional

### 3. Add Your OpenAI API Key
Create a .env file in the project root:

OPENAI_API_KEY=your_openai_api_key_here
🛑 Do not share or commit this key!

Make sure .env is in .gitignore:

### 4. Launch the App

cd app/
streamlit run app.py

💡 Note: This will use your GPT-3.5 pay-as-you-go credits. You can add logging to track usage and cost per query.

### 🧱 DBT Workflow (Week 4)
## Run DBT Models
cd churn_dbt
dbt run

## Run DBT Tests
dbt test

## Serve DBT Docs Locally
dbt docs generate
dbt docs serve
Then visit: http://127.0.0.1:8080

### 💡 Natural Language SQL via OpenAI
Once configured, you can ask questions like:

"What is the average monthly charge?"
"How many customers have churned?"
"Show me customers with tenure > 12 months and monthly charges > $70"
These are handled using LangChain agents with access to your database schema.



👤 Author
Rajat Suri
📍 Seattle, WA
📧 rajatsuri.881@gmail.com

### 🛡️ License
This project is for educational and demonstration purposes only.


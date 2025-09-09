# Laptop_Price_Prediction_H

# LaptopPricePrediction

## 1. Project Overview
- This project is the sum of all we have learnt on Data Analysis
- Purpose: To calculate the price of laptop from a given set of specification. After being trained.
- Problem it solves: Reading the data, cleaning, and modeling
- [Dataset source](https://www.kaggle.com/datasets/muhammetvarl/laptop-price)

## 2. Project Folder Structure

## _All the commands will be runed on the terminal or the command line_

```
LaptopPricePrediction/
.
├── data
│   ├── processed
│   │   ├── laptop_price_clean.csv
│   │   ├── X.csv
│   │   └── y.csv
│   └── raw
│       └── laptop_price.csv
├── Interpreting_Result
│   └── Laptop_Price_Prediction_Report.docx
├── models
│   └── laptop_price_pipeline.pkl
├── notebooks
│   ├── 01_clean.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering_extracted.ipynb
│   └── 04_model_building.ipynb
├── README.md
├── requirements.txt
└── StreamlitApp.py

```

## 3. Setup 
Create a virtual environment 
```bash
python -m venv venv 
source venv/bin/activate  #linux/Mac
venv\Scripts\activate     #Windows
```
------
# 4. To install all dependencies run
```
pip install -r requirements.txt
```

# 5. To run the streamlit app run
```
cd notebooks
streamlit run StreamlitApp.py
```

### Click on the link to access streamlit app
[Streamlit App](https://appapppy-8ilag6w4d7hofgdzb6v57s.streamlit.app/)







# Stock Prices Chatbot

A minimal chatbot that uses FAISS to analyze and answer basic queries using the Stock-market-dataset from Kaggle.

 ## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Dataset](#dataset)
- [Directorystruct](#directory)

## Features
- Analyzes stock prices of 4 different companies('Amazon', 'Tesla', 'JPMorgan', 'Apple') in the analysis.ipynb.
- Uses FAISS to answer user queries with similarity index.

## Installation

1. Create a vertual environment 
•	pip install virtualenv
•	virtualenv env
•	env\Scripts\Activate.bat
2. Download the dataset into the env
• instructions on how to download dataset in [Dataset](#dataset)
3. clone the repository and place the files and folders inside the environment
4. to run the chatbot
• flask run

## Dataset

1. pip install kaggle
2. Create a new API token and download json file to it
3. Create a .kaggle folder
4. Move the json file to .kaggle folder
5. Download the dataset
•	Go to your activated env and download the dataset with the following command:
      kaggle datasets download -d jacksoncrow/stock-market-dataset

 ## Directorystruct

project/
│── .ipynb_checkpoints/
│── pycache/
│── env/
│── stock-market-dataset/
│── templates/
│── analysis.ipynb
│── app.py
│── .gitignore
│── Questionnaire.xlsx
│── requirements.txt
│── stock-market-dataset.zip

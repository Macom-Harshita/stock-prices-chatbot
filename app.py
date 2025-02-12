from flask import Flask, render_template, request
import re
import pandas as pd
import faiss
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask('__name__')

stocks = {
    'amazon': pd.read_csv("stock-market-dataset/stocks/AMZN.csv"),
    'apple': pd.read_csv("stock-market-dataset/stocks/AAPL.csv"),
    'tesla': pd.read_csv("stock-market-dataset/stocks/TSLA.csv"),
    'jpmorgan': pd.read_csv("stock-market-dataset/stocks/AMJ.csv")
}

features = ["Open", "Close", "Low", "High", "Volume"]

for stock, df in stocks.items():
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
    else:
        df.reset_index(inplace=True)

def find_similar_stock(company, query_stock):
    if company not in stocks:
        return f"Error: {company} not found."
    df = stocks[company]
    stock_data = df[features].values
    scaler = StandardScaler()
    stock_data_normalized = scaler.fit_transform(stock_data)
    dimension = stock_data_normalized.shape[1]  
    index = faiss.IndexFlatL2(dimension) 
    index.add(np.array(stock_data_normalized))
    query_stock_normalized = scaler.transform([query_stock]).astype(np.float32)
    D, I = index.search(np.array(query_stock_normalized), k=1)
    best_match_idx = I[0][0]
    best_match_date = df.iloc[best_match_idx]['Date']
    best_match_details = df.iloc[best_match_idx][features]
    return f"Most similar stock data found for {company} on {best_match_date}:\n{best_match_details.to_dict()}\n(Similarity Score: {D[0][0]})"

"""def chatbot_response(question):
    return "HELLOOOOOO PEOPLEEE!!"""

@app.route('/', methods=['GET', 'POST'])
def stock_predict():
    response = ''
    if request.method == 'POST':
        try:
            query_string = request.form['query']
            match = re.match(r"([A-Za-z]+)\s*Open:\s*([0-9\.]+),\s*Close:\s*([0-9\.]+),\s*Low:\s*([0-9\.]+),\s*High:\s*([0-9\.]+),\s*Volume:\s*([0-9]+)", query_string)
            if match:
                company = match.group(1).lower()
                user_open = float(match.group(2))
                user_close = float(match.group(3))
                user_low = float(match.group(4))
                user_high = float(match.group(5))
                user_volume = float(match.group(6))
                query_stock = [user_open, user_close, user_low, user_high, user_volume]
                response = find_similar_stock(company, query_stock)
            else:
                response = "Error: Invalid query format. Please use the correct format."
        except Exception as e:
            response = f"Error: {str(e)}"
    return render_template('chatbot.html', response=response)




"""@app.route('/', methods = ['POST', 'GET'])
def askyourques():
    response = ""
    if request.method == 'POST':
        question = request.form['ques']
        response = chatbot_response(question)
    return render_template('chatbot.html', response = response)"""

if __name__ == '__main__':
    app.run(debug = True)
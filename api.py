from flask import Flask, request, jsonify
import numpy as np
import pickle
from flask_cors import CORS
import json
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


df = pd.read_csv('./predictive_maintenance.csv')

df.drop(columns = ['Product ID'],inplace=True)
df[(df['Target']==1)&(df['Failure Type']=='No Failure')]
df.drop(df[(df['Target']==1)&(df['Failure Type']=='No Failure')].index,inplace=True)
df.drop(columns = ['Failure Type'],inplace=True)
df.groupby('Target').size()

feature_scaler = MinMaxScaler()
x_train = df.drop(columns=['Target', 'UDI'])
feature_scaler.fit(x_train)
print(x_train)


app = Flask(__name__)
CORS(app)

model = pickle.load(open('model.pkl', 'rb'))
print(type(model))  

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return "Hello"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from the request
        data = request.get_json(force=True)
        print("Received data: ", data)

        data = np.array(data['data'], dtype=object).reshape(-1, 1)
        print(data)             
        

        data = data.reshape(1, -1)  
        scaled_data = feature_scaler.transform(data)
        print("Scaled features: ", scaled_data)

        # Reshape the scaled data to 2D array
        features = np.array(scaled_data, dtype=object).reshape(1, -1)
        print("Features: ", features)

        prediction = model.predict(features)
        return str(prediction)

    except Exception as e:
        # Handle exceptions and return an error message
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

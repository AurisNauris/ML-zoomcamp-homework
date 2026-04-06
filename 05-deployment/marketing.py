import requests

#url = 'http://localhost:9696/predict'

url = 'https://young-breeze-5711.fly.dev/predict'

customer = {
    "gender": "male",
    "seniorcitizen": 1,
    "partner": "no",
    "dependents": "yes",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 6,
    "monthlycharges": 29.85,
    "totalcharges": 129.85,
}


response = requests.post(url, json = customer)
churn = response.json()

print("response", churn)

if churn['churn_probability'] >= 0.5:
    print("Send")
else:
    print("Don't")
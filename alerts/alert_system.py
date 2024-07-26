import joblib
import smtplib
from email.mime.text import MIMEText

import pandas as pd

def send_alert(message):
    msg = MIMEText(message)
    msg['Subject'] = 'Maintenance Alert'
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'maintenance_team@example.com'

    with smtplib.SMTP('smtp.example.com') as server:
        server.login('your_email@example.com', 'password')
        server.send_message(msg)

def check_for_alerts():
    model = joblib.load('data/models/fault_prediction_model.pkl')
    data = pd.read_csv('data/processed/processed_data.csv')
    
    predictions = model.predict(data[['temperature', 'vibration', 'humidity']])
    if any(predictions):
        send_alert('Maintenance needed for one or more machines!')

def main():
    check_for_alerts()

if __name__ == "__main__":
    main()

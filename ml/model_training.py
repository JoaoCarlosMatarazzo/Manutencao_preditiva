import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(data):
    X = data[['temperature', 'vibration', 'humidity']]
    y = data['fault']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    joblib.dump(model, 'data/models/fault_prediction_model.pkl')

def main():
    data = pd.read_csv('data/processed/processed_data.csv')
    train_model(data)

if __name__ == "__main__":
    main()


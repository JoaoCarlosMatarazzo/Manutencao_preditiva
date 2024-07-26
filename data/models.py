#Modelos de machine learning treinados.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os

# Caminhos para os arquivos de dados e modelo
dataset_path = 'data/dataset.csv'
model_path = 'data/model.joblib'

def load_data(path):
    return pd.read_csv(path)

def preprocess_data(df):
    X = df[['feature1', 'feature2']]
    y = df['label']
    return X, y

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    joblib.dump(model, model_path)
    print(f"Modelo salvo em {model_path}")

def load_model(path):
    if os.path.exists(path):
        return joblib.load(path)
    else:
        print(f"Modelo não encontrado em {path}")
        return None

def predict(model, X):
    return model.predict(X)

def main():
    df = load_data(dataset_path)
    X, y = preprocess_data(df)
    train_model(X, y)
    model = load_model(model_path)
    if model:
        sample_data = X.iloc[:5]  
        predictions = predict(model, sample_data)
        print("Predictions:", predictions)

if __name__ == "__main__":
    main()


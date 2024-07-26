import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

processed_data_path = 'data/processed_dataset.csv'
model_path = 'data/model.joblib'

def load_data(path):
    return pd.read_csv(path)
def evaluate_model(X_test, y_test, model):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1 Score: {f1:.2f}")
def main():
    df = load_data(processed_data_path)
    X = df[['feature1', 'feature2', 'feature_sum', 'feature_diff']]  # Ajuste conforme suas features
    y = df['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = joblib.load(model_path)
    evaluate_model(X_test, y_test, model)

if __name__ == "__main__":
    main()

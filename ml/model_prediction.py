import pandas as pd
import joblib

new_data_path = 'data/new_data.csv'
model_path = 'data/model.joblib'
predictions_path = 'data/predictions.csv'

def load_data(path):
    return pd.read_csv(path)
def load_model(path):
    return joblib.load(path)
def predict(model, X):
    return model.predict(X)
def save_predictions(predictions, path):
    pd.DataFrame(predictions, columns=['Prediction']).to_csv(path, index=False)
    print(f"Predictions saved to {path}")
def main():
    df = load_data(new_data_path)
    X_new = df[['feature1', 'feature2', 'feature_sum', 'feature_diff']]  # Ajuste conforme suas features
    model = load_model(model_path)
    predictions = predict(model, X_new)
    save_predictions(predictions, predictions_path)

if __name__ == "__main__":
    main()

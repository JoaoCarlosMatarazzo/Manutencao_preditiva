import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Caminho para o arquivo de dados bruto e processado
raw_data_path = 'data/dataset.csv'
processed_data_path = 'data/processed_dataset.csv'

def load_data(path):
    return pd.read_csv(path)

def handle_missing_values(df):
    df.fillna(df.mean(), inplace=True)
    return df

def normalize_data(df, columns):
    scaler = MinMaxScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df

def standardize_data(df, columns):
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df

def create_features(df):
    df['feature_sum'] = df['feature1'] + df['feature2']
    df['feature_diff'] = df['feature1'] - df['feature2']
    return df

def preprocess_data(df):
    df = handle_missing_values(df)
    df = create_features(df)
    df = normalize_data(df, ['feature1', 'feature2', 'feature_sum', 'feature_diff'])
    return df

def save_data(df, path):
    df.to_csv(path, index=False)
    print(f"Processed data saved to {path}")

def main():
    df = load_data(raw_data_path)
    df_processed = preprocess_data(df)
    save_data(df_processed, processed_data_path)

if __name__ == "__main__":
    main()

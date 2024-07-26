import pandas as pd

def preprocess_data(data):
    # Limpar e formatar dados
    df = pd.DataFrame(data)
    df = df.dropna()
    return df

def main():
    raw_data = pd.read_json('data/raw/sensor_data.json', lines=True)
    processed_data = preprocess_data(raw_data)
    processed_data.to_csv('data/processed/processed_data.csv', index=False)

if __name__ == "__main__":
    main()

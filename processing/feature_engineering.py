import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

raw_data_path = 'data/raw_dataset.csv'
processed_data_path = 'data/processed_dataset.csv'

def load_data(path):
    """Carrega dados de um arquivo CSV em um DataFrame."""
    return pd.read_csv(path)
def save_data(df, path):
    """Salva um DataFrame em um arquivo CSV."""
    df.to_csv(path, index=False)
    print(f"Dados salvos em {path}")
def feature_engineering(df):
    """Realiza engenharia de características no DataFrame."""
    df['feature_sum'] = df['feature1'] + df['feature2']
    df['feature_diff'] = df['feature1'] - df['feature2']
    numeric_features = ['feature1', 'feature2', 'feature_sum', 'feature_diff']
    scaler = StandardScaler()
    df[numeric_features] = scaler.fit_transform(df[numeric_features])
    if 'category_feature' in df.columns:
        encoder = OneHotEncoder(sparse=False, drop='first')
        encoded_features = encoder.fit_transform(df[['category_feature']])
        encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out())
        df = df.join(encoded_df)
        df.drop('category_feature', axis=1, inplace=True)
    return df
def main():
    df = load_data(raw_data_path)
    df_processed = feature_engineering(df)
    save_data(df_processed, processed_data_path)

if __name__ == "__main__":
    main()

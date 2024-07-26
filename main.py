#Lembrando que os dados são simulados e exemplos infundados 

import pandas as pd
from sensors.mock_sensor import generate_data_stream
from processing.feature_engineering import feature_engineering
from processing.data_storage import save_data, load_data
from ml.model_prediction import predict_with_model

def main():
    # Passo 1: Coletar dados simulados dos sensores
    print("Coletando dados simulados dos sensores...")
    num_samples = 100
    df_simulated_data = generate_data_stream(num_samples)
    
    # Salvar dados simulados
    simulated_data_path = 'data/simulated_sensor_data.csv'
    save_data(df_simulated_data, simulated_data_path)
    
    # Passo 2: Processar os dados (engenharia de características)
    print("Processando dados...")
    df_raw = load_data(simulated_data_path)
    df_processed = feature_engineering(df_raw)
    
    # Salvar dados processados
    processed_data_path = 'data/processed_dataset.csv'
    save_data(df_processed, processed_data_path)
    
    # Passo 3: Realizar previsões com o modelo treinado
    print("Realizando previsões...")
    # Exemplo fictício: carregar um modelo pré-treinado e realizar previsões
    # Modelos podem ser treinados e salvos em etapas anteriores
    predictions = predict_with_model(df_processed)
    
    # Exibir ou salvar previsões
    print("Predições realizadas:")
    print(predictions.head())
    
    # Opcional: Salvar previsões em um arquivo
    predictions_path = 'data/predictions.csv'
    predictions.to_csv(predictions_path, index=False)
    print(f"Predições salvas em {predictions_path}")

if __name__ == "__main__":
    main()

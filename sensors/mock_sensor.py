import random
import time
import pandas as pd
from datetime import datetime

# Função para gerar dados simulados do sensor
def generate_sensor_data():
    """Gera dados simulados para sensores de temperatura, umidade e vibração."""
    # Simular leituras de sensores
    temperature = round(random.uniform(15.0, 30.0), 2)  
    humidity = round(random.uniform(30.0, 70.0), 2)     
    vibration = round(random.uniform(0.0, 5.0), 2)      
    return {
        'timestamp': datetime.now(),
        'temperature': temperature,
        'humidity': humidity,
        'vibration': vibration
    }

def generate_data_stream(num_samples):
    """Gera uma série de dados simulados para um número especificado de amostras."""
    data = []
    for _ in range(num_samples):
        data.append(generate_sensor_data())
        time.sleep(1)  #1 segundo
    
    return pd.DataFrame(data)

def save_data(df, path):
    """Salva um DataFrame em um arquivo CSV."""
    df.to_csv(path, index=False)
    print(f"Dados simulados salvos em {path}")

def main():
    # Gerar e salvar dados simulados
    num_samples = 100  
    df_simulated_data = generate_data_stream(num_samples)
    save_data(df_simulated_data, 'data/simulated_sensor_data.csv')

if __name__ == "__main__":
    main()

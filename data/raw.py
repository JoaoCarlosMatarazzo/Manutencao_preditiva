import pandas as pd
import random
import time

raw_data_path = 'data/dataset.csv'

def simulate_sensor_data():
    temperature = random.uniform(20.0, 80.0)  
    vibration = random.uniform(0.0, 5.0)  
    humidity = random.uniform(30.0, 90.0)  
    timestamp = pd.Timestamp.now()
    return {
        'timestamp': timestamp,
        'temperature': temperature,
        'vibration': vibration,
        'humidity': humidity
    }

def collect_data(num_samples=100, delay=1):
    data = []
    for _ in range(num_samples):
        sensor_data = simulate_sensor_data()
        data.append(sensor_data)
        time.sleep(delay)
    return data

def save_data(data, path):
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)
    print(f"Raw data saved to {path}")

def main():
    data = collect_data(num_samples=10, delay=1)
    save_data(data, raw_data_path)

if __name__ == "__main__":
    main()

import random
import time
import json

def collect_sensor_data():
    data = {
        "temperature": random.uniform(20.0, 100.0),
        "vibration": random.uniform(0.1, 1.0),
        "humidity": random.uniform(30.0, 70.0)
    }
    return data

def main():
    while True:
        data = collect_sensor_data()
        with open('data/raw/sensor_data.json', 'a') as f:
            f.write(json.dumps(data) + '\n')
        time.sleep(5)

if __name__ == "__main__":
    main()


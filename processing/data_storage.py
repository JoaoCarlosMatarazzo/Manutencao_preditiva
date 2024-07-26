#usado para gerenciar a leitura e escrita de dados no armazenamento, 
# como bancos de dados, sistemas de arquivos ou serviços em nuvem.

import pandas as pd
import sqlite3

csv_file_path = 'data/processed_dataset.csv'
sqlite_db_path = 'data/database.db'

def save_to_csv(df, path):
    """Salva um DataFrame em um arquivo CSV."""
    df.to_csv(path, index=False)
    print(f"Dados salvos em {path}")

def load_from_csv(path):
    """Carrega dados de um arquivo CSV em um DataFrame."""
    return pd.read_csv(path)

def save_to_sqlite(df, db_path, table_name):
    """Salva um DataFrame em uma tabela de um banco de dados SQLite."""
    with sqlite3.connect(db_path) as conn:
        df.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"Dados salvos na tabela '{table_name}' do banco de dados {db_path}")

def load_from_sqlite(db_path, table_name):
    """Carrega dados de uma tabela de um banco de dados SQLite em um DataFrame."""
    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    return df

def main():
    # Exemplo de uso
    df = pd.DataFrame({
        'feature1': [0.1, 0.2, 0.3],
        'feature2': [0.4, 0.5, 0.6],
        'feature_sum': [0.5, 0.7, 0.9],
        'feature_diff': [-0.3, -0.3, -0.3],
        'label': [0, 1, 0]
    })

    save_to_csv(df, csv_file_path)
    df_loaded_csv = load_from_csv(csv_file_path)
    print("Dados carregados do CSV:")
    print(df_loaded_csv)
    save_to_sqlite(df, sqlite_db_path, 'data_table')
    df_loaded_sqlite = load_from_sqlite(sqlite_db_path, 'data_table')
    print("Dados carregados do SQLite:")
    print(df_loaded_sqlite)

if __name__ == "__main__":
    main()





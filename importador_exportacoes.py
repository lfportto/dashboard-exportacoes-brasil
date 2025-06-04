import os
import mysql.connector
import shutil

# Conexão com o MySQL
# MySQL connection
conn = mysql.connector.connect(
    host='INSIRA_O_HOST_AQUI',         # ex: 'localhost'
    user='INSIRA_SEU_USUARIO',         # ex: 'root'
    password='INSIRA_SUA_SENHA',       # ex: 'root1234'
    database='exportacoes',            # nome do banco de dados
    allow_local_infile=True
)
cursor = conn.cursor()

# Caminho para a pasta Downloads
# Path to the Downloads folder
downloads_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
processed_dir = os.path.join(downloads_dir, 'Arquivos processados')  # Processed files folder

# Criar a pasta se ela não existir
# Create the folder if it doesn't exist
os.makedirs(processed_dir, exist_ok=True)

# Procura por arquivos CSV que comecem com "EXP_"
# Search for CSV files starting with "EXP_"
for file in os.listdir(downloads_dir):
    if file.startswith("EXP_") and file.endswith(".csv"):
        ano = file[4:8]  # Pega os 4 dígitos do ano (ex: 2026)
                         # Get the 4-digit year (e.g. 2026)
        table_name = f"exp_{ano}"
        file_path = os.path.join(downloads_dir, file).replace('\\', '/')

        # Cria a tabela (se ainda não existir)
        # Create the table (if it doesn't already exist)
        create_sql = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            CO_ANO INT,
            CO_MES TEXT,
            CO_NCM TEXT,
            CO_UNID INT,
            CO_PAIS INT,
            SG_UF_NCM TEXT,
            CO_VIA TEXT,
            CO_URF TEXT,
            QT_ESTAT INT,
            KG_LIQUIDO INT,
            VL_FOB INT
        );
        """
        cursor.execute(create_sql)

        # Importa os dados do CSV
        # Import data from the CSV file
        load_sql = f"""
        LOAD DATA LOCAL INFILE '{file_path}'
        INTO TABLE {table_name}
        FIELDS TERMINATED BY ';'
        OPTIONALLY ENCLOSED BY '"'
        LINES TERMINATED BY '\\r\\n'
        IGNORE 1 ROWS;
        """
        cursor.execute(load_sql)
        conn.commit()

        print(f"✓ Arquivo {file} importado com sucesso para a tabela {table_name}.")
        # File successfully imported

        # Faz o append dos dados na tabela unificada
        # Append data to the unified table
        union_sql = f"""
        INSERT INTO tb_exportacoes_unificada
        SELECT * FROM {table_name};
        """
        cursor.execute(union_sql)
        conn.commit()
        print(f"✓ Dados da tabela {table_name} adicionados à tb_exportacoes_unificada.")
        # Data successfully appended

        # Renomeia o arquivo e move para a pasta "Arquivos processados"
        # Rename the file and move to "Arquivos processados" folder
        new_filename = f"Importado_{file}"
        new_path = os.path.join(processed_dir, new_filename)
        shutil.move(os.path.join(downloads_dir, file), new_path)
        print(f"✓ Arquivo movido para '{new_path}'.")
        # File moved to archive

        # break  # Processa apenas o primeiro arquivo encontrado
        # Uncomment if you want to stop after one file

cursor.close()
conn.close()

import pandas as pd
import os
import logging

BRONZE_PATH = r"C:\Users\Lusimar Silva\Documents\lusimar\projetosTECHBI\football-data-analytics\data\bronze\matches_bronze.csv"
SILVER_PATH = r"C:\Users\Lusimar Silva\Documents\lusimar\projetosTECHBI\football-data-analytics\data\silver"

logging.basicConfig(
    filename=r"C:\Users\Lusimar Silva\Documents\lusimar\projetosTECHBI\football-data-analytics\logs\pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_silver():

    try:

        logging.info("Starting Silver Layer")

        df = pd.read_csv(BRONZE_PATH)
        logging.info("Dataset Silver layer loaded successfully")

        # selecionar colunas relevantes
        df = df[[
            "Date",
            "HomeTeam",
            "AwayTeam",
            "FTHG",
            "FTAG",
            "FTR",
            "season"
        ]]

        # Renomear colunas
        df.columns = [
            "date",
            "home_team",
            "away_team",
            "home_goals",
            "away_goals",
            "result",
            "season" 
        ]

        # Converter data
        df["date"] = pd.to_datetime(df["date"], dayfirst=True)

        #Remover nulos
        df = df.dropna()

        output_path = os.path.join(SILVER_PATH, "matches_silver.csv")
        df.to_csv(output_path, index=False)
        logging.info("Silver layer created successfully")
        print("Silver layer created successfully")
    except Exception as e:

        logging.error(f"Error in Silver Layer: {str(e)}")

        print("Error during Silver pipeline execution")

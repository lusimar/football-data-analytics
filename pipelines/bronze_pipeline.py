import pandas as pd
import os
import logging

RAW_PATH = "data/raw"
BRONZE_PATH = "data/bronze"

logging.basicConfig(
    filename=r"C:\Users\Lusimar Silva\Documents\lusimar\projetosTECHBI\football-data-analytics\logs\pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_bronze():

    try:

        logging.info("Starting Bronze Layer")

        files = os.listdir(RAW_PATH)

        if not files:
            raise Exception("No files found in RAW folder")

        all_dfs = []

        for file in files:

            if file.endswith(".csv"):

                file_path = os.path.join(RAW_PATH, file)

                logging.info(f"Reading file: {file}")

                df = pd.read_csv(file_path)

                season = file.replace(".csv","")

                df["season"] = season

                all_dfs.append(df)

        bronze_df = pd.concat(all_dfs)

        output_path = os.path.join(BRONZE_PATH, "matches_bronze.csv")

        bronze_df.to_csv(output_path, index=False)

        logging.info("Bronze layer created successfully")

        print("Bronze layer created successfully")

    except Exception as e:

        logging.error(f"Error in Bronze Layer: {str(e)}")

        print("Error during Bronze pipeline execution")
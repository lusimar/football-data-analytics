import pandas as pd
import os
import logging

SILVER_PATH = r"C:\Users\Lusimar Silva\Documents\lusimar\projetosTECHBI\football-data-analytics\data\silver\matches_silver.csv"
GOLD_PATH = "data/gold"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_gold():

    try:
        
        logging.info("Starting Gold Layer")
        
        df = pd.read_csv(SILVER_PATH)

        #Total de gols por time

        home_goals = df.groupby("home_team")["home_goals"].sum()
        away_goals = df.groupby("away_team")["away_goals"].sum()

        total_goals = home_goals.add(away_goals, fill_value=0)

        goals_df = total_goals.reset_index()
        goals_df.columns = ["team", "total_goals"]

        #Vitórias por time
        home_wins = df[df["result"] == "H"].groupby("home_team").size()
        away_wins = df[df["result"] == "A"].groupby("away_team").size()

        total_wins = home_wins.add(away_wins, fill_value=0)

        wins_df = total_wins.reset_index()
        wins_df.columns = ["team", "wins"]

        #Média de gols por partida
        df["total_goals_match"] = df["home_goals"] + df["away_goals"]

        avg_goals = df["total_goals_match"].mean()

        avg_df = pd.DataFrame({
            "metric": ["avg_goals_per_match"],
            "value": [avg_goals]
        })

        #Salvar os resultados

        goals_df.to_csv(os.path.join(GOLD_PATH, "goals_by_team.csv"), index=False)
        wins_df.to_csv(os.path.join(GOLD_PATH, "wins_by_team.csv"), index=False)
        avg_df.to_csv(os.path.join(GOLD_PATH, "avg_goals.csv"), index=False)

        logging.info("Gold layer created successfully")

        print("Gold layer created successfully")

    except Exception as e:
        logging.error(f"Error in Gold Layer: {e}")
        print(f"Error in Gold Layer: {e}")
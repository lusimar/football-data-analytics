import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import os
import time
import logging

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def connect_sheet():

    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "credentials/credentials.json", scope
    )

    client = gspread.authorize(creds)

    return client.open("football_analytics")

def upload_dataframe(sheet, df, sheet_name):

    try:
        worksheet = sheet.worksheet(sheet_name)
        worksheet.clear()
    except:
        worksheet = sheet.add_worksheet(title=sheet_name, rows="1000", cols="20")

    worksheet.append_row(df.columns.tolist())

    for row in df.values.tolist():
        worksheet.append_row(row)
        time.sleep(1)  # evita erro 429

def run():

    try:

        logging.info("Sending GOLD to Sheets")

        sheet = connect_sheet()

        files = {
            "goals_by_team": "data/gold/goals_by_team.csv",
            "wins_by_team": "data/gold/wins_by_team.csv",
            "avg_goals": "data/gold/avg_goals.csv"
        }

        for name, path in files.items():

            df = pd.read_csv(path)

            upload_dataframe(sheet, df, name)

            logging.info(f"{name} uploaded successfully")

        print("Gold data sent to Google Sheets")

    except Exception as e:

        logging.error(f"Error sending to Sheets: {str(e)}")

        print("Error sending data")
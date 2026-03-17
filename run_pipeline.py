from pipelines.bronze_pipeline import run_bronze
from pipelines.silver_pipeline import run_silver
from pipelines.gold_pipeline import run_gold
from sheets.send_to_sheets import run as send_to_sheets

def run():

    print("Running Bronze Layer")
    run_bronze()

    print("Running Silver Layer")
    run_silver()

    print("Running Gold Layer")
    run_gold()  

    print("Sending data to Google Sheets")
    send_to_sheets()

if __name__ == "__main__":
    run()
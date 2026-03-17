from pipelines.bronze_pipeline import run_bronze
from pipelines.silver_pipeline import run_silver


def run():

    print("Running Bronze Layer")
    run_bronze()

    print("Running Silver Layer")
    run_silver()

if __name__ == "__main__":
    run()
import os
import sys
from config.env_config import setup_env
from etl.extract.extract import load_cards_data
from etl.transform.transform import remove_useless_columns
from etl.transform.transform import remove_duplicate_cards
from etl.transform.transform import remove_un_set_rows

def main():
    run_env_setup()

    print("Extracting data...")
    extracted_data = extract_data()
    print("Data extraction complete.")

    print("Transforming data...")
    transformed_data = transform_data(extracted_data)
    print("Data transformation complete.")

    print("Loading data...")
    load_data(transformed_data)
    print("Data loading complete.")

    print(
        f"ETL pipeline run successfully in "
        f'{os.getenv("ENV", "error")} environment!'
    )


def run_env_setup():
    print("Setting up environment...")
    setup_env(sys.argv)
    print("Environment setup complete.")


if __name__ == "__main__":
    main()

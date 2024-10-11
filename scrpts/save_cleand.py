import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

def save_to_postgres(cleaned_data: pd.DataFrame, db_url: str, table_name: str):
    """
    Save the cleaned data to a PostgreSQL database table.

    :param cleaned_data: DataFrame to save.
    :param db_url: PostgreSQL database URL.
    :param table_name: The name of the table where data will be stored.
    """
    try:
        # Create an engine to connect to the PostgreSQL database
        engine = create_engine(db_url)

        # Save the DataFrame to the PostgreSQL table
        cleaned_data.to_sql(table_name, engine, if_exists='replace', index=False)

        print(f"Data successfully saved to table '{table_name}' in the PostgreSQL database.")
    except SQLAlchemyError as e:
        print(f"Error occurred while saving to PostgreSQL: {e}")
    finally:
        # Ensure the connection is closed after the operation
        engine.dispose()

import pandas as pd
from datetime import datetime
import logging

# Set up logging
logging.basicConfig(
    filename='telegram_text_cleaning.log',  # Log file name
    level=logging.INFO,  # Log level (you can change this to DEBUG for more details)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
    datefmt='%Y-%m-%d %H:%M:%S'  # Log date format
)

class DataCleaning:
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the DataCleaning class with the input DataFrame.
        
        :param data: The original DataFrame to be cleaned.
        """
        self.data = data
        self.cleaned_data = data.copy()  # Create a copy for cleaning

    def check_identical_rows(self):
        """
        Check for identical rows in the DataFrame.
        Print the number of identical rows and the corresponding duplicated rows.
        """
        # Identify identical rows
        identical_rows = self.data[self.data.duplicated(keep=False)]
        identical_count = identical_rows.shape[0]  # Count of identical rows
        
        if identical_count > 0:
            print(f"There are {identical_count} identical rows:")
            print(identical_rows.reset_index(drop=True))  # Display identical rows
        else:
            print("There are no identical rows.")

    def remove_duplicates(self):
        """
        Remove identical rows from the DataFrame, return the number of removed duplicates,
        and return a DataFrame containing the duplicated rows.
        """
        # Identify duplicates
        duplicates = self.data[self.data.duplicated(keep=False)]
        initial_count = self.data.shape[0]  # Initial count of rows
        self.data = self.data.drop_duplicates(keep='first')  # Remove identical rows
        final_count = self.data.shape[0]  # Final count of rows
        removed_count = initial_count - final_count  # Count of removed duplicates
        
        print(f"Removed {removed_count} identical rows.")
        return self.cleaned_data, duplicates.reset_index(drop=True)

    def missing_values(self) -> int:
        """
        Check total missing values in the DataFrame.
        
        :return: Total count of missing values.
        """
        self.data['text'] = self.data['text'].str.strip()  # Remove leading/trailing whitespace
        self.data['text'] = self.data['text'].replace('', pd.NA)  # Replace empty strings with NaN
        initial_missing = self.data.isnull().sum().sum()  # Total missing values
        return initial_missing

    def remove_missing_values(self) -> pd.DataFrame:
        """
        Remove rows with missing values and return the cleaned DataFrame.
        """
        self.cleaned_data['text'] = self.cleaned_data['text'].str.strip()  # Remove leading/trailing whitespace
        self.cleaned_data['text'] = self.cleaned_data['text'].replace('', pd.NA)  # Replace empty strings with NaN
        self.cleaned_data = self.cleaned_data.dropna()  # Drop rows with any NaN values
        return self.cleaned_data

    def get_cleaned_data(self) -> pd.DataFrame:
        """
        Return the cleaned DataFrame.
        
        :return: The cleaned DataFrame.
        """
        return self.cleaned_data

    def check_duplicates(self) -> int:
        """
        Check for duplicates in the DataFrame and print the count.
        
        :return: Number of duplicate rows.
        """
        duplicate_count = self.data.duplicated().sum()  # Count of duplicate rows
        print(f"Number of duplicate rows: {duplicate_count}")
        return duplicate_count

    def check_missing_values(self) -> pd.Series:
        """
        Check for missing values in the DataFrame and print counts per column.
        
        :return: Series containing counts of missing values per column.
        """
        missing_values = self.data.isnull().sum()  # Count of missing values per column
        print("Missing values per column:")
        print(missing_values[missing_values > 0])  # Display only columns with missing values
        return missing_values

    def standardize_formats(self):
        """
        Standardize the formats of date and message IDs in the DataFrame.
        """
        # Standardize date format to ISO 8601
        self.cleaned_data['date'] = pd.to_datetime(self.cleaned_data['date']).dt.strftime('%Y-%m-%dT%H:%M:%SZ')
        print("Standardized formats for date.")
        return self.cleaned_data

    def remove_whitespaces(self):
        """
        Remove leading, trailing, and multiple spaces from text entries in the DataFrame.
        """
        self.cleaned_data['text'] = self.cleaned_data['text'].str.strip()  # Remove leading/trailing spaces
        self.cleaned_data['text'] = self.cleaned_data['text'].str.replace(r'\s+', ' ', regex=True)  # Replace multiple spaces with a single space
        print("Removed whitespaces from text entries.")
        return self.cleaned_data

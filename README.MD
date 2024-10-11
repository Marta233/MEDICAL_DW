Ethiopian Medical Business Data Scraping and Data Warehouse Project
Overview
This project focuses on building a data pipeline for Ethiopian medical business data scraped from Telegram channels. The goal is to collect, clean, and store the data in a data warehouse for further analysis and insights. The scraped data is then transformed using DBT (Data Build Tool) for efficient storage and querying within a centralized data warehouse.

Objective
Scrape text and image data from selected Ethiopian medical Telegram channels.
Clean and preprocess the scraped data to remove duplicates, handle missing values, and standardize formats.
Store the cleaned data in a data warehouse for future analysis.
Use DBT to perform data transformations and ensure data quality for seamless analysis and reporting.
Methodology
Data Collection:

Scrape text and images from targeted Telegram channels using the Telethon library.
Channels include:
https://t.me/DoctorsET
https://t.me/lobelia4cosmetics
https://t.me/yetenaweg
https://t.me/EAHCI
Data Cleaning:

Use Python (Pandas) to clean the scraped data by removing duplicates, handling missing values, and standardizing data formats (e.g., message dates, text formats).
Data Storage:

Set up a data warehouse to store the cleaned data for further processing and querying.
Data Transformation with DBT:

Use DBT to define models that transform raw scraped data into analysis-ready datasets.
Transformations include filtering, joining, and restructuring data to meet business requirements.
Test and document data transformations to ensure data accuracy and quality.
Project Structure
bash
Copy code
.
├── data/                           # Raw data (scraped messages, images)
├── dbt_project/                    # DBT project for transformations
├── logs/                           # Logs from scraping and cleaning
├── scripts/                        # Python scripts for scraping and cleaning
│   ├── telegram_scraper.py         # Script for scraping text and images
│   ├── data_cleaning.py            # Script for data cleaning
├── .env                            # Environment variables for API credentials
├── README.md                       # Project overview (this file)
└── requirements.txt                # Python dependencies

Installation
Clone the repository:

bash
Copy code
git clone https://github.com/marta233/MEDICAL_DW.git
Install dependencies:
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up environment variables:

Fill in the API credentials in the .env file.
Run the scraper:

bash
Copy code
python scripts/telegram_scraper.py
Run DBT transformations:

bash
Copy code
dbt run
Future Work
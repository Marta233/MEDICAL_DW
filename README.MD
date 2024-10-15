# Project Title
# Ethiopian Medical Business Data Scraping and Data Warehouse Project

## Overview
This project implements a data scraping and transformation pipeline that extracts information from public Telegram channels related to Ethiopian medical businesses. The collected data is cleaned, stored in a PostgreSQL database, and transformed using DBT (Data Build Tool) for further analysis.
## Table of Contents
1. [Project Structure](#project-structure)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Data Scraping](#data-scraping)
5. [Data Cleaning](#data-cleaning)
6. [Data Storage](#data-storage)
7. [Data Transformation](#data-transformation)
8. [API](#api)
9. [Contributing](#contributing)
10. [License](#license)

/project-root │ ├── /data # Folder for storing raw and processed data ├── /scrapers # Contains scripts for web scraping Ethiopian medical business data ├── /cleaning # Scripts for cleaning and pre-processing scraped data ├── /transformations # Code for transforming the cleaned data for warehouse storage ├── /warehouse # Data warehouse schema and setup files ├── /api # FastAPI app for serving data and API endpoints ├── README.md # Project README file └── requirements.txt # Python dependencies


## Installation

To set up this project locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/Marta233/MEDICAL_DW.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Ethiopian-Medical-Data-Warehouse
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the data warehouse by following the instructions in the `/warehouse` folder.

## Usage

### Running the Scrapers

To scrape data from Ethiopian medical businesses, run:

```bash
python scrapers/scraper_script.py


Running the API
To start the API and serve data from the warehouse, run the FastAPI application:

API
The API serves the data in the data warehouse and allows users to access information programmatically. It includes endpoints for:

Fetching business data by region.
Querying services offered by medical businesses.
Analyzing medical business trends.
API Documentation can be found at /docs after running the FastAPI server

bash
Copy code
uvicorn api.main:app --reload



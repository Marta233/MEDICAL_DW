Ethiopian Medical Business Data Scraping and Data Warehouse Project
Overview
This project is focused on scraping data from Ethiopian medical business-related public Telegram channels. The data collected is cleaned, stored in a PostgreSQL data warehouse, and transformed using DBT (Data Build Tool). The purpose of this project is to facilitate analysis and insights into Ethiopian medical businesses.

Table of Contents
Project Structure
Installation
Usage
Data Scraping
Data Cleaning
Data Storage
Data Transformation
API
Contributing
License
Project Structure
bash
Copy code
/project-root
│
├── /data             # Folder for storing raw and processed data
├── /scrapers         # Contains scripts for web scraping Ethiopian medical business data
├── /cleaning         # Scripts for cleaning and pre-processing scraped data
├── /transformations  # Code for transforming the cleaned data for warehouse storage
├── /warehouse        # Data warehouse schema and setup files
├── /api              # FastAPI app for serving data and API endpoints
├── README.md         # Project README file
└── requirements.txt  # Python dependencies
Installation
To set up this project locally, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/Marta233/MEDICAL_DW.git
Navigate to the project directory:

bash
Copy code
cd MEDICAL_DW
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the data warehouse: Follow the instructions provided in the /warehouse folder to configure and initialize the data warehouse.

Usage
Running the Scrapers
To collect data from Ethiopian medical businesses, run:

bash
Copy code
python scrapers/scraper_script.py
Running the API
To start the API and serve the scraped and transformed data, use:

bash
Copy code
uvicorn api.main:app --reload
The API will be accessible at http://127.0.0.1:8000 and the interactive documentation can be accessed at /docs.

Data Scraping
The scrapers pull relevant data (business names, services, locations, contact info, etc.) from public Telegram channels focused on Ethiopian medical businesses.

Data Cleaning
The cleaning scripts handle tasks like:

Removing duplicate entries
Correcting inconsistent data
Filling in missing information
Normalizing text for uniformity
Data Storage
The cleaned data is stored in a PostgreSQL database. This storage step ensures that the data is structured and ready for querying and transformation.

Data Transformation
Using DBT (Data Build Tool), the stored data is transformed into a structured and analysis-friendly format. DBT models are used to clean, join, and optimize the data for future use in reporting and analytics.

API
This project includes a FastAPI application that provides an interface for querying the data warehouse. The API offers endpoints to:

Retrieve business data by region
Fetch details on services offered by medical businesses
Analyze trends within Ethiopian medical businesses
API documentation is available at /docs once the server is running.

Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new feature branch:
bash
Copy code
git checkout -b feature-branch-name
Commit your changes.
Push to your fork:
bash
Copy code
git push origin feature-branch-name
Submit a pull request.
License
This project is licensed under the MIT License. For more details, see the LICENSE file.


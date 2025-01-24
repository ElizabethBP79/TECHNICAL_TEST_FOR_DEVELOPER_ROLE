# Medical_Api
  Medical_Api is a RESTful API built with FastAPI that is designed to manage the results of medical image processing. It allows performing CRUD (Create, Read, Update, Delete) operations on processing results, storing the data in a PostgreSQL database. The API receives data in JSON format, validates and normalizes the values, and computes averages before and after normalization.

# Project Structure
 The project is organized as follows:

          Medical_Api/
          │
          ├── App/
          │   ├── __init__.py
          │   ├── main.py              # Main file to run the API
          │   ├── schemas.py           # Data schema definitions (Pydantic)
          │   ├── models.py            # Database models definition (SQLAlchemy)
          │   ├── crud.py              # Functions interacting with the database
          │   ├── database.py          # Database configuration (SQLAlchemy)
          │   └── dependencies.py      # Dependencies for database connection
          │
          ├── data/                    # Folder for storing data files (if necessary)
          ├── requirements.txt         # Python dependencies requirements file
      ── README.md                     # This file

# Requirements
  To run this project, ensure you have the following dependencies:

    * Python 3.7+
    * PostgreSQL (database connection)
    * Python libraries defined in the requirements.txt file

# Installing Dependencies
    Install the necessary dependencies using pip:

      pip install -r requirements.txt

# Database Configuration
    The project is configured to use a PostgreSQL database. Ensure that PostgreSQL is installed and running. Also, make sure to create a database called medical_images_db (or modify the DATABASE_URL variable in the database.py file with your credentials).

# API Endpoints
  The API, built using FastAPI, offers the following endpoints to interact with the data:

  1. Create elements (POST)
    * Endpoint: /api/elements/
    * Description: This endpoint accepts a JSON payload representing the elements and stores them in the database after processing (normalization and calculations).
    * Payload (example):
    
          {
            "1": {
              "id": "aabbcc1",
              "data": [
                "78 83 21 68 96 46 40 11 1 88",
                "58 75 71 69 33 14 15 93 18 54",
                "46 54 73 63 85 4 30 76 15 56"
              ],
              "deviceName": "CT SCAN"
            },
            "2": {
              "id": "aabbcc2",
              "data": [
                "14 85 30 41 64 66 85 76 96 71",
                "68 53 85 9 35 52 68 0 17 5",
                "78 40 83 72 82 94 8 19 23 62"
              ],
              "deviceName": "CT SCAN"
            }
          }
  * Response: A list of the created elements with details such as the average before and after normalization.

  2. List elements (GET)
    * Endpoint: /api/elements/
    * Description: Retrieves all elements from the database. You can filter the elements by created_date.
    * Optional Parameters:
            created_date: Filter by creation date.
    * Response: A list of elements with details.

  3. Get a specific element (GET)
    * Endpoint: /api/elements/{id}/
    * Description: Retrieves a single element by its id.
    * Response: Element details.


  4. Update an element (PUT/PATCH)
    * Endpoint: /api/elements/{id}/
    * Description: Updates the device_name or id of an existing element.
    * Payload (example):

          { "device_name": "new_device_name" }

    * Response: The updated element.

  5. Delete an element (DELETE)
    * Endpoint: /api/elements/{id}/
    * Description: Deletes an element by its id.
    * Response: A confirmation message for deletion.

# Features
    1. Data Normalization: All values in the data field are normalized to a range of 0 to 1. The normalization is performed by dividing each value by the maximum value found in the data.
    2. Average Calculation: Two averages are computed:
          * Average before normalization: The average of the original data.
          * Average after normalization: The average of the normalized data.
    3. Data Validation: The API validates that all items in the data list are integers. If any invalid value is found, the API will return an error.


# Setup and Running the API
      1. Clone this repository:
        git clone https://github.com/ElizabethBP79/TECHNICAL_TEST_FOR_DEVELOPER_ROLE
          cd TECHNICAL_TEST_FOR_DEVELOPER_ROLE/3_RESTful_API

      2. Ensure your PostgreSQL database is running and accessible.
      3. Configure the database URL in database.py.
      4. Run the API with the following command:
      
          uvicorn App.main:app --reload
          
      5. The API will be available at http://127.0.0.1:8000/
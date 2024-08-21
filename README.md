# logging_apis

# FastAPI Application for Logging and Managing Exceptions

## Overview

This FastAPI application allows you to log and manage application exceptions in a MySQL database. It provides endpoints to save exceptions, retrieve application details, and get exceptions based on type and application ID.

## Features

- **Save Application Exceptions:** Log exceptions with detailed information, including category, message, stack trace, and more.
- **Get Application Exceptions:** Retrieve exceptions based on exception type and application ID.
- **Get Application Details:** Fetch detailed information about an application, including name, type, created date, and updated date.

## Requirements

- Python 3.7+
- FastAPI
- MySQL
- `logging_error_custom` library (ensure it is installed globally)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/pritzal/logging_apis.git
   cd logging_apis
   
##Create dotenv file as per your according

DB_USER=<your_mysql_username>
DB_PASSWORD=<your_mysql_password>
DB_HOST=<your_mysql_host>
DB_NAME=<your_database_name>


### Summary of the Instructions:

1. **Environment Setup**: Set up the `.env` file with database credentials.
2. **Running the Application**: Instructions to run the FastAPI app using Flask.
3. **API Documentation**: Describes the available endpoints and how to use them.

This `README.md` should help users set up and run your application smoothly.

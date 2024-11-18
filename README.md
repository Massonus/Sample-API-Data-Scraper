# Coding Resources API

This project provides a RESTful API for accessing, filtering, and managing coding resources. It uses FastAPI for
building the web application, MongoDB for data storage, and Scrapy for scraping coding resources data from a provided
endpoint.

## The API allows users to:

- Retrieve coding resources with pagination and filtering options.
- Trigger a data scraping job to fetch updated resources.

## Features

- **Get Coding Resources**: Retrieve a list of coding resources with support for pagination and filters (e.g., by type,
  topic, level, or keyword search).
- **Trigger Data Fetching**: Start a scraping process to update the coding resources in the database.
- **MongoDB Integration**: Data is stored and managed in MongoDB.
- **Customizable**: Easy to extend with additional endpoints or data sources.

## Installation

Follow these steps to set up and run the project locally:

### Prerequisites

Ensure you have the following installed on your machine:

- Python 3.8 or higher
- MongoDB server
- Bash (Linux/MacOS) or Command Prompt/PowerShell (Windows)
- Poetry (Python dependency management tool)

### Steps

#### Clone the Repository

```bash
git clone https://github.com/Massonus/Sample-API-Data-Scraper.git  
cd coding-resources-api
```

#### Set Up a Virtual Environment

```bash
python -m venv venv  
source venv/bin/activate  # Linux/MacOS  
venv\Scripts\activate     # Windows
```

#### Install Dependencies

Install the required Python packages using `poetry`:

```bash
poetry install
```

This will create a virtual environment and install all dependencies specified in `pyproject.toml`.

#### Configure MongoDB

- Ensure MongoDB is running on your machine.
- Edit the database configuration in `code_resources/code_resources/database.py` to point to your MongoDB instance.

#### Run the Scraper (Optional)

To populate the database initially, run the Scrapy spider:

```bash
bash run_scrapy.sh  # Linux/MacOS  
run_scrapy.bat      # Windows
```

#### Start the FastAPI Server

Launch the application on your local machine:

```bash
python main.py
```

The server will be available at [http://127.0.0.1:8001](http://127.0.0.1:8001).

## API Endpoints

### 1. Get Coding Resources

- **Endpoint**: `/resources`
- **Method**: `GET`

**Query Parameters**:

- `page` (default: 1) - Page number for pagination.
- `limit` (default: 10) - Number of resources per page.
- `types` - Filter by resource types (e.g., tutorial, documentation).
- `topics` - Filter by topics (e.g., web development, data science).
- `levels` - Filter by levels (e.g., beginner, intermediate).
- `search` - Keyword search in the resource descriptions.

**Example Request**:

```bash
curl "http://127.0.0.1:8001/resources?page=1&limit=5&types=tutorial"
```

**Example Response**:

```json
[
  {
    "id": 1,
    "description": "A beginner's tutorial on Python.",
    "url": "https://example.com",
    "types": [
      "tutorial"
    ],
    "topics": [
      "web development"
    ],
    "levels": [
      "beginner"
    ]
  }
]
```

### 2. Trigger Scraping

- **Endpoint**: `/fetch`
- **Method**: `POST`
- **Description**: Starts the Scrapy process to fetch and update coding resources.

**Example Request**:

```bash
curl -X POST http://127.0.0.1:8001/fetch
```

**Example Response**:

```json
{
  "status": "Scraping started successfully"
}
```

## Running Tests

To ensure the functionality works as expected, run the tests using `pytest`:

### Install test dependencies:

```bash
poetry add pytest pytest-mock
```

### Run tests:

```bash
pytest
```

## Project Structure

```graphql
coding-resources-api/
├── code_resources/
│   ├── code_resources/
│   │   ├── database.py   # MongoDB configuration
│   │   ├── pipeline.py   # MongoDB pipeline logic
│   │   ├── spider.py     # Scrapy spider for data scraping
│   ├── __init__.py
├── main.py               # FastAPI application
├── models.py             # Data models
├── requirements.txt      # Project dependencies
├── run_scrapy.sh         # Script to run Scrapy (Linux/MacOS)
├── run_scrapy.bat        # Script to run Scrapy (Windows)
├── test_main.py          # Tests for FastAPI endpoints
└── README.md             # Project documentation
```

## Notes

- The scraper fetches data from the endpoint: `https://api.sampleapis.com/codingresources/codingResources`.
- Customize filtering and database logic in the relevant sections of the code.
- Feel free to fork and extend this project for your specific needs! 😊

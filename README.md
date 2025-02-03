# Internship Data Collector

This repository is a Scrapy-based project designed to scrape internship data from a specified GitHub repository and store the collected information in a MongoDB database. The project is modular and extensible, ensuring efficient data collection and management.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Files Overview](#files-overview)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Overview

The **Internship Data Collector** uses the Scrapy framework to scrape internship opportunities from GitHub and processes the data for storage in MongoDB. It enables you to manage and analyze internship data effectively.

## Features

- Scrapes internship data (e.g., company, title, date, location, and URL).
- Ensures unique entries using SHA-256 hashing for item IDs.
- Stores data in a MongoDB database.
- Modular pipeline and middleware design for extensibility.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/A-Lassi/internship-data-collector.git
   cd internship-data-collector
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
3. Set up MongoDB on your local or remote server. Update the connection settings in `settings.py` (see the Configuration section).

## Usage

1. Run the scrapy spider to collect data:
   ```bash
   scrapy crawl internships
2. The scraped data will be stored in the configured MongoDB database.

## Files Overview

### `internships.py`
The spider responsible for scraping internship data from the GitHub repository.
Key details:
- Parses table rows to extract internship data.
- Retrieves attributes like `company`, `title`,  `date`, `location`, and `URL`.

### `items.py`
Defines the data model (`InternshipItem`) for the scraped items. Fields include:
- `_id`: Unique ID for each item (computed in `pipelines.py`).
- `url`, `company`, `title`, `date`, `location`: Fields for storing internship data.

### `pipelines.py`
Handles data processing and storage:
- Removes duplicated by computing hashes for URLs.
- Inserts valid, unique data into a MongoDB collection (`internship`).

### `middlewares.py`
Contains middleware definitions for:
- Processing requests and responses.
- Managing errors and signals for the spider.

### `settings.py`
Holds project-level configurations, including:
- Scrapy settings such as `BOT-NAME`, `SPIDER-MODULES`, and `ITEM_PIPELINES`.
- MongoDB connection settings (`MONGO_URI` and `MONGO_DATABASE`).

## Configuration

Update the `settings.py` file to configure:
- **MongoDB Connection**:
  ```python
  MONGO_URI = "mongodb://localhost:27017"
  MONGO_DATABASE = "internship_db"
- **Pipeline**: Ensure `InternshipPipeline` is enabled in the `ITEM_PIPELINES` dictionary:
  ```python
  ITEM_PIPELINES = {
      "internship.pipelines.InternshipPipeline": 300,
  }

## Contributing

Contributions are welcome! If ytou find a bug or have an idea for an improvement:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.


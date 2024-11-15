# ETL PIPELINE - UK Stock Market Price Tracker

This project is designed to track and analyze prices in the UK stock exchange market by employing a comprehensive data pipeline. The pipeline scrapes stock market data, processes it through an ETL (Extract, Transform, Load) workflow, and stores the refined data in a MySQL database for advanced analytics.

## Features

- **Web Scraping**: Automated data extraction from UK stock exchange websites.
- **ETL Process**: End-to-end data orchestration, including extraction, transformation, and loading for premium analytics.
- **Database Integration**: Processed data is stored in a MySQL database for persistent and structured storage.
- **Dockerized Workflow**: Portable and reusable containerization ensures the application can be run seamlessly on any system.

---

## Prerequisites

Before running this project, ensure you have the following installed:

1. **Docker**: For containerization and portability.
2. **MySQL**: To set up the database for storing processed data.
3. **Python**: Required for the web scraping and ETL scripts (check dependencies in `requirements.txt`).

---

## Installation and Setup

### Clone the Repository

```bash
git clone https://github.com/fredie7/data_etl.git
cd uk-stock-price-tracker
```

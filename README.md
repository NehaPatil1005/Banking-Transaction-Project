# Banking Transaction ETL and Analytics Project

## Project Overview

This project demonstrates an end-to-end banking transaction data pipeline using Python and MySQL. It extracts raw banking transaction data from CSV files, performs data cleaning and validation, separates valid and rejected records, loads valid transactions into a MySQL database, and generates analytical reports using SQL.


## Technology Stack

- **Programming Language:** Python 3.12
- **Data Processing:** Pandas
- **Database:** MySQL
- **Database Connectivity:** MySQL Connector
- **Query Language:** SQL
- **Testing:** Pytest
- **Version Control:** Git and GitHub
- **CI/CD:** GitHub Actions
- **Development Environment:** VS Code

## Project Architecture

The project follows an ETL (Extract, Transform, Load) architecture.

1. **Extract:** Read raw banking transaction data from CSV files using Pandas.
2. **Transform:** Validate transaction records and identify duplicate IDs and invalid transaction amounts.
3. **Separate:** Store valid and rejected transactions in separate CSV files.
4. **Load:** Insert valid transaction records into MySQL.
5. **Analyse:** Execute SQL queries to analyse transaction amounts, transaction types, and customer activity.
6. **Report:** Generate a banking transaction summary using Python and MySQL.

### Architecture Flow

```text
Raw CSV Data
     |
     v
Python ETL Pipeline
     |
     v
Data Validation
     |
     +------------------+
     |                  |
     v                  v
Valid Records     Rejected Records
     |
     v
MySQL Database
     |
     v
SQL Analytics
     |
     v
Daily Banking Report
```


## Project Folder Structure

```text
Banking-Transaction-Project/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── rejected/
│
├── logs/
├── reports/
├── sql/
│   └── banking_analysis.sql
│
├── src/
│   ├── etl_pipeline.py
│   ├── load_to_mysql.py
│   └── daily_report.py
│
├── tests/
│   └── test_transactions.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

**Note:** This represents the main project files. Include any additional files that actually exist in your project.


## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/NehaPatil1005/Banking-Transaction-Project.git
```

### 2. Navigate to the Project Folder

```bash
cd Banking-Transaction-Project
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment (Windows PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure MySQL

- Start your MySQL server.
- Create a database named `banking_analytics`.
- Create the `transactions` table using the SQL schema provided in the project.
- Update the database connection settings as required.

### 7. Run the ETL Pipeline

```bash
python src/etl_pipeline.py
```

### 8. Load Data into MySQL

```bash
python src/load_to_mysql.py
```

### 9. Generate the Daily Report

```bash
python src/daily_report.py
```

### 10. Run Automated Tests

```bash
python -m pytest tests/ -v
```


## Key Features

- Extracts banking transaction data from CSV files.
- Validates transaction records using Python and Pandas.
- Identifies duplicate transaction IDs.
- Rejects transactions with invalid or negative amounts.
- Separates valid and rejected records.
- Loads valid transaction data into MySQL.
- Prevents duplicate inserts using `INSERT IGNORE`.
- Performs SQL-based transaction analysis.
- Generates daily banking transaction summaries.
- Includes automated unit tests using Pytest.
- Uses GitHub Actions for continuous integration (CI).


## Sample Project Results

The project was tested using 10 sample banking transactions.

| Metric | Result |
|---|---:|
| Total raw records | 10 |
| Valid transactions | 8 |
| Rejected transactions | 2 |
| Successful transactions | 7 |
| Failed transactions | 1 |
| Total transaction amount | 34,500.00 |

### Transaction Analysis

| Transaction Type | Count | Total Amount |
|---|---:|---:|
| DEPOSIT | 4 | 18,500.00 |
| WITHDRAWAL | 2 | 2,000.00 |
| TRANSFER | 2 | 14,000.00 |

### Data Quality Results

- One transaction was rejected because its amount was negative.
- One transaction was rejected because its transaction ID was duplicated.


## Testing and Continuous Integration

The project includes automated testing using Pytest.

### Unit Tests

The following scenarios are tested:

1. Valid transactions are accepted.
2. Negative transaction amounts are rejected.
3. Duplicate transaction IDs are rejected.

### GitHub Actions

A GitHub Actions workflow automatically runs when code is pushed to the `main` branch or a pull request is created.

The workflow performs:

- Python environment setup.
- Dependency installation.
- Python syntax validation.
- Automated test execution.

This helps maintain code quality and identify errors during development.
## Future Improvements

The following enhancements can be added to the project:

- Implement advanced data validation rules.
- Add structured logging and error handling.
- Automate daily report generation.
- Integrate Apache Airflow for workflow orchestration.
- Implement incremental data loading.
- Build interactive dashboards using Power BI.
- Migrate the pipeline to Azure cloud services.

## Author

**Neha Patil**

GitHub: https://github.com/NehaPatil1005
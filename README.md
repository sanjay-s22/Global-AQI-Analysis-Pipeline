**# Global AQI Analysis Pipeline**



This project establishes a complete, reproducible data pipeline to ingest, store, process, and visualize global Air Quality Index (AQI) data.



\## 🚀 Technologies



\* \*\*Development Environment:\*\* Jupyter Notebook

\* \*\*ETL \& Ingestion:\*\* Python (Pandas, SQLAlchemy)

\* \*\*Database:\*\* MySQL

\* \*\*Analytics \& Visualization:\*\* Power BI (SQL Queries, DAX)



**## 🛠️ Setup \& Execution**



\### Prerequisites



1\.  \*\*MySQL Server\*\* must be running locally.

2\.  Install Python dependencies: `pip install pandas sqlalchemy pymysql`.

3\.  Ensure the raw data file, \*\*`global\_aqi\_project\_data.csv`\*\*, is in this directory.



**### Phase 1: Database Setup**



You must first create the target database schema in MySQL:



CREATE DATABASE aqi\_project;



**### Phase 2: Data Ingestion**



Run the Python script to load data into the `global\_aqi` table.



You can execute this from your \*\*terminal\*\* or using the \*\*`!` magic command in a Jupyter cell\*\*:





**### Phase 3: Power BI Analysis**



Use the file \*\*`powerbi\_analytics.md`\*\* (which contains the SQL and DAX) to build the dashboard:



1\.  \*\*Import Raw Data:\*\* Connect Power BI to the `aqi\_project` database and import the `global\_aqi` table.

2\.  \*\*Import Aggregations:\*\* Run the \*\*5 SQL Queries\*\* from the analytics file as separate data sources (e.g., `Top 10 Cities`).

3\.  \*\*Modeling:\*\* Apply the \*\*5 DAX Formulas\*\* from the analytics file to the main `global\_aqi` table to create KPIs and calculated columns.



**## 📁 Repository Structure**



| File | Purpose |

| :--- | :--- |

| \*\*`aqi\_data.py`\*\* | Python script to load CSV to MySQL. |

| `powerbi\_analytics.txt` | Contains all 5 SQL and 5 DAX definitions. |

| `README.md` | Project documentation. |

| `.gitignore` | Excludes the large `global\_aqi\_project\_data.csv` file. |

| \*\*`jupyter\_sql.txt`\*\* | Verification commands for Jupyter Notebook testing. |


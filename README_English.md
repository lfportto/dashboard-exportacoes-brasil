# 📦 Brazilian Export Mapping (2022 - 2025)

📄 [Versão em português](README.md)

## Description
This project focuses on analyzing Brazilian exports from 2022 to 2025, based on public data provided by the federal government. Using a combination of tools such as MySQL, Python, and Power BI, the solutions were developed for importing, modeling, and interactively visualizing the data, with a focus on logistical and commercial insights.

## Objective
Analyze the behavior of Brazilian exports by answering the following key questions:
- Which URFs (Brazilian Customs Units) handle the export processes?
- What are the main types of goods exported by state?
- What are the top destination countries for Brazilian exports?
- Is there seasonality in the monthly cargo export flow?

## Tools Used
- **MySQL**: Storage, structuring, and creation of optimized SQL views.
- **Python**: Automation of massive CSV file imports into MySQL.
- **Power BI**: Database connection, Power Query transformations, DAX metrics, and dashboard development.

## Access the Dashboard
🔗 [Click here to view the dashboard on Power BI](https://app.powerbi.com/view?r=eyJrIjoiYTVmZWQ0NWQtOGFjYy00MzhkLWE5MjAtNWZkNzc1ODc4MTllIiwidCI6ImNmNzJlMmJkLTdhMmItNDc4My1iZGViLTM5ZDU3YjA3Zjc2ZiIsImMiOjR9&embedImagePlaceholder=true)

## Dashboard Preview
![Brazilian Export Mapping Dashboard (2022 - 2025)](https://github.com/user-attachments/assets/e4e757a4-f0d4-4d2a-b40b-dd710d200d8a)

## Process Stages (ELT)
**1. Extract:**  
Raw export data was obtained from the official open data portal of the Brazilian government, provided in `.csv` format by the Ministry of Development, Industry, Trade and Services.  

**2. Load:**  
The CSV files were first loaded into MySQL using a Python script that automatically detects new files and imports them into year-specific tables.  

**3. Transform:**  
Data transformations (joins, aggregations, calculations, and filters) were performed within Power BI’s Power Query, ensuring flexibility and ease of updates without altering the original database.  

**4. Visualization:**  
With the data prepared, KPIs, DAX measures, and visualizations were created in Power BI to answer the project’s key questions. The dashboard was then published for public access.

## Python Automation
A Python script was developed to automate the following tasks:
- Detect `.csv` files starting with `EXP_` in the Downloads folder.
- Create the corresponding table in MySQL (if not already created).
- Import the data using `LOAD DATA LOCAL INFILE`, ensuring fast performance.
- Run a `UNION` to append the new data to the consolidated table (`tb_exportacoes_unificada`).
- Rename the original file by adding the prefix `Importado_` (`Imported_`).
- Move the processed file into a folder called `Arquivos processados` (`Processed files`).  
📁 [View the Python script here]()

## Data Source
The data used in this project is publicly available at:  
🔗 [Foreign Trade Statistics - Open Data - Ministry of Development, Industry, Trade and Services](https://www.gov.br/mdic/pt-br/assuntos/comercio-exterior/estatisticas/base-de-dados-bruta)

## About the Project
This project was developed as part of the course "Information Technology Applied to Operations and Process Management" in the 6th semester of the undergraduate degree in Industrial Production Management Technology, at Faculdade de Tecnologia de São José dos Campos - Prof. Jessen Vidal (FATEC SJC).

## License
This project is licensed under the [MIT License](LICENSE).

## Tags
`#Python` `#MySQL` `#PowerBI` `#Exports` `#DataAnalysis` `#Dashboard` `#DataEngineering` `#ETL` `#ELT` `#BusinessIntelligence` `#BI` `#DataVisualization` `#PublicData` `#BrazilExports`

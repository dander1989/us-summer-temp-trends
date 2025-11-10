# U.S. Summer Temperature Trends (2005–2025)

This project explores how average summer (June–August) temperatures have changed across major U.S. cities over the past 20 years.

## Objectives
1. Collect historical daily temperature data using Open-Meteo’s public API.
2. Aggregate and analyze city-level temperature trends.
3. Convert tabular data into spatial layers.
4. Visualize trends on a U.S. map.

## Project Structure
- data/
  - raw/ (raw temperature data from API)
  - processed/ (cleaned or aggregated datasets)
  - outputs/ (final maps or visualizations)
- scripts/ (Python scripts for each ETL stage)
- notebooks/ (optional Jupyter notebooks)

## Tools
- Python (pandas, geopandas, matplotlib, plotly)
- QGIS (optional)
- GitHub for version control

## Setup
```bash
# clone repo
git clone https://github.com/<your-username>/us-summer-temp-trends.git
cd us-summer-temp-trends

# create and activate environment
python -m venv .venv
.venv\Scripts\activate

# install dependencies

pip install -r requirements.txt


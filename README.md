# Gene Editing Data Collection

This repository contains code for collecting data related to gene editing from Medline, a trusted source of biomedical literature. The collected data includes articles related to gene editing from Medline (https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/).

## Files

The repository includes the following files:

- `Data_collection.py`: Python script for data collection from Medline.
- `Unzipping.py`: Python script for unzipping the files downloaded from Medline.
- `Find_all_articles.py`: Python script for finding articles related to gene editing.
- `Publications_during_the_time.py`: Python script for generating a graph with the distribution of gene editing-related publications over time.
- `Most_active_researchers.py`: Python script for identifying the 20 most active researchers in the field of gene editing and generating a chart with their information.
- `Output/`: Folder containing the following generated files:
  - `hist.png`: Graph showing the distribution of gene editing-related publications over time.
  - `result.csv`: CSV file containing metadata of the collected articles.
  - `top_20_authors_plot.png`: Chart showing the information of the 20 most active researchers in the field of gene editing.

## Data Collection Process

1. Data collection: The `Data_collection.py` script collects data from Medline using their core repository. It unzips all the files and finds articles related to gene editing using relevant keywords. It retrieves metadata such as authors and publication dates.

2. Data processing: The collected data is processed using various scripts. The `Publications_during_the_time.py` script counts the total number of articles related to gene editing and generates a graph showing the distribution of gene editing-related publications over time. The `Most_active_researchers.py` script identifies the 20 most active researchers in the field of gene editing and generates a chart with their information.

## Contact

If you have any questions or suggestions, please feel free to contact at dzhunmykola@gmail.com

# Ebuy data prediction

## Description of files

### Code files
1. purchase_prophecy.py - predicts future purchases
2. Graph comparison for test and actual.ipynb - plots comparing predicted and actual purchase amounts of raw material, to visualise accuracy of model
3. Dataset cleaning and generation.ipynb - consolidates sale data to obtain required amount of each raw material
4. sales_prophecy.py - predicts future sales/required amount of each raw material, based on cleaned data from Dataset cleaning and generation.ipynb
5. Plots.ipynb - plot for purchase and sale of each raw material over time

Note: before running .py files, remember to download dependencies listed in requirements.txt by running `pip install -r requirements.txt`

### Data sets

1. Master Data (Purchase).xlsx - Purchase data for 3 outlets, from 2018/01 to 2020/11 (inclusive)
2. Master Data (Sales).xlsx - Sales data for 3 outlets, from 2018/01 to 2020/12 (inclusive)
3. Collated dataset - Sheet1.csv - Product's mapping to raw materials, obtained from Data Summary.docx.

### Directories
1. churned datasets - required amount of each raw material each day (past data)
2. graphs - generated graphs
3. prediction datasets - required amount of each raw material each day (prediction)
4. purchase forecast datasets - prediction and actual data of test sets for amount of each raw material to purchase/purchased

### Other documents
1. Data Summary.docx - Summary of the data
2. Answer Sheet.xlsx - Filled in by participants in their predicted results in this Answer sheet.
Population of Kazakhstan by Regions and Years Animated
======================================================================

## Installation

Clone the repository

```shell
$ git clone https://github.com/open-data-kazakhstan/population-projections-by-regions.git
```
Requires Python 3.11.3 

Create a virtual environment and activate it 

```bash
pip install venv
python -m venv /path/to/localrepo
```
Swicth to venv directory by using cd comand
```bash
cd /path/to/localrepo
Scripts/activate
```

Install dependecies in venv by using pip
```bash
pip install -r requirements.txt
```
Run the project:
```bash
python scripts/main.py
```

## Data 

Sourse data is in xslx format and located in archive/source.xslx. Data soursed from https://stat.gov.kz/api/iblock/element/6584/file/ru/

We downoladed data from that source and located in acrhive as source.xsls

We have processed the source data to make it normalized and derived  several aggregated datasets from it:

* archive/source.xsls - sourse data 
* acrhive/kazpop.csv - unpivoted sourse data 
* data/csv_final.csv - expanded main dataset which predicts populations from 2023 to 2050
* data/rsl1.csv - final dataset expanded to 10 steps to make vizualization smoother
* datapackge.json - conatins all of the key information about our dataset

## Scripts overview

1. unpivot.py takes the Excel spreadsheet with initial population data and unpivots it to a standard CSV format for further work
2. regression.py uses kazpop.csv from step 1, trains a model on the existing data and builds population projections for each area up to 2050
3. wrang_data.py cleans up the data resulting from step 2 and improves some projections for areas with few initial  population values.
4. animate.py uses matplotlib to create an infographic about populations over the years and exports it to a gif file

## Visualization

Final result is visualized data that displays and predicts the population of Kazakhstan from 2000 to 2050:
<img src="population-animation.gif" alt="population-kazkhstan" width="450" height="800">

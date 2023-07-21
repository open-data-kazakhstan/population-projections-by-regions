Population of Kazakhstan by Regions and Years Animated
======================================================================

[toc]

---

Made by @sanzhik22 @msolodilin @Mikanebu

---
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

We downoladed data from that sourse and located in acrhive as source.xsls

We have processed the source data to make it normalized and derived from it several aggregated datasets:

* archive/source.xsls - sourse data 
* acrhive/kazpop.csv - unpivoted sourse data 
* data/csv_final.csv - expanded main dataset which is predicts population from 2023 to 2050
* data/rsl1.csv - dinal dataset expanded to 10 steps to make vizualization smoother
* datapackge.json - conatins all key informations about our dataset

## Visualization

Final result is visualized data that displays and predict population of Kazakhstan from 2000 to 2050:
![population-kazkhstan](population-animation.gif)
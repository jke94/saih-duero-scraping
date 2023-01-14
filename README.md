[![Main branch pipeline](https://github.com/jke94/saih-duero-scraping/actions/workflows/main-branch.yml/badge.svg)](https://github.com/jke94/saih-duero-scraping/actions/workflows/main-branch.yml)

[![PyPI version](https://badge.fury.io/py/saih-duero-scraping.svg)](https://badge.fury.io/py/saih-duero-scraping)
# Saih Duero Scraping  - Python Package
Source code to build a python package for web scraping operations over Saih Duero web page and save data as CSV file.

## A. Pypi - Python Repository Package
- Link: [saih-duero-scraping](https://pypi.org/project/saih-duero-scraping/)

## B. How to use it...

### B.1 - Install python pacakge with pip tool.

```
pip install saih-duero-scraping
```

### B.2 - Example of code.

- Source code: [example.py](https://github.com/jke94/saih-duero-scraping/blob/main/example.py)

```
from saih_duero_scraping.gauging_collection import GaugingCollection
from saih_duero_scraping.gauging_enum import GaugingStation
from saih_duero_scraping.hydrologic_years import HydrologicYears
from saih_duero_scraping.data_downloader import DataDownloader

datadownloader = DataDownloader()

# You can add a simple URL.
datadownloader.add_url(
    GaugingCollection[GaugingStation.Leon].gauging_code, 
    HydrologicYears.year_2018
)

# You can add several URLs.
datadownloader.add_urls(
    [
        dict(
            gauging_code = GaugingCollection[GaugingStation.MorlaDeLaValderia].gauging_code, 
            hydrologic_year = HydrologicYears.year_2018
        ),
        dict(
            gauging_code = GaugingCollection[GaugingStation.Zamora].gauging_code, 
            hydrologic_year = HydrologicYears.year_2019
        ),
        dict(
            gauging_code = GaugingCollection[GaugingStation.Valladolid_Esgueva].gauging_code, 
            hydrologic_year = HydrologicYears.year_2020
        ),
        dict(
            gauging_code = GaugingCollection[GaugingStation.MoralesDelRey].gauging_code, 
            hydrologic_year = HydrologicYears.year_2021
        )
    ]
)

# Finally to call the method to download the data sets.
datadownloader.download_data()
```

- Ouput:

A 'Data' folder it´s created with the following info:

```
PS H:\Repositories\saih-duero-scraping\data> ls


    Directorio: H:\Repositories\saih-duero-scraping\data


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        14/01/2023     15:54                csv
d-----        14/01/2023     15:54                txt
-a----        14/01/2023     15:54            926 summary.txt


PS H:\Repositories\saih-duero-scraping\data> ls .\csv\


    Directorio: H:\Repositories\saih-duero-scraping\data\csv


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        14/01/2023     15:54         254368 Leon_hidroyear_2018-2019.csv
-a----        14/01/2023     15:54         258765 MoralesdelRey_hidroyear_2021-2022.csv
-a----        14/01/2023     15:54         257251 MorladeLaValderia_hidroyear_2018-2019.csv
-a----        14/01/2023     15:54         257630 Valladolid-Esgueva_hidroyear_2020-2021.csv
-a----        14/01/2023     15:54         250941 Zamora_hidroyear_2019-2020.csv


PS H:\Repositories\saih-duero-scraping\data> ls .\txt\


    Directorio: H:\Repositories\saih-duero-scraping\data\txt


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        14/01/2023     15:54         246673 Leon_hidroyear_2018-2019.txt
-a----        14/01/2023     15:54         251051 MoralesdelRey_hidroyear_2021-2022.txt
-a----        14/01/2023     15:54         249573 MorladeLaValderia_hidroyear_2018-2019.txt
-a----        14/01/2023     15:54         250260 Valladolid-Esgueva_hidroyear_2020-2021.txt
-a----        14/01/2023     15:54         243172 Zamora_hidroyear_2019-2020.txt


PS H:\Repositories\saih-duero-scraping\data>
```

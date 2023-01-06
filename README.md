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

- Source code: [example.py]()

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
            gauging_code = GaugingCollection[GaugingStation.MorlaDeLaValderia].gauging_code, 
            hydrologic_year = HydrologicYears.year_2019
        ),
        dict(
            gauging_code = GaugingCollection[GaugingStation.MorlaDeLaValderia].gauging_code, 
            hydrologic_year = HydrologicYears.year_2020
        ),
        dict(
            gauging_code = GaugingCollection[GaugingStation.MorlaDeLaValderia].gauging_code, 
            hydrologic_year = HydrologicYears.year_2021
        )
    ]
)

# Finally to call the method to download the data sets.
datadownloader.download_data()
```

- Ouput:

```
#TODO
```
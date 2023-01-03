from core.gauging_collection import GaugingCollection
from core.gauging_enum import GaugingEnum
from core.hydrologic_years import HydrologicYears
from core.data_downloader import DataDownloader

datadownloader = DataDownloader()

datadownloader.add_url(
    GaugingCollection[GaugingEnum.Leon].gauging_code, 
    HydrologicYears.year_2018
)

datadownloader.add_urls(
    [
    dict(
        gauging_code = GaugingCollection[GaugingEnum.Leon].gauging_code, 
        hydrologic_year = HydrologicYears.year_2019
    ),
    dict(
        gauging_code = GaugingCollection[GaugingEnum.MoralesDelRey].gauging_code, 
        hydrologic_year = HydrologicYears.year_2020
    ),
    dict(
        gauging_code = GaugingCollection[GaugingEnum.LasOmanias].gauging_code, 
        hydrologic_year = HydrologicYears.year_2018
    )])

datadownloader.download_data()

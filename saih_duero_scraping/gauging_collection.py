from saih_duero_scraping.gauging_enum import GaugingStation
from saih_duero_scraping.gauging import Gauging

GaugingCollection = {
    GaugingStation.MorlaDeLaValderia : Gauging(
        name='Morla De La Valdería',
        gauging_code=2089
    ),
    GaugingStation.MoralesDelRey : Gauging(
        name='Morales Del Rey',
        gauging_code=2082
    ),
    GaugingStation.Leon : Gauging(
        name='León',
        gauging_code=2115
    ),
    GaugingStation.LasOmanas : Gauging(
        name='Las Omañanas',
        gauging_code=2076
    )
}
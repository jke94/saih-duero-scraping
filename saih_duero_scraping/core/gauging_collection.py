from core.gauging_enum import GaugingEnum
from core.gauging import Gauging

GaugingCollection = {
    GaugingEnum.MorlaDeLaValderia : Gauging(
        name='Morla De La Valdería',
        gauging_code=2089
    ),
    GaugingEnum.MoralesDelRey : Gauging(
        name='Morales Del Rey',
        gauging_code=2082
    ),
    GaugingEnum.Leon : Gauging(
        name='León',
        gauging_code=2115
    ),
    GaugingEnum.LasOmanias : Gauging(
        name='Las Omañanas',
        gauging_code=2076
    )
}
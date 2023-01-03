class HydrologicUrl:
    
    def __init__(self, place_code:int, hydrologic_year:int)-> None:
        self.place_code = place_code
        self.hydrologic_year = hydrologic_year
        
        self._url = f"https://www.saihduero.es/historico-risr-csv?f={place_code}_AH{hydrologic_year}_HQ.csv"
        
    def get_url(self) -> str:
        return self._url
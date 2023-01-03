class HydrologicUrl:
    
    def __init__(self, place_code, hydrologic_year):
        self.place_code = place_code
        self.hydrologic_year = hydrologic_year
        
        self._url = f"https://www.saihduero.es/historico-risr-csv?f={place_code}_AH{hydrologic_year}_HQ.csv"
        
    def get_url(self):
        return self._url
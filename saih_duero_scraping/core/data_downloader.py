import requests
import csv
import os

from core.hydrologic_url import HydrologicUrl as HydrologicUrl
from core.gauging_collection import GaugingCollection

class DataDownloader():
    
    def __init__(self) -> None:
        self.hydrologic_urls = []
                    
    def add_url(self, gauging_code:int, hydrologic_year:str)-> None:
        
        hydrologic_url = HydrologicUrl(
            gauging_code, 
            hydrologic_year)       
        
        if self._is_valid_url(hydrologic_url.get_url()):
            
            self.hydrologic_urls.append(hydrologic_url)
    
    def add_urls(self, dict_hydrologic_years:dict)-> None:
        
        for item in dict_hydrologic_years:
            
            hydrologic_url = HydrologicUrl(
                item["gauging_code"], 
                item["hydrologic_year"])
                    
            if self._is_valid_url(hydrologic_url.get_url()):
                
                self.hydrologic_urls.append(hydrologic_url)
    
    def _is_valid_url(self, url:str)-> bool:
        
        # TODO: Improve URL validation.
        if type(url) is str:
            
            return True
        else:
            return False
    

    def download_data(self)-> None:
        
        if not os.path.exists('./data/csv'):
            os.makedirs('./data/csv')
        
        if not os.path.exists('./data/txt'):
            os.makedirs('./data/txt')
        
        count = 0
        
        for url in self.hydrologic_urls:
            
            count += count + 1
            name = self.__find_gauging_by_gauging_code(url.place_code).replace(' ','')
            
            response = requests.get(url.get_url())

            if response.status_code == 200:
                
                reader = csv.reader(response.text.split('\n'), delimiter=';')
                
                txt_file = f'./data/txt/{name}_hidroyear{url.hydrologic_year}-{url.hydrologic_year+1}.txt'
                
                with open(txt_file, mode='w') as file:
                    file.write(response.text)
                    
                file.close()
                
            csv_file = f'./data/csv/{name}_hidro_year{url.hydrologic_year}-{url.hydrologic_year+1}.csv'
            
            with open(csv_file, mode='w') as file:
                
                writer = csv.writer(file)
                
                for row in reader:
                    
                    if len(row) == 3 and 'AAAA-MM-DD HH:mm' not in row[0]:
                        
                        writer.writerow(row)

            file.close()

    def __find_gauging_by_gauging_code(self, gauging_code:int)-> str:
                    
        for key, value in GaugingCollection.items():
            
            if value.gauging_code == gauging_code:
                
                return value.name
        
        return str('')
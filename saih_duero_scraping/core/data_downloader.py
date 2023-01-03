import requests
import csv
import os

from core.hydrologic_url import HydrologicUrl as HydrologicUrl

class DataDownloader():
    
    def __init__(self) -> None:
        self.urls = []
                    
    def add_url(self, gauging_code, hydrologic_year):
        
        hydrologic_url = HydrologicUrl(
            gauging_code, 
            hydrologic_year)
        
        url = hydrologic_url.get_url()
        
        if self._is_valid_url(url):
            
            self.urls.append(url)
    
    def add_urls(self, dict_hydrologic_years):
        
        for item in dict_hydrologic_years:
            
            hydrologic_url = HydrologicUrl(
                item["gauging_code"], 
                item["hydrologic_year"])
        
            url = hydrologic_url.get_url()
            
            if self._is_valid_url(url):
                
                self.urls.append(url)
    
    def _is_valid_url(self, url):
        
        # TODO: Validate URL.
        return True
    

    def download_data(self):
        
        if not os.path.exists('./data/csv'):
            os.makedirs('./data/csv')
        
        if not os.path.exists('./data/txt'):
            os.makedirs('./data/txt')
        
        count = 0
        
        for url in self.urls:
            
            count += count + 1
            
            response = requests.get(url)

            if response.status_code == 200:
                reader = csv.reader(response.text.split('\n'), delimiter=';')
                
                with open(f'./data/txt/{count}.txt', mode='w') as file:
                    file.write(response.text)
                    
                file.close()
                
            with open(f'./data/csv/{count}.csv', mode='w') as file:
                
                writer = csv.writer(file)
                
                for row in reader:
                    
                    if len(row) == 3 and 'AAAA-MM-DD HH:mm' not in row[0]:
                        
                        writer.writerow(row)

            file.close()
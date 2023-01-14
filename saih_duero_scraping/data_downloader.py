import requests
import csv
import os

from saih_duero_scraping.hydrologic_url import HydrologicUrl as HydrologicUrl
from saih_duero_scraping.gauging_collection import GaugingCollection
from saih_duero_scraping.summary_info_file import SummaryInfoFile

class DataDownloader():
    
    def __init__(self) -> None:
        
        self.hydrologic_urls = []
        
        self.__csv_data_folder = './data/csv'
        self.__txt_data_folder = './data/txt'
        self.__data_folder = './data'
        self.__summary_info = SummaryInfoFile(
            summary_info_file_name='./data/summary.txt')
                    
    def add_url(self, gauging_code:int, hydrologic_year:str) -> None:
        
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
    
    def download_data(self)-> int:
        
        self.__create_data_downlods_folders()
        
        count = 0
        
        for url in self.hydrologic_urls:
            
            count += 1
            name = self.__find_gauging_by_gauging_code(url.place_code).replace(' ','')
            
            response = requests.get(url.get_url())

            # Http request 200 - OK and gauging code exits.
            
            if response.status_code == 200 and name != '':
                
                reader = csv.reader(response.text.split('\n'), delimiter=';')
                
                txt_file_name = f'./data/txt/{name}_hidroyear_{url.hydrologic_year}-{url.hydrologic_year+1}.txt'
                
                with open(txt_file_name, mode='w') as txt_file:
                    
                    txt_file.write(response.text)
                    
                txt_file.close()
                
                csv_file_name = f'./data/csv/{name}_hidroyear_{url.hydrologic_year}-{url.hydrologic_year+1}.csv'
                
                with open(csv_file_name, mode='w') as csv_file:
                    
                    writer = csv.writer(csv_file)
                    
                    writer.writerow(['AAAA-MM-DD HH:mm','H(m)','Q(m3/s)'])
                    
                    for row in reader:
                        
                        if len(row) == 3 and 'AAAA-MM-DD HH:mm' not in row[0]:
                            
                            writer.writerow(row)

                csv_file.close()
                
                # Add summary info.
                self.__summary_info.append_summary_info(
                    n_item=count,
                    n_total_items=len(self.hydrologic_urls),
                    csv_file_name=csv_file_name,
                    txt_file_name=txt_file_name)
                
        self.__create_summary_downloads_info_file()
            
        return 0

    def __find_gauging_by_gauging_code(self, gauging_code:int) -> str:
                    
        for key, value in GaugingCollection.items():
            
            if value.gauging_code == gauging_code:
                
                return value.name
        
        return ''
    
    def __create_data_downlods_folders(self) -> None:
        
        if not os.path.exists(self.__csv_data_folder):
            os.makedirs(self.__csv_data_folder)
        
        if not os.path.exists(self.__txt_data_folder):
            os.makedirs(self.__txt_data_folder)
            
    def __create_summary_downloads_info_file(self) -> None:
        
        if not os.path.exists(self.__data_folder):
            os.makedirs(self.__data_folder)

        self.__summary_info.create_summary_info_file()
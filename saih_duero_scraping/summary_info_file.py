import time

class SummaryInfoFile():

    def __init__(self, summary_info_file_name) -> None:
        self.__summary_info = []
        self.__summary_info_file_name = summary_info_file_name

    @property
    def summary_info_file_name(self):
        return self.__summary_info_file_name

    def append_summary_info(self, n_item, n_total_items, txt_file_name, csv_file_name) -> None:

        self.__summary_info.append(f'ITEM [{n_item}/{n_total_items}]\n')
        self.__summary_info.append(
            f'{time.strftime("%d-%m-%Y %H:%M:%S")}\t|\tFile created: {txt_file_name}\n')
        
        self.__summary_info.append(
            f'{time.strftime("%d-%m-%Y %H:%M:%S")}\t|\tFile created: {csv_file_name}\n')
        
        self.__summary_info.append('\n\n')

    def create_summary_info_file(self):

        with open(self.__summary_info_file_name, mode='w') as file:
            
            file.writelines(self.__summary_info)
        
        file.close()
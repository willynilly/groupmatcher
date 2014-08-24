import os.path
from csv_preference_loader import CsvPreferenceLoader
from json_preference_loader import JsonPreferenceLoader

class PreferenceLoader:    
    def load(self, input_filename=None):
        try:
            file_name, file_ext = os.path.splitext(input_filename)
        except Exception as e:
            file_ext = None
        if file_ext == '.csv':
            return CsvPreferenceLoader().load(input_filename)
        elif file_ext == '.json':
            return JsonPreferenceLoader().load(input_filename)
        else:
            raise Exception('Invalid file extension. The input file must be a .csv or .json file.')

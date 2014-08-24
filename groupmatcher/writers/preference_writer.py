import os.path 
from csv_preference_writer import CsvPreferenceWriter
from json_preference_writer import JsonPreferenceWriter

class PreferenceWriter:
    def write(self, model_manager, output_filename=None):
        if not output_filename:
            raise Exception('Invalid output file.  The output file must be a .csv or .json file.')
        else:
            try:
                file_name, file_ext = os.path.splitext(output_filename)
            except Exception as e:
                file_ext = None
            if file_ext == '.csv':
                CsvPreferenceWriter().write(model_manager, output_filename)
            elif file_ext == '.json':
                JsonPreferenceWriter().write(model_manager, output_filename)
            else:
                raise Exception('Invalid file extension. The output file must be a .csv or .json file.')

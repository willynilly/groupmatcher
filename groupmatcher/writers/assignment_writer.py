import os.path 
from screen_assignment_writer import ScreenAssignmentWriter
from csv_assignment_writer import CsvAssignmentWriter
from json_assignment_writer import JsonAssignmentWriter

class AssignmentWriter:
    def write(self, model_manager, output_filename=None):
        if not output_filename:
            ScreenAssignmentWriter().write(model_manager)
        else:
            try:
                file_name, file_ext = os.path.splitext(output_filename)
            except Exception as e:
                file_ext = None
            if file_ext == '.csv':
                CsvAssignmentWriter().write(model_manager, output_filename)
            elif file_ext == '.json':
                JsonAssignmentWriter().write(model_manager, output_filename)
            else:
                raise Exception('Invalid file extension. The output file must be a .csv or .json file.')

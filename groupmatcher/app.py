from groupmatcher.loaders.preference_loader import PreferenceLoader
from groupmatcher.matchers.max_munkres_matcher import MaxMunkresMatcher
from groupmatcher.writers.assignment_writer import AssignmentWriter
from groupmatcher.writers.preference_writer import PreferenceWriter


class App:
    def __init__(self, input_filename, output_filename, convert_pref_file=False):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.convert_pref_file = convert_pref_file
    
    def run(self):
        try:
            model_manager = PreferenceLoader().load(self.input_filename)
            
            if not self.convert_pref_file:
                model_manager.assignments = MaxMunkresMatcher().match(model_manager)
                AssignmentWriter().write(model_manager, self.output_filename)
            else:
                PreferenceWriter().write(model_manager, self.output_filename)
                
        except Exception as e:
            print e
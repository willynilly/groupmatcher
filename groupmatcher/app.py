from groupmatcher.loaders.preference_loader import PreferenceLoader
from groupmatcher.matchers.max_munkres_matcher import MaxMunkresMatcher
from groupmatcher.writers.assignment_writer import AssignmentWriter

class App:
    def __init__(self, input_filename, output_filename):
        self.input_filename = input_filename
        self.output_filename = output_filename
    
    def run(self):
        try:
            model_manager = PreferenceLoader().load(self.input_filename)
            model_manager.assignments = MaxMunkresMatcher().match(model_manager)
            AssignmentWriter().write(model_manager, self.output_filename)
        except Exception as e:
            print e
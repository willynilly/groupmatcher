import json
from groupmatcher.analyzers.assignment_stats import AssignmentStats

class JsonAssignmentWriter:
    def write(self, model_manager, output_filename=None):
        if output_filename:
            json_string = self.get_assignment_string(model_manager, output_filename)
            with open (output_filename, "w") as json_file:
                json_file.write(json_string)
        else:
            raise Exception('Invalid output file name for .json file.')
    
    def get_assignment_string(self, model_manager, output_filename=None):
        j = {}
        j_a = {}
        for (individual, group) in model_manager.assignments:
            j_a[str(individual.id)] = group.id
        j['assignments'] = j_a
        
        j['stats'] = AssignmentStats().compute(model_manager)
        
        return json.dumps(j, sort_keys=True, separators=(',',':'), indent=4)
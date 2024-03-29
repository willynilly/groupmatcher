import json
from groupmatcher.models.model_manager import ModelManager
from groupmatcher.models.individual import Individual
from groupmatcher.models.group import Group

class JsonPreferenceLoader:
    def load(self, json_file_name = 'prefs.json'):
        with open (json_file_name, "r") as json_file:
            json_string = json_file.read()        
        return self.load_from_string(json_string)
        
    def load_from_string(self, json_string):
        model_manager = ModelManager()
        groups = {}
        individuals = {}
        j = json.loads(json_string)
        if j:        
            # load groups
            if 'groups' in j:
                if len(j['groups']):
                    for group_id, g_v in j['groups'].iteritems():
                        group = Group(str(group_id))
                        group.max_size = g_v['max']
                        groups[str(group_id)] = group
                else:
                    raise Exception("Invalid JSON string for preference input. Must have at least one group defined in 'groups' dictionary.")         
            else:
                raise Exception("Invalid JSON string for preference input. Must have 'groups' dictionary.")
            
            # load individuals
            if 'individuals' in j:
                if len(j['individuals']):
                    for individual_id, i_v in j['individuals'].iteritems():
                        individual = Individual(str(individual_id))
                        for group_id, group_pref_value in i_v['prefs'].iteritems():
                            individual.set_group_pref_value(str(group_id), float(group_pref_value))
                        individuals[str(individual_id)] = individual
                else:
                    raise Exception("Invalid JSON string for preference input. Must have at least one group defined in 'individuals' dictionary.")         
            else:
                raise Exception("Invalid JSON string for preference input. Must have 'individuals' dictionary.")
        
        model_manager.individuals = individuals
        model_manager.groups = groups     
        return model_manager
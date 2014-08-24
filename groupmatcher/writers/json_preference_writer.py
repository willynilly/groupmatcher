import json

class JsonPreferenceWriter:
    def write(self, model_manager, output_filename=None):
        if output_filename:
            json_string = self.get_pref_string(model_manager, output_filename)
            with open (output_filename, "w") as json_file:
                json_file.write(json_string)
        else:
            raise Exception('Invalid output file name for .json file.')
            
    def get_pref_string(self, model_manager, output_filename=None):
        j = {}
        j['individuals'] = {}
        for ind_id, ind in model_manager.individuals.iteritems():
            prefs = {}
            for group_id, group in model_manager.groups.iteritems():
                prefs[str(group_id)] = ind.get_group_pref_value(group_id)
            ind_j = {'prefs': prefs}
            j['individuals'][str(ind_id)] = ind_j 
        return json.dumps(j, sort_keys=True, separators=(',',':'))
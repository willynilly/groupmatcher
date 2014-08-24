import csv
from groupmatcher.models.model_manager import ModelManager
from groupmatcher.models.individual import Individual
from groupmatcher.models.group import Group

class CsvPreferenceLoader:
    def load(self, csv_filename = 'prefs.csv'):
      with open(csv_filename, 'rb') as f:
          reader = csv.DictReader(f)
          model_manager = ModelManager()
          model_manager.groups = self._get_groups_from_csv_dict_reader(reader)
          model_manager.individuals = self._get_individuals_from_csv_dict_reader(reader)          
          return model_manager
    
    def _get_field_names_from_csv_dict_reader(self, reader):
        field_names = [fname.lower().strip() for fname in reader.fieldnames]
        if 'individual_id' not in field_names:
            raise Exception('Invalid CSV preference file. Missing column header: individual_id')
        if len(field_names) < 2:
            raise Exception('Invalid CSV preference file. Must have at least one group column header.')
        return field_names
        
    def _get_group_field_names_from_csv_dict_reader(self, reader):
        group_field_names = self._get_field_names_from_csv_dict_reader(reader)
        group_field_names.remove('individual_id')
        return group_field_names
    
    def _get_groups_from_csv_dict_reader(self, reader):
        group_field_names = self._get_group_field_names_from_csv_dict_reader(reader)
        groups = {}
        for group_field_name in group_field_names:
            (group_id, group_max_size) = self._parse_csv_group_field_name(group_field_name)
            g_k = str(group_id)
            if g_k in groups:
                raise Exception('Invalid CSV preference file. Duplicate group_id (' + g_k  + ') in column header: ' + group_field_name)
            else:
                groups[g_k] = Group(group_id, group_max_size)
        return groups
    
    def _parse_csv_group_field_name(self, field_name):
        parts = field_name.split('_')
        if len(parts) != 4:
            raise Exception('Invalid CSV preference file. Invalid group field name: ' + str(field_name))
        group_id = str(parts[1])
        max_group_size = int(parts[3])
        return (group_id, max_group_size)
    
    def _get_individuals_from_csv_dict_reader(self, reader):
        individuals = {}
        row_num = 0
        for row in reader:
            row_num += 1
            # lowercase and strip column names
            row = dict((k.lower().strip(), v) for k,v in row.iteritems())
            field_names = self._get_field_names_from_csv_dict_reader(reader)
            individual_id = str(row['individual_id'])
            if individual_id is None:
                raise Exception('Invalid CSV preference file. On row number ' + str(row_num) + ', missing individual_id')
            elif individual_id in individuals:
                raise Exception('Invalid CSV preference file. On row number ' + str(row_num) + ', duplicate individual_id: ' + individual_id)

            i_k = str(individual_id)
            individual = Individual(individual_id)                        
            for field_name in field_names:
                if field_name != 'individual_id':
                    (group_id, group_max_size) = self._parse_csv_group_field_name(field_name)
                    group_pref_value = float(row[field_name])
                    individual.set_group_pref_value(str(group_id), float(group_pref_value))            
            individuals[str(individual.id)] = individual
        return individuals
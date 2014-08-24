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
            groups[str(group_id)] = Group(group_id, group_max_size)
        return groups
    
    def _parse_csv_group_field_name(self, field_name):
        parts = field_name.split('_')
        if len(parts) != 4:
            raise Exception('Invalid group field name in CSV file: ' + str(field_name))
        group_id = str(parts[1])
        max_group_size = int(parts[3])
        return (group_id, max_group_size)
    
    def _get_individuals_from_csv_dict_reader(self, reader):
        individuals = {}
        for row in reader:
            # lowercase and strip column names
            row = dict((k.lower().strip(), v) for k,v in row.iteritems())
            field_names = self._get_field_names_from_csv_dict_reader(reader)
            if 'individual_id' in field_names:
                individual_id = str(row['individual_id'])
                if individual_id is None:
                    raise Exception('Missing individual id in CSV file: ' + str(row))
            else:
                 raise Exception('Missing individual_id column header.')

            individual = Individual(individual_id)                        
            for field_name in field_names:
                if field_name != 'individual_id':
                    (group_id, group_max_size) = self._parse_csv_group_field_name(field_name)
                    group_pref_value = float(row[field_name])
                    individual.set_group_pref_value(str(group_id), float(group_pref_value))            
            individuals[str(individual.id)] = individual
        return individuals
import csv

class CsvPreferenceWriter:
    def write(self, model_manager, output_filename=None):
        group_field_names = [self._create_group_field_name(model_manager.groups[group_id]) for group_id in sorted(model_manager.groups.iterkeys())]
        field_names = ['individual_id'] + group_field_names
                    
        with open(output_filename, 'wb') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            writer.writeheader()
            for individual_id in sorted(model_manager.individuals.iterkeys()):
                individual = model_manager.individuals[individual_id]
                row = {}
                row['individual_id'] = individual.id
                for group_id in sorted(model_manager.groups.iterkeys()):
                    group = model_manager.groups[group_id]
                    row[self._create_group_field_name(group)] = individual.get_group_pref_value(group_id)
                writer.writerow(row)
                
    def _create_group_field_name(self, group):
        field_name = '_'.join(['group', str(group.id), 'max', str(group.max_size)]) 
        return field_name
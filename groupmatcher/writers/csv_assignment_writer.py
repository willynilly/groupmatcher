import csv

class CsvAssignmentWriter:
    def write(self, model_manager, output_filename=None):
        field_names = ['individual_id', 'group_id', 'group_pref_value']
        with open(output_filename, 'wb') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            writer.writeheader()
            for (individual, group) in model_manager.assignments:
                row = {}
                row['individual_id'] = individual.id
                row['group_id'] = group.id
                row['group_pref_value'] = individual.get_group_pref_value(group.id)
                writer.writerow(row)
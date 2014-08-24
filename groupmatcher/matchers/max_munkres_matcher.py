from munkres import Munkres

class MaxMunkresMatcher:
    def __init__(self):
        pass
        
    def match(self, model_manager):
        individuals = model_manager.individuals
        groups = model_manager.groups
        pref_matrix = []
        individual_count = len(individuals)        
        row_index = -1
        individuals_by_row = {}
        groups_by_col = {}
        for individual_id, individual in individuals.iteritems():
            row_index += 1
            individuals_by_row[str(row_index)] = individual
            pref_matrix_row = []
            col_index = -1
            for group_id, group in groups.iteritems():
                group_pref_value = individual.get_group_pref_value(group.id)
                # we use group slots to control the max number of individuals per group.  one individual per slot
                # each slot represents a potential membership within a group within the preference matrix. 
                # the len(pref_matrix_group_slots[grounp.id]) == min(group.max_size, len(individuals))
                group_slot_size = min(group.max_size, individual_count)
                for s in range(group_slot_size):
                    # multiply value by negative 1 because munkres finds
                    # the assignment with minimum net value, 
                    # and we want to find the assignment with
                    # maximum net value
                    pref_matrix_row.append(group_pref_value * -1)
                    col_index += 1
                    groups_by_col[str(col_index)] = group      
            pref_matrix.append(pref_matrix_row)  
        
        munkres = Munkres()
        optimal_match_indexes = munkres.compute(pref_matrix)
        assignments = [(individuals_by_row[str(row)], groups_by_col[str(col)]) for row, col in optimal_match_indexes]            
        return assignments
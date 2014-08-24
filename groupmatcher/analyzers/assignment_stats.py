import numpy

class AssignmentStats:
    def compute(self, model_manager):
        individuals = model_manager.individuals
        groups = model_manager.groups
        assignments = model_manager.assignments
        
        stats = {}
        stats['assigned_individual_count'] = len(set([ind.id for (ind, group) in assignments]))
        stats['total_individual_count'] = len(individuals)
        stats['percentage_individual_assigned'] =  float(stats['assigned_individual_count']) / stats['total_individual_count'] * 100
        stats['assigned_group_count'] = len(set([group.id for (ind, group) in assignments]))
        stats['total_group_count'] = len(groups)
        stats['percentage_group_assigned'] = float(stats['assigned_group_count']) / stats['total_group_count'] * 100
        
        assignment_values = [individual.get_group_pref_value(group.id) for (individual, group) in assignments]
        stats['total_assignment_value'] = numpy.sum(assignment_values)
        stats['mean_assignment_value'] = numpy.mean(assignment_values)
        stats['median_assignment_value'] = numpy.median(assignment_values)
        stats['min_assignment_value'] = numpy.min(assignment_values)
        stats['max_assignment_value'] = numpy.max(assignment_values)
        stats['std_dev_assignment_value'] = numpy.max(assignment_values)
        
        return stats
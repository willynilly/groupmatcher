from groupmatcher.analyzers.assignment_stats import AssignmentStats

class ScreenAssignmentWriter:
    def write(self, model_manager):
        stats = AssignmentStats().compute(model_manager)
        print 
        print "GroupMatcher"
        print "By: Will Riley"
        print 
        print "Individuals"
        print " Assigned Count: " + str(stats['assigned_individual_count'])
        print " Total Count: " + str(stats['total_individual_count'])
        print " Percentage Assigned: " + str(stats['percentage_individual_assigned'])
        print
        print "Groups"
        print " Assigned Count: " + str(stats['assigned_group_count'])
        print " Total Count: " + str(stats['total_group_count'])
        print " Percentage Assigned: " + str(stats['percentage_group_assigned'])        
        print
        print "Assignments:"
        print " Individual Id -> Group Id"
        assignment_values = []
        for (individual, group) in model_manager.assignments:
            assignment_value = individual.get_group_pref_value(group.id)
            print " " + str(individual.id) + ' -> ' + str(group.id) + "\t\t\t\t (value: "  + str(assignment_value) + ')' 
        print
        print "Total of Assignment Values: " + str(stats['total_assignment_value'])
        print "Mean of Assignment Values: " + str(stats['mean_assignment_value'])
        print "Median of Assignment Values: " + str(stats['median_assignment_value'])
        print "Min Assignment Value: " + str(stats['min_assignment_value'])
        print "Max Assignment Value: " + str(stats['max_assignment_value'])
        print "Std. Dev. of Assignment Values: " + str(stats['std_dev_assignment_value'])
        print
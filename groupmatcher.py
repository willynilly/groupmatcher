# GroupMatcher
# By: Will Riley

# Description: The program matches groups to projects based on group preferences for various projects.
# Each group ranks N projects, where 
# 1 = Most Preferred Project and {N} = Least Preferred Project
# It does not allow two projects to have the same ranking.

# The matching occurs in rounds.
# In the first round, it finds every group that has picked a project as its first pick (ranking = 1).
# It then randomly selects one of these groups and assigns that project to them.
# In the next round, it finds every group that has picked a project as their second pick (ranking = 2).
# Again, it randomly selects one of these groups and  assigns the project to them.
# This process is repeated until all of the groups have been assigned a project, or until there are no more projects left.

# I have enclosed a sample CSV file.  You can edit the file.
# The file contains the following columns:
# group_id, proj_1_rank, proj_2_rank, proj_4_rank, ... , proj_{N}_rank

# To run the progrom, type:
# python groupmatcher.py

# Look at the last output to see the final project assignments for the various groups.

import csv
import random

def main():
  groups = getGroupsFromCSV()
  groupProjectMatcher = GroupProjectMatcher()
  groups = groupProjectMatcher.match(groups)
  print ""
  print "Final Project Assignments For Groups:"
  for group in groups:
    print 'Group ' + str(group.groupId) + ' has Project ' + str(group.projectId)
  
  pass

def getGroupsFromCSV(csvFileName = 'group_project_prefs.csv'):
  groups = []
  with open(csvFileName, 'rb') as f:
      reader = csv.DictReader(f)
      numProjects = len(reader.fieldnames) - 1
      for row in reader:
          groupId = int(row['group_id'])
          rankings = []
          for i in range(1, numProjects + 1):
            rankings.append(int(row['proj_' + str(i) + '_rank']))
          group = Group(groupId, rankings)
          groups.append(group)
  return groups
  
class Group:
  def __init__(self, groupId, projRankings):
      self.groupId = groupId
      self.projRankings = projRankings
      self.projectId = None

class GroupProjectMatcher:
  def match(self, groups):
    numProjects = len(groups[0].projRankings)
    projectIdsToMatch = range(1, numProjects + 1)
    print projectIdsToMatch
    groupsToMatch = groups[:]

    print "Number of Projects: " + str(numProjects)
    print "Number of Groups: " + str(len(groups))
    
    bestRank = 0
    while len(groupsToMatch) > 0 and len(projectIdsToMatch) > 0:
      bestRank += 1
      print ""
      print "Round # " + str(bestRank)

      matchedProjectIds = []
      for projectIdToMatch in projectIdsToMatch:
        print ""
        print "Matching Project " + str(projectIdToMatch)
        bestGroups = []
        for groupToMatch in groupsToMatch:
          groupRank = groupToMatch.projRankings[projectIdToMatch-1]
          print 'Group: ' + str(groupToMatch.groupId) + ' Ranking:' + str(groupRank)
          if groupRank == bestRank:
            bestGroups.append(groupToMatch)
        if len(bestGroups) > 0:
            bestGroupIds = []
            for bestGroup in bestGroups:
              bestGroupIds.append(str(bestGroup.groupId))
            print "Best Groups " + ', '.join(bestGroupIds)
            bestGroup = random.choice(bestGroups)
            bestGroup.projectId = projectIdToMatch
            groupsToMatch.remove(bestGroup)
            matchedProjectIds.append(projectIdToMatch)
            print "Project " + str(projectIdToMatch) + " Matched With Group " + str(bestGroup.groupId)
      for matchedProjectId in matchedProjectIds:
        projectIdsToMatch.remove(matchedProjectId)

    return groups
       
          
if __name__ == "__main__":
  main()
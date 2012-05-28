groupmatcher
============
The program matches groups to projects based on group preferences for various projects.
Each group ranks N projects, where 
1 = Most Preferred Project and {N} = Least Preferred Project
It does not allow two projects to have the same ranking.

The matching occurs in rounds.
In the first round, it finds every group that has picked a project as its first pick (ranking = 1).
It then randomly selects one of these groups and assigns that project to them.
In the next round, it finds every group that has picked a project as their second pick (ranking = 2).
Again, it randomly selects one of these groups and assigns the project to them.
This process is repeated until all of the groups have been assigned a project, or until there are no more projects left.

I have enclosed a sample CSV file.  You can edit the file.
The file contains the following columns:
group_id, proj_1_rank, proj_2_rank, proj_4_rank, ... , proj_{N}_rank

To run the progrom, type:
python groupmatcher.py

Look at the last output to see the final project assignments for the various groups.
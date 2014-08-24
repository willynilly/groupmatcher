groupmatcher
============
The program matches individuals to groups based on individual preferences for various groups.
Each group g can have a different number of individuals, where the maximum capacity is max_capacity(g).

In the preferences definition, each individual indicates the utility u(i, g) they would get from belonging to that group.
A higher number indicates the individual would receive more utility or benefit for belonging to that group.
Negative utilities are allowed.   
If no preference is specified, the system assumes that the utility is zero.

An individual can only belong to one group.
The matching algorithm takes O(sum_of_max_capacities_across_all_groups^3) time.

I have enclosed two sample preference files, a CSV file and a JSON file.  You can edit a file.

The CSV file must contain the following columns:
individual_id, group_1_max_4, group_2_max_1, group_3_max_2, ... , group_{group id}_max_{max size of group}

The JSON file must contain the following structure:

{
  "groups": {
    "group1": {"max":2},
    "group2": {"max":4},
    "group3": {"max":1},
  },
  "individuals": {
    "bob": {"prefs":{
      "group1":4,
      "group2":2.2,
      "group3":0
    }},
    "sam": {"prefs":{
      "group1":4,
      "group2":2.2,
      "group3":-6
    }}, 
    "lisa": {"prefs":{
      "group1":4,
      "group2":0,
      "group3":4
    }}
  }
}

For groups, the syntax is:
group_id: {"max":max_size_of_group}

For individuals, the syntax is:
individual_id:{"pref":{group_id:utility_of_group}}

To run the progrom, execute the following from the terminal:
python groupmatcher.py {preference_inputfile} {assignment_outputfile}


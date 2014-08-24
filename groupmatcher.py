"""

GroupMatcher
By:Will Riley

Description:
    Optimally assigns individuals to groups based on their 
    individual preferences for (or the utility they would gain from) 
    belonging to each group.  Each group can have a maximum size,
    but no minimum size.  Each individual is only assigned to one group.
    The assignment maximizes the overall utility across all individuals.  
    It uses a modification of the Munkres algorithm. 

Usage:
  groupmatcher.py <input_pref_filename> [<output_assignment_filename>]
  groupmatcher.py (-c | --convert) <input_pref_filename> <output_pref_filename>
  groupmatcher.py --help
  
Parameters
  All files must be either a .json or .csv file.
  
  <input_pref_filename> - a .json or .csv file containing individual 
  preferences of groups
  
  <output_assignment_filename> - a .json or .csv file containing optimal 
  assignments of individuals to groups.  If not specified, it will
  output the assignments to the screen or standard output.
  
  <output_pref_filename> - a .json or .csv file containing individual
  preferences of groups

Examples:
  groupmatcher.py prefs.csv
  groupmatcher.py prefs.json
  groupmatcher.py prefs.csv assignments.csv
  groupmatcher.py prefs.csv assignments.json
  groupmatcher.py prefs.json assignments.json
  groupmatcher.py prefs.json assignments.csv
  
  groupmatcher --convert prefs.csv prefs.json
  groupmatcher --convert prefs.json prefs.csv
  
  groupmatcher -h
  groupmatcher --help


Options:
  -h, --help
  -c, --convert  Convert a preference file from a .json preference file 
                 to a .csv prefernce file, or from a csv file 
                 to a .json preference file.

"""
from docopt import docopt
from groupmatcher.app import App

def main(arguments):
    # files must be .json or .csv 
    # if output file is empty it will print to screen
    convert_pref_file = arguments['--convert']
    input_filename = arguments['<input_pref_filename>']
    output_filename = arguments['<output_assignment_filename>'] or arguments['<output_pref_filename>']
    
    # create and run app
    app = App(input_filename, output_filename, convert_pref_file)
    app.run()
    
if __name__ == "__main__":
    arguments = docopt(__doc__, version="GroupMatcher 1.0", help=True)
    main(arguments)
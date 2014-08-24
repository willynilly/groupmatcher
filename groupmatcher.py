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
  groupmatcher.py <input_filename> [<output_filename>]
  groupmatcher.py --help
  
Parameters
  <input_filename> - a .json or .cvs file containing individual 
  preferences of groups
  <output_filename> - a .json or .cvs file containing optimal 
  assignments of individuals to groups.  If not specified, it will
  output the assignments to the screen or standard output.

Examples:
  groupmatcher.py prefs.csv
  groupmatcher.py prefs.json
  groupmatcher.py prefs.csv output.csv
  groupmatcher.py prefs.csv output.json
  groupmatcher.py prefs.json output.json
  groupmatcher.py prefs.json output.csv

Options:
  -h, --help

"""
from docopt import docopt
from groupmatcher.app import App

def main(arguments):
    # files must be .json or .csv 
    # if output file is empty it will print to screen
    input_filename = arguments['<input_filename>']
    output_filename = arguments['<output_filename>'] 
    
    # create and run app
    app = App(input_filename, output_filename)
    app.run()
    
if __name__ == "__main__":
    arguments = docopt(__doc__, version="GroupMatcher 1.0", help=True)
    main(arguments)

"""Virtual Host App

Creates the hosts file and vhost files 
Usage: python VHostApp.py [project domain]

Options:
  -p ..., --project=...   use specified project/domainS
  -h, --help              show this help
  -d                      show debugging information while parsing


"""

__author__ = "David Duggins (david@duggins.net"
__version__ = "$Revision: 0.2 $"
__date__ = "$Date: 2012/09/22 21:57:19 $"
__copyright__ = "Copyright (c) 2012 David Duggins"
__license__ = "GPL3"


import sys
import getopt



class VHostApp():
    """This is the main class file for the VHost App"""
    def __init__(self, project):
        self.project = project
        # here we handle the command line input and test it for validity,
        # if there is an issue, we end the program and spit out errors.
    def print_name(self):
        print f"""
        <VirtualHost *:80>
            ServerAlias {self.project}
            DocumentRoot /var/www/html/{self.project}
            ErrorLog logs/{self.project}-error_log
            CustomLog logs/{self-project}-access_log combined
        </VirtualHost>"""
def usage():
        print __doc__
        
def main(argv):
    
    try:
        opts, args = getopt.getopt(argv, "hp:", ["help", "project="])
    except getopt.GetoptError:           
        usage()                          
        sys.exit(2)  
    for opt, arg in opts:                
        if opt in ("-h", "--help"):      
            usage()                     
            sys.exit()                                
        elif opt in ("-p", "--project"): 
            project = arg
    
    me = VHostApp(project)
    me.print_name()
    
    

main(sys.argv[1:])

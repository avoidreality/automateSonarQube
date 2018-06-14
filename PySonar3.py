#! /usr/bin/env python

import os
import subprocess
import time 
import getopt
import sys
import time 

#from ClearCaseDownload import getCode  #importing this is not important now since the view does not need to be set 


'''

  This code will download code from a view and a folder and change its permissions from root to the sonar user


'''



def startScan(scanFile="/v01/scans/sonar-project-dph-r2.properties"):

    """This function starts a SonarQube scan """
    start = time.time() 

    x = time.asctime()
    z = 'sonar_'
    y = x.replace(" ", "_").replace(":", "_")
    log_name = z + y + 'scan_log_y__.txt'

    print 'now scanning your code from the following file: %s' % scanFile 
    print 'The date is: %s' % str(time.asctime()) 

    with open('/v01/scans/%s' % log_name, 'a+') as scanz:
        scanz.write("Now scanning your code from the following file: %s " % scanFile)
	scanz.write("The date is: %s" % str(time.asctime()))
        scanz.write("\n\n") 


    try:
        subprocess.call('sonar-runner -Dproject.settings=' + scanFile + ' >>  /v01/scans/%s 2>&1 ' % log_name, shell=True)
	 
    except Exception, e:
        print "something went wrong with the sonar-runner SonarQube scan" 
        print "the following error was thrown: %s " % str(e)


    #append the date to the scan file 
    with open('/v01/scans/%s' % log_name, 'a+') as wd: 
        wd.write("\n The date is: %s \n" % str(time.asctime()))
	wd.write("\n It took roughly %s minutes to run this script." % ((time.time() - start)/60) )


def usage():

    """ This function displays how to use the program. """

    print """
 _|_|_|                _|_|_|                                              
 _|    _|  _|    _|  _|          _|_|    _|_|_|      _|_|_|  _|  _|_|      
 _|_|_|    _|    _|    _|_|    _|    _|  _|    _|  _|    _|  _|_|          
 _|        _|    _|        _|  _|    _|  _|    _|  _|    _|  _|            
 _|          _|_|_|  _|_|_|      _|_|    _|    _|    _|_|_|  _|            
                 _|                                                        
             _|_|         
    """
    print "PySonar -s --scanFile=/v01/scans/sonar-project.properties" 

    print "PySonar --help (will print this help information)" 






#start the program if it is called with 'python ' command from a shell
if __name__ == "__main__":
    
    #these are local variables to hold values from the command line
    #these variables are used to call the functions in this module

    
    scanFile1 = None
    scan = False 

    
    try:
        options, remainder = getopt.gnu_getopt(sys.argv[1:], 'sv', ['help', 
                                                      'scanFile=',])	
        for opt, arg in options: 
            
            if opt == '--scanFile':
                scanFile1 = arg
            elif opt == '-s':
                scan = True
	    elif opt == '-v':
		print 'OPTIONS    :', options 
                print "found some options: %s values: %s " % (opt, arg)
	    elif opt == '--help':
		usage()
		sys.exit(1)

        
        
            
    except getopt.GetoptError:
        print "the option you entered is not recognized"     
    

    if scan:
        if scanFile1 != None:
            print "running startScan(scanFile1)"
            startScan(scanFile1)

        else:
            startScan()
            print "running startScan()"

    if not scan:
        print "You should have '-s' in your program call."
	usage()
        sys.exit(1)
        
    

            
            

    



    

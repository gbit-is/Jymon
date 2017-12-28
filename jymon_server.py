#!/usr/bin/env python
from flask import Flask 	# Import webserver
app = Flask(__name__)   	# Initialise Flask stuff
import sys					# Needed for system interactions and more
import commands 				# Needed to call the jymon_executable
import time					# Needed for cache functions
import daemon				# Yeah, we wanna run this as a deamon, if not .... remove it 
from daemon import pidfile	# And those deamon should have pidfiles 
import argparse				# And those pidfile setups need to be parsed


jymon_executable = "/full/path/to/jymon.py" 	# Location of the jymon_executable, the other part of this project
port = 5000							# Port the webserver will run on
cache_time = 3							# Seconds for which the response is cached. 0 to disable cache


#Establish routes
@app.route('/') #Default server behaviour 
def index():

	try:
		message = callJymon()
		return message
	except:
		return "Error in def index calling \"call_Jymon\""

# If HTTP requests are made. This allow javascript to fetch the data
@app.after_request 
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response


# The function that is run when someone queries the server
def callJymon():


	# Establish that these vars are global
	global newtime 
	global oldtime
	global cached_response

	# Get the current time 
	newtime = gettime(0)


	if newtime < oldtime + cache_time: # If newtime is smaller then oldtime + cache time
		return cached_response # Then serve up the Cached response


	try:
		status, response   = commands.getstatusoutput(jymon_executable) # Run the jymon_executable
		oldtime = newtime	
		cached_response = response
		return response
	except:
		return "error in calling  the \"jymon_executable\""



def gettime(offset): #Offset is needed for first initalisation 
	stamp = int(time.time())
	try:
		stamp = stamp - offset
	except:
		stamp = stamp
	return stamp


# Start command
def startflask():
	try:
		app.run(host= '0.0.0.0', port=port, debug=False) #Starting flask server
	except:
		return False


# Runs the startup procedure, runs early on, runs only once
def startup():
	global oldtime #Make sure we are working with the global variable
	oldtime = gettime(3600) # Let's make sure that our oldtime exists and that it is smaller then our currenttime - cached_time

	startflask()	# Call the startflask function above


# runs the startup procedure as a daemon
def start_daemon(pidf,logf):
	with daemon.DaemonContext( 							# with deamon do stuff in the context of:
		working_directory='/usr/local/bin',				# Not sure what this line is for 
		umask=0o002,									# Or this one 
		pidfile=pidfile.TimeoutPIDLockFile(pidf),		# This ofcourse is .... something 
		) as context:									# okay, the confusing stuff is over, phew
		startup() 										# Finally, the actual running command 


# When run as main (normal run)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Health Check Daemon")	
    parser.add_argument('-p', '--pid-file', default='/var/run/healthcheck_daemon.pid')	# Location of pid file 
    parser.add_argument('-l', '--log-file', default='/var/log/healthcheck.log')			# Location of unused logfile

    args = parser.parse_args()															# Parse those arguments :)
    start_daemon(pidf=args.pid_file, logf=args.log_file)								# Call the deamon starter 



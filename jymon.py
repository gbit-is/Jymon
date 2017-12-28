#!/usr/bin/env python
# Import requirements
import commands # Needed to run the xymon-client
import json     # JSON is needed for this JSON based project, surprise



message_list = []; #Initalise list

xymon_client = "/usr/lib/xymon/client/bin/xymon" 	# Location of the xymon client
xymon_server = "xymonserver.intra"			# URL of the Xymon Server
xymon_board  = "xymondboard"				# name of the board, defaults are hobbitdboard or xymondboard (notice the d in there)


status, messages   = commands.getstatusoutput(xymon_client + " " + xymon_server + " " + xymon_board) # Run xymon client


messages = messages.decode('utf-8','ignore').encode("utf-8") # Let's just get rid of those pesky non-utf character



for line in messages.split('\n'): # Lets get to parsing the xymon data, split by newline seperators
		
        data = line.split('|') # the xymon client sends each data field with a | seperator


	# Let's assign the data to variables
	
	hostname 	= data[0]
	testname 	= data[1]
	testcolor 	= data[2]
	testflags 	= data[3]
	lastchange 	= data[4]
	logtime    	= data[5]
	validtime 	= data[6]
	acktime		= data[7]
	disabledtime	= data[8]
	sender		= data[9]


	# And populate a json with those variables

	parsed_data = {

		'hostname'	:	hostname,
		'testname'	:	testname,
		'testcolor'	:	testcolor,
		'testflags'	:	testflags,
		'lastchange'	:	lastchange,
		'logtime'	:	logtime,
		'validtime'	:	validtime,
		'acktime'	:	acktime,
		'disabledtime'	:	disabledtime,
		'sender'	:	sender
	}


	message_list.append(parsed_data)  # Then add those variables to the list



# Once all the responses have been parsed 
print json.dumps(message_list) # Print out the JSON
exit()

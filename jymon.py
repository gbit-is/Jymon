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
		'lanschange'	:	lastchange,
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

print "processing packages (DPKG)"
for line in packages.split('\n'):
        #str.split(line)
        #print line[3]
        pack = line.split(' ', 2)

        dpkgstat = pack[0]
        dpkgname = pack[1]
        dpkgvers = pack[2]
        comname = dpkgname.split(':',2)

	match = ""



        pack_data = {



		'@timestamp'		:	timestamp,
		'hostname'		:	hostname,
		'shorthost'		: 	shorthost,
		'osVersion'		:	osvers,
		'os'			:	"ubuntu",
		'packageName'		:	dpkgname,
		'installedVersion'	:	dpkgvers,
		'dpkgStatus'		:	dpkgstat






        }

      


	for s in message_list:
		#print "checking"
		#print s
		if comname[0] in str(s):
              		#print 'Yes'
			#print comname[0]
               		#print message_list.index(s)
               		#print
			match = "true" # comname[0]
		#else:
			#print 'No'
			#print comname[0]

        		#json_packages = json.dumps(pack_data)
			#message_list2.append(upgrade_data)



	if match:
		#print "matches"	
		match = "true"
	else:
		#print comname[0]
		#json_packages = json.dumps(pack_data)
		message_list2.append(pack_data)


	#print comname




        #print comname[0]

        #json_packages = json.dumps(pack_data)
        #es.index(index='v2_1', doc_type='packages', body=json.loads(json_packages))


        #if pack[0] == "ii":
        #       print "ii"
        #else:
        #       print "aSD"


#exit()



#message_list.append(message_list2)
message_list.extend(message_list2)
mess_length = len(message_list)
sending_status = 0

print " "
print "list contains %s reports" % (mess_length,)

print "sending message_list"
print "status:"



for item in message_list:

	json_upgrade = json.dumps(item)
	es.index(index='v3_0', doc_type='packages', body=json.loads(json_upgrade))

	if sending_status%100==0:
		print sending_status
		#print item
	sending_status=sending_status+1

print "done sending data"
exit()

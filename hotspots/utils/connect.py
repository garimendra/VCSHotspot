from P4 import P4, P4Exception 
from datetime import datetime
import math
import time

p4 = None

def connectToPerforce():
	global p4
	p4 = P4()  	   
	p4.host = "ptgperforce.corp.intuit.net"
	p4.port = "ptgperforce.corp.intuit.net:1666"

	p4.connect()



#############			Calculation of Rahman Score 	   ##################

epoch = datetime.utcfromtimestamp(0)


def unix_time(dt):
    return (dt - epoch).total_seconds()


def getScore(filepath) : 

	times = []
	
	#run_filelog Returns file history ordered by most recent check-in

	for fileRevisions in  p4.run_filelog(filepath)[0].revisions :
		times.append(unix_time(fileRevisions.time))

	timeRange = unix_time(datetime.now()) - times[len(times)-1]

	score = 0

	for idx in range(len(times)) :
		times[idx] -= times[len(times)-1]
		times[idx] /= timeRange
		score += 1/(1 + math.exp(-12*times[idx] + 12))

	return score


##########################################################################



def expand(root) :
	
	dirs = []
	files = []
	scores = []

	try : 
		di = p4.run("dirs", root + '*')
		
		for entry in di:
			st = entry['dir'].split('/')
			fol = st[len(st)-1]
			#print (fol)
			dirs.append(entry['dir'])

		fi = p4.run("files", root + '*')

		for entry in fi:
			path = entry['depotFile']
			# temp = getScore(path)
			# scores.append(temp)
			# st = path.split('/')
			# fil = st[len(st)-1]
			files.append(path)
			#print(fil)
		

	except:
		pass
	return dirs, files



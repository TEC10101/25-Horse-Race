import random
from random import randint
from random import random
from random import randrange
from random import uniform
import pdb

horseData = [
	["Alpha",None],
	["Brigadier",None],
	["Chutzpah",None],
	["Dragonfly",None],
	["Excalibur",None],
	#get name of random winning horse for prior round
   [None,None],
   ["Fame",None],
   ["Ghanima",None],
   ["Hockeye Hickory",None],
   ["Incredibly Idle",None],
# /!\ ##get name of random winning horse for prior round
	[None,None],
	["Jumping Jack",None],
	["Kendrasaurus",None],
	["Lucky",None],
	["Monty",None],
    #get name of random winning horse for prior round
    [None,None],
    ["Nano",None],
    ["Ouroboros",None],
    ["Peanut",None],
    ["Quasar",None],
    #get name of random winning horse for prior round
    [None,None],
    ["Rhastamon",None],
    ["Sticky Widget",None],
    ["Terwilliger Tango",None],
    ["Underdog",None],
    #get name of random winning horse for prior round
    [None,None],
    ["Vegeta",None],
    ["Why?",None],
    ["Xavier Omar",None],
    ["Yoshi",None]
    ]

winstreak = [None,None,None,None,None,]

# /!\ # I am going to have to change rand 0,4  to round(random()) to see if the same horse wins again because otherwise it's too much randomness!!!



randomWinnerThisRace = None
count = 0

raceWinner = (randrange(5))

for raceNumber in range(0,6,1): # race loop, race 6 times: race# 0,1,2,3,4,5
	print('In raceNumber begging, race#{}, count={}'.format(raceNumber,count))
	if raceNumber == 5:
		pdb.set_trace()
	# raceWinner = 
	# print('randWinner after randmizer:{}'.format(raceWinner))

	#### start first race... just the first race only
	if raceNumber == 0: 
		for theHorse in range(0,5): # horse 0,1,2,3,4 (alpha,brigadier, chutzpah, dragonfly,excalibur)
			print('Horse being assessed:{}'.format(horseData[count][0]))
			# print('In theHorse for loop, count={}'.format(count))
			
			if theHorse == raceWinner:
				horseData[count][1] = 1.0 	# set the winner's distance to 1.0    // I could just do this before the first race after firstRaceWinner
				horseData[5][0] = horseData[count][0] 	# update the data table, pos[5] races in the next race
				horseData[5][1] = horseData[count][1]	# carry their distance over too		   // I just realized this is overcomplicating things
				print('{}\'s distance in race{}: {}'.format(horseData[count][0], raceNumber, horseData[count][1]))
				count += 1

			else:
				horseData[count][1] = (uniform(.700, .999))
				print('{}\'s distance in race{}: {}'.format(horseData[count][0], raceNumber, horseData[count][1]))
				count += 1
	#### end  first race

	# /#\ # pdb.set_trace()

	#if wonAgain == 1:
	#	print('\nHorse {} WINS AGAIN!\n'.format(wonAgain)) # this is weird right now.  race has to finish first

	#if at least 1 race has been ran and all 6 races aren't over, assess whether same winner and adj data accordingly
	if count in (10, 15, 20, 25, 30) and horseData[count] != horseData[count-5]: 	# if these were equal it would mean the same horse won and thus no relative distance change
		#pdb.set_trace()
		for recurseAdj in range(0,(count-5)): 	# count-5 because the current count is the current race, -5 takes it to the previous race(s)
			horseData[recurseAdj][1] = (horseData[recurseAdj][1]*(horseData[count-5][1]))
	
	if raceNumber != 5:
		wonAgain = round(random())	#0 = no, 1 = yes
		winstreak[raceNumber] = wonAgain
		if wonAgain != 1:
			print('horse //{}// didn\'t win again'.format(horseData[5*(raceNumber + 1)]))
			print('current count: {}'.format(count))

	#### start second, third etc race analysis
	#if raceNumber > 0: # second, third, etc races
	if raceNumber != 0 and raceNumber != 5 and wonAgain == 1:
		# horseData[count][1] = 1.0 # set 5, 10, 15, 20, 25 as 1.0 (these are the winners)
		horseData[5*(raceNumber+1)][0] = horseData[count][0] # place winner into next race
		horseData[5*(raceNumber+1)][1] = 1.0 #set distance of next race = 1.0 //not explicitly needed has to check if wonAgain
		count += 1 # count 1 for the winning horse to move the analysis to the next horse
		for theHorse in range(1,5): # +1,+2,+3,+4 horses; 
			horseData[count][1] = (uniform(.700, .999)) # count equals the current analysis position
			print('{}\'s distance in race{}: {}'.format(horseData[count][0], raceNumber, horseData[count][1]))
			count += 1		# next


	elif raceNumber != 0 and raceNumber != 5 and wonAgain != 1: # if wonAgain != 1/if horseHasToBattleAgainForTopPosition
		raceWinner = (randrange(5)) # choose a random winner, could be same horse
		for theHorse in range(0,5):
			if theHorse == raceWinner:
				horseData[5*(raceNumber+1)][0] = horseData[count][0] #5*raceNum+1 = place winner into next race
				horseData[5*(raceNumber+1)][1] = 1.0 #set distance of next race = 1.0 //not needed has to check if wonAgain
				horseData[count][1] = 1.0
				count += 1
			else:
				horseData[count][1] = (uniform(.700, .999))
				print('{}\'s distance in race{}: {}'.format(horseData[count][0], raceNumber, horseData[count][1]))
				count += 1

	elif raceNumber == 5 and wonAgain == 1: #6th race, last race
		count += 1
		for theHorse in range(1,5): # +1,+2,+3,+4 horses; 
			horseData[count][1] = (uniform(.700, .999)) # count equals the current analysis position
			print('{}\'s distance in race{}: {}'.format(horseData[count][0], raceNumber, horseData[count][1]))
			count += 1		# next

	elif raceNumber == 5 and wonAgain != 1: # 6thracenumber == 5 and horsewinsagain != 1
		raceWinner = (randrange(5)) # choose a random winner, could be same horse
		for theHorse in range(0,5):
			if theHorse == raceWinner:
				horseData[count][1] = 1.0
				count += 1
			else:
				horseData[count][1] = (uniform(.700, .999))
				print('{}\'s distance in race{}: {}'.format(horseData[count][0], raceNumber, horseData[count][1]))
				count += 1

		if count == 30: 	# if these were equal it would mean the same horse won and thus no relative distance change
			# pdb.set_trace()
			for recurseAdj in range(0,(count-5)): 	# count-5 because the current count is the current race, -5 takes it to the previous race(s)
				horseData[recurseAdj][1] = (horseData[recurseAdj][1]*(horseData[count-5][1]))

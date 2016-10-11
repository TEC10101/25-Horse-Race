from random import randint
from random import random
from random import randrange

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


# /!\ # I am going to have to change rand 0,4  to round(random()) to see if the same horse wins again because otherwise it's too much randomness!!!



randomWinnerThisRace = None
count = 0
for j in range(0,6,1):
	print('In j for loop, race#{}, count={}, randWinTR:{}'.format(j, count,randomWinnerThisRace))
	randomWinnerThisRace = (randrange(5))
	print('randWinTR after randmoizer:{}'.format(randomWinnerThisRace))

	#if j > 0 and j < 6 and randomWinnerThisRace == 0: # assess whether same winner and adj data accordingly
	for i in range(0,5,1):
		print('Horse being assessed:{}'.format(horseData[count][0]))
		print('In i for loop, count={}'.format(count))
		if i == randomWinnerThisRace:
			if j == 5: # reserved if stmt for last race so don't place winner up against ghosts :)
				horseData[count][1] = 1.0
			else: # do this when assessing winner:
				horseData[5*(j+1)][0] = horseData[count][0]
				horseData[5*(j+1)][1] = horseData[count][1]
				horseData[count][1] = 1.0
				print('Current Fastest: {}'.format(horseData[count][1]))
		else:
			horseData[count][1] = (random())
		count += 1
		if count in (10, 15, 20, 25, 30) and randomWinnerThisRace != 0:
			for adjRelativeDist in range(0,(count-5)):
				# adjRatio = [5*(j+1)]
				horseData[adjRelativeDist][1] = (horseData[adjRelativeDist][1]*(horseData[count-5][1]))

horseData.sort(key=lambda pair: pair[1])
# for top3 in range(4):
enumerate(horseData)

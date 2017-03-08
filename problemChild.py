# Python 3.5.2 IDLE x86/32-bit
# Author: Tyler Corum, 10/11/2016
# Purpose: A group of people were presented the following problem to solve.  I have done just that and I am building the program in Python to demonstrate it to you.  This is a great learning experience for me, and I am pround to have presented it to the class as well.  I had found the solution in relatively less steps than others.  Even the website I found the problem had it solved in more steps than what I was able to solve it in.  http://www.programmerinterview.com/index.php/puzzles/25-horses-3-fastest-5-races-puzzle/  I hope you enjoy!
#
# Tested On: Windows 7 x64


# ____________________Table Of Contents____________________
#
# 1. Introduction to the problem
# 2. Import, functions, objects/variables
# 3. Processing
# 4. 
#
# 999. TESTING
#
# /$\ # urgent and important
# /!\ # important
# /#\ # important but not ugent
# /?\ # error?/unknown?


# 1. Introduction to the problem
# ------------------------------
# 	Outline:  Let’s say that you have 25 horses, and you want to pick the fastest 3 
#	horses out of those 25. In each race, only 5 horses can run at the same time because 
# 	there are only 5 tracks. What is the minimum number of races required to find the 3 
# 	fastest horses without using a stopwatch?
#
#	My solution:  Race 5 horses.  Once the top fastest horse of that race crosses the
# 	finish line, create a photo finish of the position of the 4 other horses relative
# 	to the fastest.  We can use the fastest as a point of relativity for the rest of
# 	the 20 horses by racing 4 new horses with it.  If the horse still wins, the relative
#	position of all horses remains the same, but if he doesn't come in first, it means
# 	that all prior racers need to be adjusted relative to the fastest's new relative
# 	position.
#
#	Illustration: horse1 comes in first, his relative position to the other horses is
#	1.000  Lets say the rest of the horses only reached 50% of the way complete when
#   horse1 finished.  This means they are 0.500.  Let's say he races 4 new horses, and 
#   a new leader emerges.  The newLeader is now 1, and with examining the second race's photo finish, you
#	determine horse1 only made it 50% of the way by the time the second race's winner
# 	passed the finish line.  This means horse2, horse3, horse4, and horse5 now are a
#	further 50% relative to the newLeader's distance.
#	
#	First Race:
#	|===============================horses2-5|==================================horse1|
#	|==============================horses2-5|=================================horse1|
#	|=============================horses2-5|================================horse1|
#	|============================horses2-5|===============================horse1|
#	|===========================horses2-5|===========================horse1|
#	|=========================horses2-5|========================horse1|
#	|=======================horses2-5|=====================horse1|
#	|====================horses2-5|===================horse1|
#	|================horses2-5|===================horse1|
# 	Second Race: =horses2-5|================horse1|
# 	|===========horses2-5|============horses1|===============================newLeader|
# 	
# 	...and so on, shifting their relative distance ran to the current-fastest horse.  
#	The minimum amount of races to complete this problem is 6.  Now I'm going to code
#	it in Python.


# 2. Import, functions, objects/variables
# ---------------------------------------

import random
from random import randint
from random import random
from random import randrange
from random import uniform
import pdb
# from  more_itertools import unique_everseen


def sortList_Asc(listIndex):
	lengthOfList = len(listIndex)

	for eachPass in range(lengthOfList-1):
		for i in range(0,lengthOfList-1):
			if listIndex[i][1] >= listIndex[i+1][1]:
				temp0 = listIndex[i][0]
				temp1 = listIndex[i][1]
				listIndex[i][0] = listIndex[i+1][0]
				listIndex[i][1] = listIndex[i+1][1]
				listIndex[i+1][0] = temp0
				listIndex[i+1][1] = temp1
				if lengthOfList == 2:  #once only a pair left, break so not get stuck in loop
					break

def printTop3(horseData):
# this is the placeholder list for the Top 3 horses
	top3List = [
		[None,None],
		[None,None],
		[None,None]
		]

	top3Count = 0 # this will count 0>1>2 then print results and break the loop

	for top3Check in range(29,21,-1):
		if top3Count == 3:
			print('\n\nTop Horse: \t{}: {:06.4f}\nSecond: \t{}: {:06.4f}\nThird: \t\t{}: {:06.4f}\n'.format(top3List[0][0],top3List[0][1],top3List[1][0],top3List[1][1],top3List[2][0],top3List[2][1]))
			break
		elif horseData[top3Check-1][0] == horseData[top3Check][0]:
			top3Check = top3Check-1
		else:
			top3List[top3Count][0] = horseData[top3Check][0]
			top3List[top3Count][1] = horseData[top3Check][1]
			top3Count += 1
	

# I don't have a way to randomly pit horses against each other, they are pitted linearly
horseData = [ # race0/first race
	["Alpha            ",None],
	["Brigadier        ",None],
	["Chutzpah         ",None],
	["Dragonfly        ",None],
	["Excalibur        ",None],
	# race1/second race
	[None,None], # place holder for prev winner
	["Fame             ",None],
	["Ghanima          ",None],
	["Hockeye Hickory  ",None],
	["Incredibly Idle  ",None],
	# race2/third race
	[None,None], # place holder for prev winner
	["Jumping Jack     ",None],
	["Kendrasaurus     ",None],
	["Lucky            ",None],
	["Monty            ",None],
	# race3/fourth race
	[None,None], # place holder for prev winner
	["Nano             ",None],
	["Ouroboros        ",None],
	["Peanut           ",None],
	["Quasar           ",None],
	# race4/fifth race
	[None,None], # place holder for prev winner
	["Rhastamon        ",None],
	["Sticky Widget    ",None],
	["Terwilliger Tango",None],
	["Underdog         ",None],
	# race5/sixth race
	[None,None], # place holder for prev winner
	["Vegeta           ",None],
	["Why?             ",None],
	["Xavier Omar      ",None],
	["Yoshi            ",None],
	]

# just a list to say if a horse won again or not, no real use.  may turn it into something
winstreak = [None,None,None,None,None,]

# just declaring the variable which will be used later
randomWinnerThisRace = None

# count is the index of horses, essential their "ID" throughout the script
count = 0

# choose the first race winner before the first race is even started :3
raceWinner = (randrange(5))




# from tkinter import *
# from tkinter import ttk
# root = Tk()

# # root.title('25 Horse Race')
# # root.state('zoomed')
# # root.maxsize(800,600)
# # root.minsize(640,480)

# notebook = ttk.Notebook(root).pack()
# race0 = ttk.Frame(notebook)
# race1 = ttk.Frame(notebook)
# race2 = ttk.Frame(notebook)
# race3 = ttk.Frame(notebook)
# race4 = ttk.Frame(notebook)
# race5 = ttk.Frame(notebook)
# # only add the first race frame:
# # notebook.add(race0, text = 'First Race')
# # ttk.Button(race0, text = 'Race The Horses').pack()

# root.mainloop()



# 3. Processing
# -------------

for raceNumber in range(0,6,1): # race loop, race 6 times: race# 0,1,2,3,4,5

	#### start first race... just the first race only
	if raceNumber == 0: 
		print('\nRace #{} Results:'.format((raceNumber+1))) # zero indexed so i'm translating
		for theHorse in range(0,5): # horse 0,1,2,3,4 (alpha,brigadier, chutzpah, dragonfly,excalibur)			
			if theHorse == raceWinner:
				horseData[count][1] = 1 	# set the winner's distance to 1    // I could just do this before the first race after firstRaceWinner
				horseData[5][0] = horseData[count][0] 	# update the data table, pos[5] races in the next race
				horseData[5][1] = horseData[count][1]	# carry their distance over too		   // I just realized this is overcomplicating things
				print('{}\tis the winner:\t{:06.4f}'.format(horseData[count][0],horseData[count][1]))
				count += 1

			else:
				horseData[count][1] = (uniform(.850, .950))
				print('{}\tran this far:\t{:06.4f}'.format(horseData[count][0],horseData[count][1]))
				count += 1
	#### end  first race

	if count in (10, 15, 20, 25, 30) and horseData[count] != horseData[count-5]: 	# if these were equal it would mean the same horse won and thus no relative distance change
		#pdb.set_trace()
		for recurseAdj in range(0,(count-5)): 	# count-5 because the current count is the current race, -5 takes it to the previous race(s)
			horseData[recurseAdj][1] = (horseData[recurseAdj][1]*(horseData[count-5][1]))
	
	if raceNumber != 5:
		wonAgain = round(random())	#0 = no, 1 = yes
		winstreak[raceNumber] = wonAgain

	#### start second, third etc race analysis
	if raceNumber != 0 and raceNumber != 5 and wonAgain == 1:
		# horseData[count][1] = 1 # set 5, 10, 15, 20, 25 as 1 (these are the winners)
		horseData[5*(raceNumber+1)][0] = horseData[count][0] # place winner into next race
		horseData[5*(raceNumber+1)][1] = 1 #set distance of next race = 1 //not explicitly needed has to check if wonAgain
		print('\nRace #{} Results:\n{}\tis the winner:\t{:06.4f}'.format((raceNumber+1),horseData[count][0],horseData[count][1])) # zero indexed so i'm translating

		count += 1 # count 1 for the winning horse to move the analysis to the next horse
		for theHorse in range(1,5): # +1,+2,+3,+4 horses; 
			horseData[count][1] = (uniform(.850, .950)) # count equals the current analysis position
			print('{}\tran this far:\t{:06.4f}'.format(horseData[count][0],horseData[count][1]))
			count += 1		# next


	if raceNumber != 0 and raceNumber != 5 and wonAgain != 1: # if wonAgain != 1/if horseHasToBattleAgainForTopPosition
		raceWinner = (randrange(5)) # choose a random winner, could be same horse
		print('\nRace #{} Results:'.format((raceNumber+1))) # zero indexed so i'm translating

		for theHorse in range(0,5):
			if theHorse == raceWinner:
				horseData[5*(raceNumber+1)][0] = horseData[count][0] #5*raceNum+1 = place winner into next race
				horseData[5*(raceNumber+1)][1] = 1 #set distance of next race = 1 //not needed has to check if wonAgain
				horseData[count][1] = 1
				print('{}\tis the winner:\t{:06.4f}'.format(horseData[count][0],horseData[count][1]))
				count += 1
			else:
				horseData[count][1] = (uniform(.850, .950))
				print('{}\tran this far:\t{:06.4f}'.format(horseData[count][0],horseData[count][1]))
				count += 1

	if raceNumber == 5 and wonAgain == 1: #6th race, last race
		print('\nRace #{} Results:\n{}\tis the winner: \t{:06.4f}'.format((raceNumber+1),horseData[count][0],horseData[count][1])) # zero indexed so i'm translating

		count += 1
		for theHorse in range(1,5): # +1,+2,+3,+4 horses; 
			horseData[count][1] = (uniform(.850, .950)) # count equals the current analysis position
			print('{}\tran this far:\t{:06.4f}'.format(horseData[count][0],horseData[count][1]))
			count += 1		# next

	if raceNumber == 5 and wonAgain != 1: # 6thracenumber == 5 and horsewinsagain != 1
		print('\nRace #{} Results:'.format((raceNumber+1))) # zero indexed so i'm translating
		raceWinner = (randrange(5)) # choose a random winner, could be same horse
		for theHorse in range(0,5):
			if theHorse == raceWinner:
				horseData[count][1] = 1
				print('{}\tis the winner:\t{:06.4f}'.format(horseData[count][0],horseData[count][1]))

				count += 1
			else:
				horseData[count][1] = (uniform(.850, .950))
				print('{}\tran this far:\t{:06.4f}'.format(horseData[count][0],horseData[count][1]))
				count += 1

		if count == 30: 	# if these were equal it would mean the same horse won and thus no relative distance change
			# pdb.set_trace()
			for recurseAdj in range(0,(count-5)): 	# count-5 because the current count is the current race, -5 takes it to the previous race(s)
				horseData[recurseAdj][1] = (horseData[recurseAdj][1]*(horseData[count-5][1]))


sortList_Asc(horseData)
printTop3(horseData)
# pdb.set_trace()























# 999. TESTING























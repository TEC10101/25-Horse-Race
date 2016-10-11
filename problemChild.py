# Python 3.5.2
# Author: Tyler Corum
# Purpose: A group of people were presented the following problem to solve.  I have done
#			that conceptually, and I am building the program in Python to demonstrate.
# Tested On: Windows 7 x64


# ____________________Table Of Contents____________________
# 1. Introduction to the problem
# 2. Import
# 3. Chapter 2 exercise, def a class and methods to change text on button click
# 4. Chapter 3 exercise, using label widget to display text
# 	4.a ch03/01_label.py
# 	4.b ch03/02_button.py
# 	4.c ch03/03_selection_buttons.py
# 	4.d ch03/04_entry.py
# 	4.e ch03/05_selection_boxes.py
# 	4.f ch03/06_progressbar_scale.py
# 5. Chapter 4 exercise, frames and organizational widgets
# 	5.a ch04/01_frame.py
# 	5.b ch04/02_toplevel.py
# 	5.c ch04/03_panedwindow.py
# 	5.d ch04/04_notebook.py
#
# 666. TESTING
#
# /$\ # urgent and important
# /!\ # important
# /#\ # important but not ugent
# /?\ # error?/unknown?


# 1. Introduction to the problem
# ------------------------------
# 	Outline:  There are 25 race horses and a racetrack with 5 lanes.  You do not have a
# 	stopwatch but are expeced to figure out which of them are the Top 3 fastest.  You
# 	can race a maximum of 5 horses at a time.  What is the fewest number of races you
#	can find the Top 3?
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
#	1.0.  Lets say the rest of the horses only reached 50% of the way complete.  This
#	means they are 0.5.  Let's say he races 4 new horses, and a new leader emerges.
#	The newLeader is now 1.0, and with examining the second race's photo finish, you
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


# 2. Import and build root
# -------------------------------
from tkinter import *
from tkinter import ttk
root = Tk()

# root.title('25 Horse Race')
# root.state('zoomed')
# root.maxsize(800,600)
# root.minsize(640,480)

notebook = ttk.Notebook(root).pack()
race0 = ttk.Frame(notebook)
race1 = ttk.Frame(notebook)
race2 = ttk.Frame(notebook)
race3 = ttk.Frame(notebook)
race4 = ttk.Frame(notebook)
race5 = ttk.Frame(notebook)
# only add the first race frame:
# notebook.add(race0, text = 'First Race')
# ttk.Button(race0, text = 'Race The Horses').pack()










root.mainloop()




























# 666. TESTING
# button = ttk.Button(root, text = 'Next Race')
# def callback():
# 	print('Clicked!')
# button.config(command = callback)
# button.state(['disabled'])

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

		if count == 30 and horseData[count] != horseData[count-5]: 	# if these were equal it would mean the same horse won and thus no relative distance change
			pdb.set_trace()
			for recurseAdj in range(0,(count-5)): 	# count-5 because the current count is the current race, -5 takes it to the previous race(s)
				horseData[recurseAdj][1] = (horseData[recurseAdj][1]*(horseData[count-5][1]))



# for top3 in range(4):

print('\nTop Horse: {}:{}\nSecond: {}:{}\nThird: {}:{}\n'.format(horseData[29][0],horseData[29][1],horseData[28][0],horseData[28][1],horseData[27][0],horseData[27][1]))
# if any(s in line for s in ('string1', 'string2', ...)):
# if 1 in (x, y, z):



# didThatHorseWin = [
# 	0,0,0,0,0,
# 	0,0,0,0,0,
# 	0,0,0,0,0,
# 	0,0,0,0,0,
# 	0,0,0,0,0,
# 	0,0,0,0,0
# 	]

# horseDistances = [
# 	None, None, None, None, None,
# 	None, None, None, None, None,
# 	None, None, None, None, None,
# 	None, None, None, None, None,
# 	None, None, None, None, None,
# 	None, None, None, None, None
# 	]





wonAgain = round(random())
print(wonAgain)














def randomWinner(listIndex):
	randWinningHorse = int(rand(0,4))
	for i in range(0,5):
		if i == listIndex[i]:
			horseData[6][0] = horseData[randWinningHorse][0]
			horseData[6][1] = horseData[randWinningHorse][1]
			horseData[6][2] = 1.0






























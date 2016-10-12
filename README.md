Outline:  Let’s say that you have 25 horses, and you want to pick the fastest 3 
horses out of those 25. In each race, only 5 horses can run at the same time because 
there are only 5 tracks. What is the minimum number of races required to find the 3 
fastest horses without using a stopwatch?

My solution:  Race 5 horses.  Once the top fastest horse of that race crosses the
finish line, create a photo finish of the position of the 4 other horses relative
to the fastest.  We can use the fastest as a point of relativity for the rest of
the 20 horses by racing 4 new horses with it.  If the horse still wins, the relative
position of all horses remains the same, but if he doesn't come in first, it means
that all prior racers need to be adjusted relative to the fastest's new relative
position.

Illustration: horse1 comes in first, his relative position to the other horses is
1.000  Lets say the rest of the horses only reached 50% of the way complete when
 horse1 finished.  This means they are 0.500.  Let's say he races 4 new horses, and 
 a new leader emerges.  The newLeader is now 1, and with examining the second race's photo finish, you
determine horse1 only made it 50% of the way by the time the second race's winner
passed the finish line.  This means horse2, horse3, horse4, and horse5 now are a
further 50% relative to the newLeader's distance.

First Race:
|===============================horses2-5|==================================horse1|
|==============================horses2-5|=================================horse1|
|=============================horses2-5|================================horse1|
|============================horses2-5|===============================horse1|
|===========================horses2-5|===========================horse1|
|=========================horses2-5|========================horse1|
|=======================horses2-5|=====================horse1|
|====================horses2-5|===================horse1|
|================horses2-5|===================horse1|
Second Race: =horses2-5|================horse1|
|===========horses2-5|============horses1|===============================newLeader|

...and so on, shifting their relative distance ran to the current-fastest horse.  
The minimum amount of races to complete this problem is 6.  Now I'm going to code
it in Python.

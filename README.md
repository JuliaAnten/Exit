# Exit - Rush Hour
[![BCH compliance](https://bettercodehub.com/edge/badge/JuliaAnten/Exit?branch=master)](https://bettercodehub.com/)

# Information
# Authors
<h3> Julia Anten, Maxim Stomphorst, Sander Swierts<h3/>


# University
University of Amsterdam<br>
Course: Heuristieken<br>
Rech supervisor: Wietze Slagman<br>
Date: 1 juni 2017


## How to run!
This program needs at least 3 arguments and at most 4.
1. The program name. `./test.py`
2. The path to the board that needs to be solved. `/boards/01.txt`
3. The algorithm the program has to use. `breadth` or `depth` or `random`
3. The number of tries it has to peform. [optional.] `2 or above`<br>
For example:
```
./test.py boards/01.txt breadth
./test.py boards/02.txt depth
./test.py boards/03.txt random 50
argv 1    arg 2         arg 3  arg 4
```

## Its purpose
This programme is written in python 3.6.0 and is designed to solve Rush Hour boards/configurations which are placed in the folder `~/boards/`.
This programme contains 3 way's to solve the puzzels:
1. Random Search RS
2. Breadth First Search BFS
3. Depth First Search DFS
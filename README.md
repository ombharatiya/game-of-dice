# Game Of Dice

The "Game of Dice" is a multiplayer game where N players roll a 6 faced dice in a round-robin
fashion. Each time a player rolls the dice their points increase by the number (1 to 6) achieved
by the roll.

As soon as a player accumulates M points they complete the game and are assigned a rank.
Remaining players continue to play the game till they accumulate at least M points. The game
ends when all players have accumulated at least M points.

## Rules of the game
- The order in which the users roll the dice is decided randomly at the start of the game.
- If a player rolls the value "6" then they immediately get another chance to roll again and move
ahead in the game.
- If a player rolls the value "1" two consecutive times then they are forced to skip their next turn
as a penalty.

## How to run?

The current code is a simple python program that can be easily run through command line interface.

### Step 1 - Clone the code locally
    git clone https://github.com/ombharatiya/game-of-dice.git

### Step 2 - Get into the project directory
    cd game-of-dice

### Step 3 - Run the test 
    python Game/Game.py test

Note:  Currently only one test has been added

### Step 4 - Run the program

It takes two arguments: numof players & target score

    python Game/Game.py 2 25

### More details

If you're having any issue, just try to run the Game.py file

    python your/path/to/Game.py

And you'll get further instructions to run the program on Command line.

## Implementation Details
- Project uses Python Programming Language - This folder can be easily used in any Django/Flask application for any business logic implementation with correct views and fewer modifications
- The code uses Count Sort for printing the Score Board at every game pass
- The `GamePlay` is the main class for Game Play Implementations
- `Player` is the class for Player and Their Score Implementations
- `ScoreBoard` is the class for Score Board related Implementations
- `Dice` is the class for Dice functionality & faces Implementations
- `CustomException` is the class for handling any customised Exception baaed on various parameters
- `TestGamePlay` is the class for running Unit tests on the whole program
- Most of the identifiers & variables have self-explanatory names

Note: One example output has been saved in `example.txt`

## Author

  - **Om Bharatiya** 
    [Om Bharatiya](https://github.com/ombharatiya)
 

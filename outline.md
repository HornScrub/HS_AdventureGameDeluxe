# AdventureGameDeluxe (name pending...)

## OVERVIEW

I want to make an Python adventure game that combines realtime movement with turn based combat. You explore rooms, collect items, fight enemies, and attempt to escape the level.

I will be required to:

- Make a Window pop out for the game.
- Figure out how to make a top-down view of the game.
- Figure out how to use arrow keys to control movement of your character.
- Figure out how to create a navagatable level.
- Create a combat system.
- Create character information that could contain stats, items, weapons, treasure, etc.
- Create enemy to populate the dungeon that have their own stats and behaviors.
- Other things that I don't even know I have to implement yet.

Modules needed: 
    pygame
    
AdventureGameDeluxe/
│
├── main.py - initializes pygame, creates the display and game instances, runs the main game loop
├── display.py - Handles the creation and management of the display
├── events.py 
├── game.py - Contains the main game logic, including updating and rendering the player
├── player.py 
├── enemy.py
├── settings.py - stores game settings and constants
└── assets/
    ├── images/
    └── sounds/

7/10 - Learned how to make a fullscreen window with a button you can click to exit the game.

7/11 - Learned the fundamentals of a game loop, and how events are handled by defined behaviors within our game logic. Right now, its just a little blue rectangle I can move around with the arrow keys.


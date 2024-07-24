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

- main.py - initializes pygame, creates the display and game instances, runs the main game loop
- display.py - Handles the creation and management of the display
- events.py 
- level.py - Handles the management of the displayed level, like objects.
- game.py - Contains the main game logic, including updating and rendering the player
- player.py - Contains player information, like movement behavior
- enemy.py
- settings.py
 assets/
    images/
    sounds/

7/10 - Learned how to make a fullscreen window with a button you can click to exit the game.

7/11 - Learned the fundamentals of a game loop, and how events are handled by defined behaviors within our game logic. Right now, its just a little blue rectangle I can move around with the arrow keys.

7/12 - Worked on creating static objects in the game, some obstacles that stop the player from moving around. Also had to figure out some frustrating issues with
getting the movement how I want it to work and what happens when you collide with the edge of the screen and objects.

7/14 - Added a UI bezel, updated collisions. Trying to figure out how interpreters work and pathing with python modules.

7/24 - Been a while. Updated collisions so now you can smush up against objects and the display. Made the beginnings of a vision cone.

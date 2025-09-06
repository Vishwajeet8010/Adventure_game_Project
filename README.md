# Adventure Game

## Video Demo: <https://youtu.be/3uS5j1OChNk>  

### Description

## Introduction

This is a simple adventure game written in Python. In this player can move between rooms, pick up items, and view their inventory. The game includes a few predefined rooms and items to get started.

This Python code describes an engaging story-based story where players can explore different rooms, collect
items, and navigate virtual environments.
The game is built with two main classes: Room and Player.
Room classes represent individual rooms, each with names, descriptions, and features, as well as ways to
connect to other rooms and display room information.
The Player class represents the player, keeps track of their current location and collections, and provides
ways to move between rooms and collect items.
The create_world function sets up the initial game environment by creating classes, populating objects, and
connecting them.
The play_game function handles the main game loop, processing user commands to move, retrieve objects, and
display game information.

## Project Files

### 'project.py'

This project contain two classes first class room: and second class player: . In class room functions are connect, get_description, get_items, get_available_directions and in class player move, take_item,  get_store,  create_world.

## Project Structure

- `adventure_game.py`: The main game file containing the `Room` and `Player` classes, the `create_world` function to set up the game world, and the `play_game` function to start the game in `play_game` used while loop ans also used if, elif, else condition.
- `test_adventure_game.py`: Test file containing unit tests for the game using the `pytest` framework.
- `README.md`: This file, providing an overview of the project. It just a summary type.

## Classes

There are two classes are used they are described below.

### `Room`
Represents a room in the game. Each room has:
- `name`: The name of the room.
- `explanation`: A description of the room.
- `objects`: A list of objects in the room.
- `joint_rooms`: A dictionary of directions and connected rooms.

### `Player`
Represents the player in the game. The player has:
- `current_room`: The room the player is currently in.
- `stores`: A list of items the player has picked up.

## Functions

### `create_world()`
Creates the game world by defining rooms, adding objects to rooms, and connecting rooms.
This creates a new game for player. Which contains room, adds objects in it and connecting the room.

### `play_game()`
Starts the game, allowing the player to interact with the game world through a command-line interface. 
Player can play the game by giving multiple commands. After giving command game will be start and player can enjoy the game.

## Game Commands

- `look`: Look around in the current room. Describes the current room.
- `move [direction]`: Move in a specified direction (north, south, east, west).
- `take [item]`: Take an item from the current room.
- `stores`: Show the items in the player's inventory.
- `help`: Display a list of available commands.
- `quit`: Quit the game.

## Running the Game

To play the game, run the following command

python adventure_game.py

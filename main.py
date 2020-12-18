"""
Name: Tetris/main.py
Description: Tetris in Python using Tkinter
Author: Nathan "Nathcat" Baines
"""

import random
from tkinter import *
from tkinter import messagebox


"""
Shape class objects
"""


# Class for L shape
class L:
    # __init__
    def __init__(self, game_box):
        self.game_box = game_box
        # Body types for each rotation
        self.body_types = {
            'horizontal-r': ["=", "=", "=", "="],
            'vertical': ["=", "=", "=", "="],
            'upside-down': ["=", "=", "=", "="],
            'horizontal-l': ["=", "=", "=", "="],

        }

        # Current rotation
        self.rotation = 'vertical'
        # Positions of each body piece
        self.positions = [[0, 0], [0, 1], [0, 2], [1, 2]]

        self.falling = True

    # Method to change the rotation of the shape
    def toggle_rotation(self):
        # Vertical to horizontal-r
        if self.rotation == 'vertical':
            self.rotation = 'horizontal-r'
            self.positions = [[self.positions[0][0] + 1, self.positions[0][1] + 1],
                              [self.positions[1][0], self.positions[1][1]],
                              [self.positions[2][0] - 1, self.positions[2][1] - 1],
                              [self.positions[3][0] - 2, self.positions[3][1]]]

        # Horizontal-r to upside-down
        elif self.rotation == 'horizontal-r':
            self.rotation = 'upside-down'
            self.positions = [[self.positions[0][0] - 1, self.positions[0][1] + 1],
                              [self.positions[1][0], self.positions[1][1]],
                              [self.positions[2][0] + 1, self.positions[2][1] - 1],
                              [self.positions[3][0], self.positions[3][1] - 2]]

        # Upside-down to horizontal-l
        elif self.rotation == 'upside-down':
            self.rotation = 'horizontal-l'
            self.positions = [[self.positions[0][0] - 1, self.positions[0][1] - 1],
                              [self.positions[1][0], self.positions[1][1]],
                              [self.positions[2][0] + 1, self.positions[2][1] + 1],
                              [self.positions[3][0] + 2, self.positions[3][1]]]

        # Horizontal-l to vertical
        else:
            self.rotation = 'vertical'
            self.positions = [[self.positions[0][0] + 1, self.positions[0][1] - 1],
                              [self.positions[1][0], self.positions[1][1]],
                              [self.positions[2][0] - 1, self.positions[2][1] + 1],
                              [self.positions[3][0], self.positions[3][1] + 2]]

    # Method to update the body positions (ie: [position_index][1] += 1), only if self.falling == True
    def update_positions(self):
        for x in range(0, len(self.positions)):
            if self.falling:
                self.positions[x][1] += 1

    # Method to undo the update_positions() method
    def undo_update(self):
        for x in range(0, len(self.positions)):
            self.positions[x][1] -= 1


# Pyramid shape class
class Pyramid:
    # __init__
    def __init__(self, game_box):
        self.game_box = game_box
        self.body_types = {
            'horizontal-r': ["=", "=", "=", "="],
            'vertical': ["=", "=", "=", "="],
            'upside-down': ["=", "=", "=", "="],
            'horizontal-l': ["=", "=", "=", "="],

        }

        self.rotation = 'vertical'
        self.positions = [[1, 0], [0, 1], [1, 1], [2, 1]]

        self.falling = True

    def toggle_rotation(self):
        if self.rotation == 'vertical':
            self.rotation = 'horizontal-r'
            self.positions = [[self.positions[0][0] + 1, self.positions[0][1]],
                              [self.positions[1][0] + 1, self.positions[1][1] - 2],
                              [self.positions[2][0], self.positions[2][1] - 1],
                              [self.positions[3][0] - 1, self.positions[3][1]]]

        elif self.rotation == 'horizontal-r':
            self.rotation = 'upside-down'
            self.positions = [[self.positions[0][0] - 1, self.positions[0][1] + 1],
                              [self.positions[1][0] + 1, self.positions[1][1] + 1],
                              [self.positions[2][0], self.positions[2][1]],
                              [self.positions[3][0] - 1, self.positions[3][1] - 1]]

        elif self.rotation == 'upside-down':
            self.rotation = 'horizontal-l'
            self.positions = [[self.positions[0][0] - 1, self.positions[0][1] - 1],
                              [self.positions[1][0] - 1, self.positions[1][1] - 1],
                              [self.positions[2][0], self.positions[2][1]],
                              [self.positions[3][0] + 1, self.positions[3][1] + 1]]

        else:
            self.rotation = 'vertical'
            self.positions = [[self.positions[0][0] + 1, self.positions[0][1]],
                              [self.positions[1][0] - 1, self.positions[1][1] + 2],
                              [self.positions[2][0], self.positions[2][1] + 1],
                              [self.positions[3][0] + 1, self.positions[3][1]]]

    def update_positions(self):
        for x in range(0, len(self.positions)):
            if self.falling:
                self.positions[x][1] += 1

    def undo_update(self):
        for x in range(0, len(self.positions)):
            self.positions[x][1] -= 1


# Square class
class Square:
    def __init__(self, game_box):
        self.game_box = game_box
        self.body_types = {
            'default': ["=", "=", "=", "="]
        }

        self.rotation = 'default'
        self.positions = [[0, 0], [1, 0], [0, 1], [1, 1]]

        self.falling = True

    def toggle_rotation(self):
        # This shape's rotation is redundant, so just return None.
        # We have to have this method to prevent an error in case the user tries to rotate the shape
        return None

    def update_positions(self):
        for x in range(0, len(self.positions)):
            if self.falling:
                self.positions[x][1] += 1

    def undo_update(self):
        for x in range(0, len(self.positions)):
            self.positions[x][1] -= 1


# Line class
class Line:
    def __init__(self, game_box):
        self.game_box = game_box
        self.body_types = {
            'horizontal': ["=", "=", "=", "="],
            'vertical': ["=", "=", "=", "="]
        }

        self.rotation = 'horizontal'
        self.positions = [[0, 0], [1, 0], [2, 0], [3, 0]]

        self.falling = True

    def toggle_rotation(self):
        if self.rotation == 'vertical':
            self.rotation = 'horizontal'
            self.positions = [[self.positions[0][0] - 3, self.positions[0][1] + 3],
                              [self.positions[1][0] - 2, self.positions[1][1] + 2],
                              [self.positions[2][0] - 1, self.positions[2][1] + 1],
                              [self.positions[3][0], self.positions[3][1]]]
        else:
            self.rotation = 'vertical'
            # Ready for some intense list building?
            self.positions = [[self.positions[0][0] + 3, self.positions[0][1] - 3],
                              [self.positions[1][0] + 2, self.positions[1][1] - 2],
                              [self.positions[2][0] + 1, self.positions[2][1] - 1],
                              [self.positions[3][0], self.positions[3][1]]]
            # Okay actually that wasn't so intense lol

    def update_positions(self):
        for x in range(0, len(self.positions)):
            if self.falling:
                self.positions[x][1] += 1

    def undo_update(self):
        for x in range(0, len(self.positions)):
            self.positions[x][1] -= 1


"""
Game related class objects
"""


# Class for the text box that will hold the score
class ScoreBox:
    # __init__
    def __init__(self, master):
        # Text() object
        self.score_box = Text(master, width=100, height=425)
        # Place self.score_box on the right of the window
        self.score_box.grid(row=0, column=1, sticky=N+S+E)
        # Set state to disabled so that its read-only
        self.score_box.config(state='disabled')

    # Method to update the Text() object with new text
    def update(self, new_text):
        # Set state to normal, so the Text() object can be edited
        self.score_box.config(state='normal')
        # Delete the text in the text box
        self.score_box.delete("1.0", 'end-1c')
        # Insert the new text
        self.score_box.insert('1.0', new_text)
        # Reset the state to disabled, once again making the box read-only
        self.score_box.config(state='disabled')


# Class for the text box containing the game view
class GameBox:
    # __init__
    def __init__(self, master):
        # Text() object
        self.game_box = Text(master,  width=110, height=425)
        # Place self.game_box on the left side of the window
        self.game_box.grid(row=0, column=0, sticky=N+S+W)
        # Set state to disabled, so that its read-only
        self.game_box.config(state='disabled')

    # Method to update the Text() object with new text
    def update(self, new_text):
        # Set state to normal, so it can be edited
        self.game_box.config(state='normal')
        # Delete the current text
        self.game_box.delete("1.0", "end-1c")
        # Insert the new text
        self.game_box.insert("1.0", new_text)
        # Reset the Text() object to disabled, so that its read-only
        self.game_box.config(state='disabled')


# Main application class
class Application:
    # __init__
    def __init__(self):
        # Create the window object
        self.root = Tk()
        # Give column 0 and 1a non-0 weight value, so the sticky parameter has an effect
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)  # Also give row 0 a non-0 weight value
        self.root.title("Tetris")  # Set the title of the window
        self.root.geometry("320x425")  # Set the size of the window
        self.root.resizable(width=False, height=False)  # Make the window non-resizeable

        self.score = 0  # Define the score variable
        self.lines_cleared = 0  # Define the lines_cleared variable

        self.root.bind("<Key>", self.action_listener)  # Bind <Key> events to self.action_listener

        self.game_box = GameBox(self.root)  # Create the GameBox object
        self.score_box = ScoreBox(self.root)  # Create the ScoreBox object

        self.shapes = []  # Define the list of shapes

        self.add_shape()  # Add a shape to the list

        self.playing = True  # While self.playing == True, the game loop will run
        self.interval = 250  # Define the interval between updates (ms)

        self.root.after(0, self.build_display)  # Start the game loop

    # Method to add a new shape to the list
    def add_shape(self):
        available = [Line(self.game_box),
                     Square(self.game_box),
                     Pyramid(self.game_box),
                     L(self.game_box)]
        self.shapes.append(random.choice(available))

    # Method to update all shapes where shape.falling == True
    def update_falling(self):
        is_shape_active = False

        # Iterate over the list of shapes
        for shape_num in range(0, len(self.shapes)):
            in_contact_with_shape = False
            # Update the positions of the shape
            self.shapes[shape_num].update_positions()
            # Iterate over the list again to check for contact
            for x in range(0, len(self.shapes)):
                if x != shape_num:  # Excluding the current shape
                    # Check for identical positions
                    for position in self.shapes[x].positions:
                        if position in self.shapes[shape_num].positions and self.shapes[shape_num].falling:
                            in_contact_with_shape = True
                            self.shapes[shape_num].undo_update()
                            self.shapes[shape_num].falling = False

            # Boundary check
            for x in range(0, len(self.shapes[shape_num].positions)):
                if self.shapes[shape_num].positions[x][1] == 31:
                    self.shapes[shape_num].undo_update()
                    self.shapes[shape_num].falling = False

            if self.shapes[shape_num].falling and not in_contact_with_shape:
                is_shape_active = True

    # Method to build the window display, also the game loop
    def build_display(self):
        # Create the basic display
        display = []
        for y in range(0, 32):
            display.append([])
            for x in range(0, 22):
                if y == 31:
                    display[y].append("-")
                    continue

                if x == 21:
                    display[y].append("|")
                    continue

                display[y].append(" ")

        # Add the shapes to the display
        shape_num = 0
        for shape in self.shapes:
            for x in range(0, len(shape.positions)):
                display[shape.positions[x][1]][shape.positions[x][0]] = shape.body_types[shape.rotation][x]

            print(shape_num, shape.positions)
            shape_num += 1

        # Create a string from the list of lists that the display currently is
        # But also store the display as a list in a separate variable
        display_list = display

        d = ""
        for x in range(0, len(display)):
            d += "".join(display[x])
            d += "\n"

        display = d
        # Update the game_box
        self.game_box.update(display)
        # Update the falling shapes
        self.update_falling()
        # Check if any shapes are falling
        is_falling = False
        for shape in self.shapes:
            if shape.falling:
                is_falling = True

        # If no shapes are falling, check for complete lines and add a new shape
        if not is_falling:
            self.check_line_complete(display_list)
            self.add_shape()

        # Create the display for the score_box
        score_text = """
TETRIS

Score: {}
Level: {}
Lines cleared: {}
""".format(self.score, self.lines_cleared // 10, self.lines_cleared)
        self.score_box.update(score_text)  # Update the score_box
        # If the player has not lost, and they are still playing, continue the loop
        if not self.lost() and self.playing:
            self.root.after(self.interval, self.build_display)

        else:
            # else show the game over message
            self.build_lose_display()

    # action_listener method
    def action_listener(self, event):
        # rotate active shape
        if event.char == "w":
            for shape in self.shapes:
                if shape.falling:
                    shape.toggle_rotation()

        # Move active shape right
        elif event.char == 'd':
            for shape in self.shapes:
                if shape.falling:
                    contact_with_wall = False
                    for position_index in range(0, len(shape.positions)):
                        if shape.positions[position_index][0] == 20:
                            contact_with_wall = True

                    for position_index in range(0, len(shape.positions)):
                        if not contact_with_wall:
                            shape.positions[position_index][0] += 1

        # Move active shape left
        elif event.char == 'a':
            for shape in self.shapes:
                if shape.falling:
                    contact_with_wall = False
                    for position_index in range(0, len(shape.positions)):
                        if shape.positions[position_index][0] == 0:
                            contact_with_wall = True

                    for position_index in range(0, len(shape.positions)):
                        if not contact_with_wall:
                            shape.positions[position_index][0] -= 1

    # Method to check for any complet lines
    def check_line_complete(self, display):
        complete_line = ["=" for x in range(0, 21)]
        complete_line.append("|")
        original_lines_completed = self.lines_cleared
        new_lines_completed = 0
        for y in range(len(display) - 1, 0, -1):
            if display[y] == complete_line:
                print("Line {} complete".format(y))
                new_lines_completed += 1
                for shape_num in range(0, len(self.shapes)):
                    self.shapes[shape_num].positions = [x for x in self.shapes[shape_num].positions if y not in x]

                # Update scoring system
                level = self.lines_cleared // 10
                score_to_add = 40
                for x in range(0, level):
                    score_to_add += 40

                self.score += score_to_add

                self.lines_cleared += 1

        # If the original lines completed is different from the new lines completed + original lines completed
        # then update all the inactive shapes (which should be all of them)
        if original_lines_completed != new_lines_completed + original_lines_completed:
            for shape_num in range(0, len(self.shapes)):
                for position_index in range(0, len(self.shapes[shape_num].positions)):
                    if not self.shapes[shape_num].falling:
                        self.shapes[shape_num].positions[position_index][1] += (new_lines_completed + original_lines_completed) - original_lines_completed

    # Method to check if the player has lost
    def lost(self):
        for shape in self.shapes:
            if not shape.falling:
                for position_index in range(0, len(shape.positions)):
                    if shape.positions[position_index][1] == 0:
                        return True

        return False

    # Show a game over message and stop the game loop
    def build_lose_display(self):
        messagebox.showinfo("GAME OVER", "Game over!")
        self.playing = False


"""
Main game loop
"""


# Start the game
if __name__ == "__main__":
    app = Application()  # Create an Application() object
    app.root.mainloop()  # Start the mainloop

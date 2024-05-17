from builtins import print
from builtins import str
from builtins import int
from builtins import range
from tkinter import *
root = Tk()

grid_color = '#1daec4'
red_color = '#e60b0b'
yellow_color = '#cfc50c'
screen_width = 420
screen_height = 420


screen = Canvas(root, width=screen_width, height=screen_height, bg=grid_color)
screen.pack
diameter = screen_width / 7 



grid = [
    ["-", "-", "-", "-", "-", "-", "-"],     # [R0C0, ..., R0C6]
    ["-", "-", "-", "-", "-", "-", "-"],     # [R1C0, ..., R1C6]
    ["-", "-", "-", "-", "-", "-", "-"],     # [R2C0, ..., R2C6]
    ["-", "-", "-", "-", "-", "-", "-"],     # [R3C0, ..., R3C6]
    ["-", "-", "-", "-", "-", "-", "-"],     # [R4C0, ..., R4C6]
    ["-", "-", "-", "-", "-", "-", "-"]      # [R5C0, ..., R5C6]
]

current_piece = "R"

last_row = -1
last_col = -1
remaining_spots = 42

def print_grid():
    for row in range(total_row): # type: ignore
        for col in range(total_cols): # type: ignore
            x_start = x_start * col
            y_start = y_start * col
            x_end = x_start * diameter
            y_end = y_start * diameter
            screen.create_oval(x_start, y_start, x_end, y_end, fill="#ffffff")
    pass
    print()
    
    for row in range(6):
        for col in range(7):
            if col != 6:
                print(grid[row][col], end="  ")            
            else:
                print(grid[row][col])
                print()

def is_bad_num_string(choice : str):
    if (choice.isnumeric() and int(choice) >= 0 and int(choice) <= 6):
        return False
    return True
                
def is_bad_choice(choice : str):
    if(choice.__eq__("STOP")):
        return False
    return is_bad_num_string(choice)

def place_piece(col : int):
    global last_row
    global last_col
    global remaining_spots
    while(True):
        row = 5
        while(row >= 0):
            if grid[row][col].__eq__("-"):
                grid[row][col] = current_piece    
                last_row = row
                last_col = col
                remaining_spots -= 1
                break
            else:
                row -= 1
        if row != -1:
            break
        else:
            user_choice = ""
            while (is_bad_num_string(user_choice)):
                user_choice = input("Enter a different number (0-6) where to drop the piece: ")
            col = int(user_choice)   

def check_row():
    first_list = [last_col, last_col + 1, last_col + 2, last_col + 3]
    second_list = [last_col - 1, last_col, last_col + 1, last_col + 2]
    third_list = [last_col - 2, last_col - 1, last_col, last_col + 1]
    fourth_list = [last_col - 3, last_col - 2, last_col - 1, last_col]
    
    if(first_list[0] >= 0 and first_list[0] < 7 and first_list[3] >=0 and first_list[3] < 7):
        one = grid[last_row][first_list[0]]
        two = grid[last_row][first_list[1]]
        three = grid[last_row][first_list[2]]
        fourth = grid[last_row][first_list[3]]
        if (one.__eq__(two) and two.__eq__(three) and three.__eq__(fourth)):
            return True
    if (second_list[0] >= 0 and second_list[0] < 7 and second_list[3] >= 0 and second_list[3] < 7):
        one = grid[last_row][second_list[0]]
        two = grid[last_row][second_list[1]]
        three = grid[last_row][second_list[2]]
        fourth = grid[last_row][second_list[3]]
        if (one.__eq__(two) and two.__eq__(three) and three.__eq__(fourth)):
            return True
    if (third_list[0] >= 0 and third_list[0] < 7 and third_list[3] >= 0 and third_list[3] < 7):
        one = grid[last_row][third_list[0]]
        two = grid[last_row][third_list[1]]
        three = grid[last_row][third_list[2]]
        fourth = grid[last_row][third_list[3]]
        if (one.__eq__(two) and two.__eq__(three) and three.__eq__(fourth)):
            return True
    if (fourth_list[0] >= 0 and fourth_list[0] < 7 and fourth_list[3] >= 0 and fourth_list[3] < 7):
        one = grid[last_row][fourth_list[0]]
        two = grid[last_row][fourth_list[1]]
        three = grid[last_row][fourth_list[2]]
        fourth = grid[last_row][fourth_list[3]]
        if (one.__eq__(two) and two.__eq__(three) and three.__eq__(fourth)):
            return True
    return False
    
 
def check_col():
    return False

def check_left_diag():
    return False #Actually Implement

def check_right_diag():
    return False  # Actually Implement

def check_draw():
    return remaining_spots == 0

def check_game_over():
    if check_row():
        print(current_piece + " wins!")
        return True
    elif check_col():
        print(current_piece + " wins!")
        return True
    elif check_left_diag():
        print(current_piece + " wins!")
        return True
    elif check_right_diag():
        print(current_piece + " wins!")
        return True
    elif check_draw():
        print("The Game Ends in a Draw!")
        return True
    else:
        return False

def game_loop():
    global current_piece
    print("Welcome to CONNECT FOUR")
    user_choice = ""
    while(True):
        print_grid()
        while(is_bad_choice(user_choice)):
            user_choice = input("Enter STOP to end.  Or a number (0-6) where to drop the piece: ")
        if user_choice.__eq__("STOP"):
            break
        column = int(user_choice)
        place_piece(column)
        if(check_game_over()):
            print_grid()
            break
        current_piece = "Y" if current_piece.__eq__("R") else "R"
        user_choice = ""
    print("GAME OVER")
        
game_loop()
mainloop()
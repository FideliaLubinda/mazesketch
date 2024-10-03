import tkinter as tk
from tkinter import ttk
import random
import heapq

# Maze and game setup
maze = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,],
    [1,0,1,1,0,1,0,1,1,0,1,0,1,0,0,0,1,1,1,1,1,0,1,1,1,0,0,1,0,1,1,1,1,0,1,1,1,0,0,0,1,],
    [1,0,1,1,0,1,0,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,1,0,1,1,1,],
    [1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,0,0,1,],
    [1,0,1,1,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,1,1,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,1,1,0,1,],
    [1,0,1,0,0,0,1,0,1,1,1,0,0,1,1,1,1,1,1,1,0,1,0,0,0,0,0,1,0,1,1,1,0,1,1,1,1,0,0,0,1,],
    [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,],
    [1,0,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,1,1,0,0,1,1,1,0,0,1,],
    [1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,1,],
    [1,0,1,0,0,0,0,1,0,0,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0,1,0,0,0,0,1,1,0,1,1,1,1,0,1,1,1,],
    [1,0,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0,0,1,0,1,],
    [1,0,1,0,1,0,1,0,0,0,0,0,0,1,0,1,1,1,1,1,0,0,1,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,1,0,1,],
    [1,0,0,0,1,0,1,1,1,1,0,1,0,1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,],
    [1,0,1,0,1,1,1,0,0,1,1,1,0,1,0,1,0,1,1,1,0,0,0,0,1,1,1,0,0,1,1,0,1,0,0,0,0,0,1,0,1,],
    [1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,0,1,0,0,1,1,1,1,1,0,1,0,1,],
    [1,0,1,0,1,1,1,1,0,0,1,1,0,0,1,1,1,0,1,0,1,0,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,1,0,1,],
    [1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,1,1,1,0,0,1,0,0,0,1,],
    [1,0,1,0,1,0,1,0,1,0,0,1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,],
    [1,0,1,1,1,0,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,1,1,1,0,0,1,1,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0,0,1,],
    [1,1,1,1,1,0,0,1,1,1,0,1,1,1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,1,1,0,0,0,1,],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
]

player_x, player_y = 1, 1
ai_x, ai_y = 3, 3
cell_size = 30
ai_speed = 400

# Heuristic function (Manhattan distance)
def heuristic(a, b):            
    
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* search to find the shortest path
def a_star(start, goal, maze):
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_list:
        current = heapq.heappop(open_list)[1]
        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in get_neighbors(current, maze):
            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return []

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    total_path.reverse()
    return total_path

def get_neighbors(position, maze):
    x, y = position
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(maze) and 0 <= nx < len(maze[0]) and maze[ny][nx] == 0:
            neighbors.append((nx, ny))
    return neighbors

# Function to move the player
def move_player(dx, dy):
    global player_x, player_y
    new_x = player_x + dx
    new_y = player_y + dy
    if maze[new_y][new_x] == 0:
        player_x, player_y = new_x, new_y
        check_collision()
        draw_maze()

# Move AI using A*
def move_ai():
    global ai_x, ai_y
    path = a_star((ai_x, ai_y), (player_x, player_y), maze)
    if len(path) > 1:
        ai_x, ai_y = path[1]
    check_collision()
    draw_maze()
    root.after(ai_speed, move_ai)

# Check if AI catches the player
def check_collision():
    if player_x == ai_x and player_y == ai_y:
        print("AI caught the player!")

# Draw the maze, player, and AI
def draw_maze():
    canvas.delete("all")
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            color = "white" if maze[y][x] == 0 else "black"
            canvas.create_rectangle(x * cell_size, y * cell_size, (x + 1) * cell_size, (y + 1) * cell_size, fill=color)
    canvas.create_oval(player_x * cell_size, player_y * cell_size, (player_x + 1) * cell_size, (player_y + 1) * cell_size, fill="red")
    canvas.create_oval(ai_x * cell_size, ai_y * cell_size, (ai_x + 1) * cell_size, (ai_y + 1) * cell_size, fill="blue")

# Handle player movement
def handle_key(event):
    if event.keysym == "Up":
        move_player(0, -1)
    elif event.keysym == "Down":
        move_player(0, 1)
    elif event.keysym == "Left":
        move_player(-1, 0)
    elif event.keysym == "Right":
        move_player(1, 0)

# Set up the game window
root = tk.Tk()
root.title("Maze Game with A* Pathfinding AI")

canvas = tk.Canvas(root, width=cell_size * len(maze[0]), height=cell_size * len(maze))
canvas.pack()

root.bind("<Up>", handle_key)
root.bind("<Down>", handle_key)
root.bind("<Left>", handle_key)
root.bind("<Right>", handle_key)

draw_maze()
move_ai()

root.mainloop()

import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    eraser_coords = canvas.coords(eraser)
    overlapping = canvas.find_overlapping(*eraser_coords)
    
    for obj in overlapping:
        if obj != eraser:
            canvas.itemconfig(obj, fill='white')

def on_mouse_move(event):
    canvas.coords(eraser, event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
    erase_objects(canvas, eraser)

root = tk.Tk()
root.title("Eraser Canvas")
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
canvas.pack()

for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
    for col in range(0, CANVAS_WIDTH, CELL_SIZE):
        canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill='blue')

root.update()
root.bind("<Button-1>", lambda event: start_eraser(event))

def start_eraser(event):
    global eraser
    eraser = canvas.create_rectangle(event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE, fill='pink')
    canvas.bind("<Motion>", on_mouse_move)  # Bind mouse movement to eraser function

root.mainloop()

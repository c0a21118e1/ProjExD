import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm


def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""

def main_proc():
    global key, cx, cy
    if key == "Up":
        cy -= 20
    if key == "Down":
        cy += 20
    if key == "Left":
        cx -= 20
    if key == "Right":
        cx += 20
    
    canvas.coords("tori", cx, cy)
    root.after(100, main_proc)




if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    maze_bg = mm.make_maze(15, 9)
    print(maze_bg)
    mm.show_maze(canvas, maze_bg)
    canvas.pack()
    tori = tk.PhotoImage(file="ex03/fig/5.png")
    cx, cy = 300, 400
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    canvas.create_image(cx, cy, image=tori, tag="tori")
    main_proc()
    
    
    canvas.mainloop()


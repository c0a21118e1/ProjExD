import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm
from random import randint

def key_down(event):
    global key
    key = event.keysym #押されたキーに更新


            


def key_up(event):
    global key
    key = "" #キーが離されたときにキーを更新


def main_proc():
    global key, cx, cy, mx, my
    
    if maze_bg[my-1][mx] == 0:
        if key == "Up": #上キーが押されたときにマスを１だけ上に更新
            my -= 1
    if maze_bg[my+1][mx] == 0:
        if key == "Down": #下キーが押されたときにマスを１だけ下に更新
            my += 1
    if maze_bg[my][mx-1] == 0:
        if key == "Left": #左キーが押されたときにマスを１だけ左に更新
            mx -= 1
    if maze_bg[my][mx+1] == 0:
        if key == "Right": #右キーが押されたときにマスを１だけ右に更新
            mx += 1
    cx, cy = mx*100+50, my*100+50 #こうかとんの図表を現在いるマスから計算
    canvas.coords("tori", cx, cy) #こうかとんの位置を更新
    
    
    if mx == 13 and my == 7:
        canvas.create_text(500,500, text="おめでとう", font = ("HG丸ゴシックM-PRO",80),fill ="red")
    root.after(100, main_proc)




if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    maze_bg = mm.make_maze(15, 9) #迷路を作成
    print(maze_bg)
    mm.show_maze(canvas, maze_bg) #迷路を描画
    goal = 14, 7
    canvas.pack()
    tori = tk.PhotoImage(file="ex03/fig/5.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    key = ""
    canvas.create_text(cx,cy, text="start", font = ("HG丸ゴシックM-PRO",20))
    canvas.create_text(13*100+50,7*100+50, text="goal", font = ("HG丸ゴシックM-PRO",20))
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    canvas.create_image(cx, cy, image=tori, tag="tori")
    main_proc()
    label = tk.Label(root, text="おめでとう",font=("Ricty Diminished", 40))
    
    canvas.mainloop()


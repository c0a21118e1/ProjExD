from cmath import e
from re import X
import pygame as pg
import sys
import random
import tkinter as tk
import tkinter.messagebox as tkm
def main():
    # 練習１
    root = tk.Tk()
    root.geometry("1x1")
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900)) # Suface
    screen_rct = screen_sfc.get_rect() # Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg") # Suface
    bgimg_rct = bgimg_sfc.get_rect()   # Rect
    screen_sfc.blit(bgimg_sfc, bgimg_rct)

    clock.tick(0.5)
    # 練習３
    kkimg_sfc = pg.image.load("fig/6.png") # Surface
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0) # Surface
    kkimg_rct = kkimg_sfc.get_rect() # Rect
    kkimg_rct.center = 900, 400

    # 練習５
    bmimg_sfc = pg.Surface((20, 20)) # Surface
    bmimg_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bmimg_sfc, (255, 0, 0), (10, 10), 10) 
    bmimg_rct = bmimg_sfc.get_rect()
    bmimg_rct.centerx = random.randint(0, screen_rct.width)
    bmimg_rct.centery = random.randint(0, screen_rct.height)
    vx, vy = +1, +1 # 練習6

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)
    
   
        # 練習２
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        # 練習4
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP] == True: kkimg_rct.centery -= 1 # y座標を-1
        if key_states[pg.K_DOWN] == True: kkimg_rct.centery += 1 # y座標を-1
        if key_states[pg.K_LEFT] == True: kkimg_rct.centerx -= 1 # y座標を-1
        if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx += 1# y座標を-1
        # 練習7
        if check_bound(kkimg_rct, screen_rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP] == True: kkimg_rct.centery += 1 # y座標を-1
            if key_states[pg.K_DOWN] == True: kkimg_rct.centery -= 1 # y座標を-1
            if key_states[pg.K_LEFT] == True: kkimg_rct.centerx += 1 # y座標を-1
            if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx -= 1# y座標を-1
        screen_sfc.blit(kkimg_sfc, kkimg_rct)

        # 練習6
        bmimg_rct.move_ip(vx, vy)

        # 練習5
        screen_sfc.blit(bmimg_sfc, bmimg_rct)

        # 練習7
        yoko, tate = check_bound(bmimg_rct, screen_rct)

        vx *= yoko
        vy *= tate
        
        # 追加機能 時間がたつとボールが速くなる
        if pg.time.get_ticks() % 1000 == 0: # 追加機能 時間がたつとボールが速くなる
            if vx < 0:
                vx -= 1
            else:
                vx += 1
            if vy < 0:
                vy -= 1
            else:
                vy += 1
            pg.draw.circle(bmimg_sfc, (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)), (10, 10), 10)
        if kkimg_rct.colliderect(bmimg_rct):
            
            kkimg_sfc = pg.image.load("fig/11.png") # 追加機能　鶏の丸焼きを表示
            kkimg_rct = kkimg_sfc.get_rect()
            #kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, )
            kkimg_rct.center = kkimg_rct.centerx, kkimg_rct.centery

            screen_sfc.blit(kkimg_sfc, kkimg_rct)
            


            pg.display.update()
            clock.tick(1000)
            tkm.showwarning("警告", "こうかとんは安らかに眠りました")  # 追加機能　爆弾とぶつかったらウィンドを表示
            
            return
        pg.display.update()
        clock.tick(1000)
# 練習7
def check_bound(rct, scr_rct):
    '''
    [1] rct:こうかとん　or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1
    if rct.left < scr_rct.left or scr_rct.right < rct.right: yoko = -1 # 領域外
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate


if __name__ == "__main__":
    pg.init() #モジュールを初期化
    main() #これから実装するゲームのメインの部分
    pg.quit()
    sys.exit()

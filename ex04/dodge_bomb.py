import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900)) # Suface
    screen_rect = screen_sfc.get_rect() # Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg") # Suface
    bgimg_rct = bgimg_sfc.get_rect()   # Rect
    screen_sfc.blit(bgimg_sfc, bgimg_rct)




if __name__ == "__main__":
    pg.init() #モジュールを初期化
    main() #これから実装するゲームのメインの部分
    pg.quit()
    sys.exit()
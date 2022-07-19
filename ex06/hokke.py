from tkinter import Y
import pygame as pg
import sys
import random

def bgm():
    # 音楽ファイルの読み込み
    pg.mixer.music.load("./fig/Floor_Beast.mp3") 
    pg.mixer.music.play(loops=-1, start=0.0)#ロードした音楽の再生

class Screen:
    def __init__(self, title, wh):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     # Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.Surface((1600, 900))    # Surface
        pg.draw.rect(self.bgi_sfc, (0, 0, 0), (0, 0, 1600, 900)) # 背景を黒に塗りつぶし
        pg.draw.rect(self.bgi_sfc, (0, 255, 255), (790, 0, 50, 900)) # 真ん中の水色の線を作成
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect
       
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) # スクリーンに描画
        
    
class Kabe: # 右側のプレイヤーを作成する関数
    def __init__(self, color, size):  #scr: Screen):
        self.sfc = pg.Surface((size, 4*size))
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.rect(self.sfc, color, (0, 0, size, 4*size))
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = 1550
        self.rct.centery = 400
        
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]: # 上キーを押すと上に移動
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]: # 下キーを押すと下に移動
            self.rct.centery += 1
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]:  
                self.rct.centery += 1
            if key_states[pg.K_DOWN]: 
                self.rct.centery -= 1
        self.blit(scr)


class Kabe2: # 左側のプレイヤーを作成する関数
    def __init__(self, color, size):  
        self.sfc = pg.Surface((size, 4*size))
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.rect(self.sfc, color, (0, 0, size, 4*size))
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = 50
        self.rct.centery = 400
        
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_w]: # wを押すと上に移動
            self.rct.centery -= 1
        if key_states[pg.K_s]: # sを押すと下に移動
            self.rct.centery += 1
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_w]: 
                self.rct.centery += 1
            if key_states[pg.K_s]: 
                self.rct.centery -= 1
        self.blit(scr)


class Score: # スコアを描画する関数
    def __init__(self, score1, score2):
        self.s1 = score1
        self.s2 = score2
        self.fscore1 = pg.font.Font(None, 80)
        self.tscore1 = self.fscore1.render(str(self.s1), True, (255, 255, 255)) # 右側のプレイヤーのスコア
        self.fscore2 = pg.font.Font(None, 80)
        self.tscore2 = self.fscore2.render(str(self.s2), True, (255, 255, 255)) # 左側のプレイヤーのスコア
    def blit(self, scr: Screen):
        scr.sfc.blit(self.tscore1, (750, 20))
        scr.sfc.blit(self.tscore2, (850, 20))

    def update(self, scr: Screen, bk):
        if bk.centerx > 800: # 左側のプレイヤーの点数を更新
            self.s1 += 1
        else: # 右側のプレイヤーの点数を更新
            self.s2 += 1
        self.tscore1 = self.fscore1.render(str(self.s1), True, (255, 255, 255))
        self.tscore2 = self.fscore2.render(str(self.s2), True, (255, 255, 255))
        self.blit(scr)


class Ball: # ボールを描画する関数
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(40, scr.rct.width)
        self.rct.centery = random.randint(40, scr.rct.height)
        self.vx, self.vy = vxy 

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate   
        self.blit(scr)          

class Bar:
    def __init__(self,image:str,size:float,xy):#中央障害物画像用のSurface
        self.sfc=pg.image.load(image)
        self.sfc= pg.transform.rotozoom(self.sfc,0,size)
        self.rct=self.sfc.get_rect()                   #中央障害物画像用のRect
        self.rct.center=xy                        #中央障害物画像の中心座標を設定する

    def blit(self,scr :Screen):
        scr.sfc.blit(self.sfc, self.rct) #中央障害物画像の更新

    def update(self, scr: Screen): #更新
        self.blit(scr)

def main():
    clock = pg.time.Clock()
    scr = Screen("ホッケーゲーム", (1600, 900))
    bkd = Ball((255,0,0), 25, (+3,+2), scr)
    bar = Bar("fig/line.jpg",0.225, (800, 450))
    kb = Kabe((0, 0, 255), 50)
    kb2 = Kabe2((0, 255, 0), 50)
    sc = Score(0, 0)

    while True:
        scr.blit()
        sc.blit(scr)
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        kb.update(scr)
        kb2.update(scr)
        if bkd.rct.centerx < 25 or bkd.rct.centerx > 1600 - 25: 
            sc.update(scr, bkd.rct)
        bkd.update(scr)
        if bkd.rct.colliderect(kb.rct): # ボールと右側のプレイヤーが当たったらボールが反射する
            bkd.vx *= -1
        if bkd.rct.colliderect(kb2.rct): # ボールと左側のプレイヤーが当たったらボールが反射する
            bkd.vx *= -1
        if sc.s1 == 5 and sc.s2 < 4 or sc.s2 == 5 and sc.s1 < 4: # どちらかが5点取ったらゲーム終了
            return
        elif sc.s1 >= 4 and sc.s2 >= 4: # デュースの場合、2点差がついたらゲーム終了
            if abs(sc.s1 - sc.s2) == 2:
                return
        if bar.rct.colliderect(kb.rct): #衝突処理
            kb*=-1
        bar.update(scr)
                
        pg.display.update()
        clock.tick(1000)


def check_bound(rct, scr_rct): 
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right :
        yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate


if __name__ == "__main__":
    pg.init()
    bgm()
    main()
    pg.quit()
    sys.exit()

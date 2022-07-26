from tkinter import Y
import pygame as pg
import sys
import random
from pygame import mixer #荒井担当分
import tkinter.messagebox as tkm #荒井担当分

count1,count2=0,0 #荒井担当分

def bgm(): #林担当分
    # 音楽ファイルの読み込み
    pg.mixer.music.load("fig/Floor_Beast.mp3") 
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
    def __init__(self ,image,size,xy):  #scr: Screen):
        self.sfc=pg.image.load(image)#画像を取得
        self.sfc=pg.transform.rotozoom(self.sfc, 0, size)#1/4倍にズーム
        self.rct=self.sfc.get_rect()
        self.rct.center=xy #位置を設定
        
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


class Kabe2: # 左側のプレイヤーを作成する関数
    def __init__(self ,image,size,xy):  
        self.sfc=pg.image.load(image)#画像を取得
        self.sfc=pg.transform.rotozoom(self.sfc, 0, size)#1/4倍にズーム
        self.rct=self.sfc.get_rect()
        self.rct.center=xy #位置を設定
        
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


class Score: # スコアを描画する関数
    def __init__(self, score1, score2):
        self.s1 = score1
        self.s2 = score2
        self.fscore1 = pg.font.Font("fig/font.ttf", 80) #中野担当分　フォントの追加
        self.tscore1 = self.fscore1.render(str(self.s1), True, (255, 255, 255)) # 右側のプレイヤーのスコア
        self.fscore2 = pg.font.Font("fig/font.ttf", 80)
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


class Bird: #本田担当分 障害物として存在するこうかとん
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP] or key_states[pg.K_w]: 
            self.rct.centery -= 1
        if key_states[pg.K_DOWN] or key_states[pg.K_s]: 
            self.rct.centery += 1
        # if key_states[pg.K_LEFT]: 
        #     self.rct.centerx -= 1
        # if key_states[pg.K_RIGHT]: 
        #     self.rct.centerx += 1
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]: 
                self.rct.centery += 1
            if key_states[pg.K_DOWN]: 
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]: 
                 self.rct.centerx += 1
            if key_states[pg.K_RIGHT]: 
                 self.rct.centerx -= 1
        self.blit(scr)


class Ball: # ボールを描画する関数
    def __init__(self, image, vxy, scr: Screen):
        self.sfc = pg.image.load(image) # Surface
        self.sfc=pg.transform.rotozoom(self.sfc, 0, 0.5)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = 800#出現位置のx座標を中心に
        self.rct.centery = 450#出現位置のy座標を中心に
        self.vx, self.vy = vxy 

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate   
        self.blit(scr)   


class Obstacle: #荒井担当分
    def __init__(self,image):
        self.sfc=pg.image.load(image)#画像を取得
        self.sfc=pg.transform.rotozoom(self.sfc, 0, 0.25)#1/4倍にズーム
        self.rct=self.sfc.get_rect()
        self.rct.center=random.randint(500,1100),random.randint(100,800) #位置を設定

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)    


class End: #荒井担当分
    def __init__(self):
        mixer.init()#初期化
        mixer.music.load("fig/poka.mp3")#音声ファイルの呼び出し
        mixer.music.play(1)#再生回数   


class Word: #荒井担当分
    def __init__(self ,title, text):
        tkm.showwarning(title,text)#終了時のテキストを表示

class Bar: #林担当分
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
    bkd = Ball("fig/ball.png", (+3,+3), scr)
    kb = Kabe("fig/line1.png",0.75,(50,450))
    kb2 = Kabe2("fig/line2.png",0.75,(1550,450))
    
    #障害物 荒井担当分
    obs=[]
    for i in range(3): #障害物を３つ生成（荒井）
        obs.append(Obstacle("fig/障害物.png"))
    kkt = Bird("fig/6.png", 2.0, (900, 400))
    # bar = Bar("fig/line.jpg",0.225, (800, 450)) #林担当分
    sc = Score(0, 0)

    while True:
        scr.blit()
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        kb.update(scr)
        kb2.update(scr)
        if pg.time.get_ticks() % 1000 == 0: # 追加機能 時間がたつとボールが速くなる　新山担当分
            if bkd.vx < 0:
                bkd.vx -= 0.4
            else:
                bkd.vx += 0.4
            if bkd.vy < 0:
                bkd.vy -= 0.4
            else:
                bkd.vy += 0.4
        bkd.update(scr)
        kkt.update(scr)
        if bkd.rct.colliderect(kb.rct): # ボールと右側のプレイヤーが当たったらボールが反射する
            bkd.vx *= -1
        if bkd.rct.colliderect(kb2.rct): # ボールと左側のプレイヤーが当たったらボールが反射する
            bkd.vx *= -1
        if count1 == 5 and count2 < 4 or count2 == 5 and count1 < 4: # どちらかが5点取ったらゲーム終了
            Word("ゲームセット","お疲れ様")#ゲームセット文の表示 #荒井担当分
            return
        elif count1 >= 4 and count2 >= 4: # デュースの場合、2点差がついたらゲーム終了
            if abs(count1 - count2) == 2:
                Word("ゲームセット","お疲れ様")#ゲームセット文の表示 #荒井担当分
                return
        for i in obs:
            i.blit(scr)
            if i.rct.colliderect(bkd.rct):
                bkd.vx*=-1
#得点表示　#荒井担当分
        font = pg.font.Font(None,100)
        text = font.render(f"{count2}:{count1}", True, (255,255,255))#得点を表示
        scr.sfc.blit(text, [750, 50])#得点を表示
        if kkt.rct.colliderect(bkd.rct):
            bkd.vx *= -1
        # 中野担当分
        if sc.s1 == 5 and sc.s2 < 4: # どちらかが5点取ったらゲーム終了
            pg.mixer.music.stop() # BGMがとまる
            pg.mixer.music.load("ex06/fig/レベルアップ.mp3") # 効果音が鳴る
            pg.mixer.music.play(1)
            tkm.showinfo("Game Clear", "Player1 Win!!")
            return
        elif sc.s2 == 5 and sc.s1 < 4:
            pg.mixer.music.stop() # BGMがとまる
            pg.mixer.music.load("ex06/fig/レベルアップ.mp3")# 効果音が鳴る
            pg.mixer.music.play(1)
            tkm.showinfo("Game Clear", "Player2 Win!!")
            return       
        elif sc.s1 >= 4 and sc.s2 >= 4: # デュースの場合、2点差がついたらゲーム終了
            if abs(sc.s1 - sc.s2) == 2:
                return

                
        pg.display.update()
        clock.tick(1000)


def check_bound(rct, scr_rct): 
    global count1, count2
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left :
        yoko = -1 # 領域外
        count1+=1#得点を加算
    if scr_rct.right  < rct.right :
        yoko = -1 # 領域外
        count2+=1#得点を加算
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate


if __name__ == "__main__":
    pg.init()
    bgm()
    main()
    pg.quit()
    sys.exit()
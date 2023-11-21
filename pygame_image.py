import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg") #練習1 背景画像Surfaceの生成
    
    kk_img = pg.image.load("ex01/fig/3.png") #練習2 こうかとん画像Surfaceの生成
    kk_img = pg.transform.flip(kk_img,True,False) #練習2 左右反転
    kk_imgs = [kk_img, pg.transform.rotozoom(kk_img, 10, 1.0)] #練習3 こうかとん10°回転

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        #screen.blit(bg_img, [0, 0]) #練習4 背景画像の表示
        x=tmr%1600
        screen.blit(bg_img, [-x, 0]) #練習4 背景画像の表示
        screen.blit(bg_img, [1600-x, 0])
        #screen.blit(kk_imgs[1],[300,200]) #こうかとんの表示
        screen.blit(kk_imgs[tmr%2],[300,200]) #練習5 10°回転したこうかとんの表示 %2で0か1の動き
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
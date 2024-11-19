import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    ko_img = pg.image.load("fig/3.png")
    ko_img = pg.transform.flip(ko_img,True,False)
    tmr = 0
    back_x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        back_x = (back_x - 2 ) % 1600

        screen.blit(bg_img, [back_x, 0])
        screen.blit(bg_img, [back_x - 1600, 0])
        screen.blit(ko_img,[300,200])
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
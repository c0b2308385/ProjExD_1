import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)
    ko_img = pg.image.load("fig/3.png")
    ko_img = pg.transform.flip(ko_img,True,False)
    tmr = 0
    back_x = 0
    ko_rct = ko_img.get_rect()
    ko_rct.center = 300, 200
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        back_x = -(tmr%3200)

        move_x = 0
        move_y = 0
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            move_y -= 1
        elif key_lst[pg.K_DOWN]:
            move_y += 1
        elif key_lst[pg.K_LEFT]:
            move_x -= 1
        elif key_lst[pg.K_RIGHT]:
            move_x += 1
        else:
            move_x -= 1
        
        ko_rct.move_ip(move_x,move_y)
        

        
        screen.blit(bg_img, [back_x,0])
        screen.blit(bg_img2, [back_x+1600,0])
        screen.blit(bg_img, [back_x+3200,0])
        screen.blit(bg_img2, [back_x+4800,0])
        #screen.blit(ko_img, [300,200])
        screen.blit(ko_img,ko_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
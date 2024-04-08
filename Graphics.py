import pygame

class Button:
    def __init__(self,y,x,h,w,color):
        self.y = y
        self.x = x
        self.h = h
        self.w = w
        self.color = color

    def is_pressed(self):     
        yy,xx = pygame.mouse.get_pos()
        return yy >= self.y and yy <= self.y + self.h and xx >= self.x and xx <= self.x + self.w

    def draw(self,sc):
        pygame.draw.rect(sc,self.color,(self.y,self.x,self.h,self.w))
        f0 = pygame.font.Font(None, 36)
        text0 = f0.render("Играть", True,[255,255,255])
        sc.blit(text0, (self.y + 32, self.x + 8))


def draw_main_screen(sc,score,last,button):
    sc.fill([255,255,255])
    button.draw(sc)
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render("Лучший счёт : "+str(score), True,[0,0,255])
    sc.blit(text1, (10, 40))
    text2 = f1.render("Прошлый раз : "+str(last), True,[0,0,255],)
    sc.blit(text2, (300, 40))

def draw_game_screen(sc,pl,balls,score):
    sc.fill([255,255,255])
    pygame.draw.rect(sc,[0,255,0],(pl.y,pl.x,30,30))
    for b in balls:
        pygame.draw.rect(sc,[255,0,0],(b.y,b.x,b.w,b.h))
    f2 = pygame.font.Font(None, 36)
    text2 = f2.render("Cчёт : "+str(score), True,[0,0,255])
    sc.blit(text2, (10, 40))
    pygame.display.flip()

def check_user_actions(pl):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and pl.y > 0:
        pl.y -= pl.speed
    if keys[pygame.K_RIGHT] and pl.y < 1170:
        pl.y += pl.speed
    if keys[pygame.K_UP] and pl.x > 0:
        pl.x -= pl.speed
    if keys[pygame.K_DOWN] and pl.x < 870:
        pl.x += pl.speed


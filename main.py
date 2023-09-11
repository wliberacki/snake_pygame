import pygame
import random

pygame.init()

white=(236,236,236)
blue=(48,54,229)
red=(218,27,27)
black=(0,0,0)
green=(94,142,30)
yellow=(240,216,0)

szerokosc = 800
wysokosc = 600

#ustawienia wyswietlacza
gui=pygame.display.set_mode((szerokosc,wysokosc))
pygame.display.set_caption('Snake gra')

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 40)
score_font = pygame.font.SysFont(None, 60)

def Score(score):
    value = score_font.render("Wynik: " + str(score), True, yellow)
    gui.blit(value, [0, 0])

snake_block = 20

def snake(snake_block , snake_list):
    for x in snake_list:
        pygame.draw.rect(gui , green, [x[0], x[1], snake_block, snake_block])

#zdefiniowanie wiadomosci koncowej
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    gui.blit(mesg, [szerokosc / 5, wysokosc / 2.2])



#petla gry
def gameLoop():
    koniec=False
    zamkniecie=False

    # wspolrzedne werza
    x1 = szerokosc / 2
    y1 = wysokosc / 2
    x1_zmiana = 0
    y1_zmiana = 0
    ruch = "brak"

    snake_List = []
    dlugosc_snake = 1

    jedzeniex = round(random.randrange(0, szerokosc - snake_block) / 20.0) * 20.0
    jedzeniey = round(random.randrange(0, wysokosc - snake_block) / 20.0) * 20.0

    while koniec==False:

        while zamkniecie == True:
            gui.fill(white)
            message("P - zagraj jeszcze raz     Q - wyjdź", blue)
            Score(dlugosc_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        koniec = True
                        zamkniecie = False
                    if event.key == pygame.K_p:
                        gameLoop()


        for event in pygame.event.get():

             if event.type == pygame.QUIT:
                koniec = True
             if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not (ruch == "lewo" or ruch =="prawo"):
                        x1_zmiana = -snake_block
                        y1_zmiana =0
                        ruch = "lewo"
                elif event.key == pygame.K_RIGHT:
                    if not (ruch == "lewo" or ruch == "prawo"):
                        x1_zmiana = snake_block
                        y1_zmiana =0
                        ruch = "prawo"
                elif event.key == pygame.K_UP:
                    if not (ruch == "gora" or ruch == "dol"):
                        y1_zmiana = -snake_block
                        x1_zmiana =0
                        ruch = "gora"
                elif event.key == pygame.K_DOWN:
                    if not (ruch == "gora" or ruch == "dol"):
                        y1_zmiana  = snake_block
                        x1_zmiana=0
                        ruch = "dol"
        if x1 >= szerokosc or x1 < 0 or y1 >= wysokosc or y1 < 0:
            zamkniecie = True
        x1+=x1_zmiana
        y1+=y1_zmiana

        gui.fill(white)

        pygame.draw.rect(gui, red, [jedzeniex, jedzeniey, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > dlugosc_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                zamkniecie = True

        snake(snake_block, snake_List)
        Score(dlugosc_snake - 1)

        pygame.display.update()

        if x1 == jedzeniex and y1 == jedzeniey:
            jedzeniex = round(random.randrange(0, szerokosc - snake_block) / 20.0) * 20.0
            jedzeniey = round(random.randrange(0, wysokosc - snake_block) / 20.0) * 20.0
            dlugosc_snake += 1
        clock.tick(15)

    pygame.quit()
    quit()

gameLoop()

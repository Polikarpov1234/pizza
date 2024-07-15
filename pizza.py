import pygame
import random 
import time
pygame.init()

# Цвета
WHITE = (255, 255, 255)
GOLD = ("gold2")
YELLOW = ("light goldenrod")
FPS = 100
clock = pygame.time.Clock()
x = 400
q = 0
w = 0

# Размеры экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Пример кнопки в Pygame")

# Шрифт и размер текста
font = pygame.font.Font(None, 18)
fontt = pygame.font.Font(None, 46)

# Текст на кнопках

text = font.render("Добавить соус", True, GOLD)
text1 = font.render("Добавить пепперони", True, GOLD)
text2 = font.render("Добавить курицу", True, GOLD)
text3 = font.render("Добавить сыр", True, GOLD)
text4 = font.render("Добавить грибы", True, GOLD)
text5 = font.render("Добавить колбаски", True, GOLD)
text6 = fontt.render("->", True, GOLD)

# Размеры и положение кнопки
button_width = 100
button_height = 50
button_x = 30
button_y = 520

button_width1 = 100
button_height1 = 50
button_x1 = 140
button_y1 = 520

button_width2 = 100
button_height2 = 50
button_x2 = 250
button_y2 = 520

button_width3 = 100
button_height3 = 50
button_x3 = 360
button_y3 = 520

button_width4 = 100
button_height4 = 50
button_x4 = 470
button_y4 = 520

button_width5 = 100
button_height5 = 50
button_x5 = 580
button_y5 = 520

button_width6 = 100
button_height6 = 50
button_x6 = 690
button_y6 = 520

# размер пиццы
option_size_pizza = (70, 85, 100)
size_pizza = random.choice(option_size_pizza)

def moove_pizza():
    global x, pizza
    for i in range(50):    
        x += 5
        time.sleep(0.1)


# Основной цикл программы
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button_x <= mouse_pos[0] <= button_x + button_width and button_y <= mouse_pos[1] <= button_y + button_height:
                q += 1
            if button_x6 <= mouse_pos[0] <= button_x6 + button_width6 and button_y6 <= mouse_pos[1] <= button_y6 + button_height6:
                w += 1
            #if button_x1 <= mouse_pos[0] <= button_x1 + button_width1 and button_y1 <= mouse_pos[1] <= button_y1 + button_height1:


    screen.fill(GOLD)
    
    pygame.draw.rect(screen, WHITE, (button_x, button_y, button_width, button_height))
    screen.blit(text, (button_x + 2, button_y + 10))
    pygame.draw.rect(screen, WHITE, (button_x1, button_y1, button_width1, button_height1))
    screen.blit(text1, (button_x1 + 2, button_y1 + 10))
    pygame.draw.rect(screen, WHITE, (button_x2, button_y2, button_width2, button_height2))
    screen.blit(text2, (button_x2 + 2, button_y2 + 10))
    pygame.draw.rect(screen, WHITE, (button_x3, button_y3, button_width3, button_height3))
    screen.blit(text3, (button_x3 + 2, button_y3 + 10))
    pygame.draw.rect(screen, WHITE, (button_x4, button_y4, button_width4, button_height4))
    screen.blit(text4, (button_x4 + 2, button_y4 + 10))
    pygame.draw.rect(screen, WHITE, (button_x5, button_y5, button_width5, button_height5))
    screen.blit(text5, (button_x5 + 2, button_y5 + 10))
    pygame.draw.rect(screen, WHITE, (button_x6, button_y6, button_width6, button_height6))
    screen.blit(text6, (button_x6 + 40, button_y6 + 7))
    
    #создание теста
    pizza = pygame.draw.circle(screen, YELLOW, (x, 300), size_pizza)
    if q >= 1:

    #создание соуса    
        pygame.draw.circle(screen, "tomato", (x, 300), size_pizza - 10)
    if w >= 1:
        x += 2
        time.sleep(0.02)

    pygame.display.flip()

pygame.quit()
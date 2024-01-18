import pygame
import os
import sys


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 1100
        self.top = 650
        self.cell_size = 140

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(int(self.height)):
            for j in range(int(self.width)):
                pygame.draw.rect(screen, (255, 255, 255), (
                    j * self.cell_size + self.left, i * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 1)

    def load_image(name, colorkey=None):
        fullname = os.path.join('data', name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        return image


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self, x, y, message='', action=None):
        buttonSound = pygame.mixer.Sound('presButton.wav')

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] and mouse[0] < x + self.width:
            if y < mouse[1] and mouse[1] < y + self.height:
                pygame.draw.rect(screen, (0, 0, 0), (x, y, self.width, self.height))
                if click[0] == 1:
                    pygame.mixer.Sound.play(buttonSound)
                    pygame.time.delay(300)
                    if action is not None:
                        action()
            else:
                pygame.draw.rect(screen, (0, 0, 0), (x, y, self.width, self.height))
        else:
            pygame.draw.rect(screen, (0, 0, 0), (x, y, self.width, self.height))


if __name__ == '__main__':
    pygame.init()
    size = width, height = 3200, 2000
    screen = pygame.display.set_mode(size)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 165, 0))
        image = Board.load_image("CvD.png")
        screen.blit(image, (1075, 500))
        button = Button(450, 150)
        button.draw(1375, 850)
        button2 = Button(450, 150)
        button2.draw(1375, 1100)
        button3 = Button(100, 100)
        button3.draw(800, 500)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        x, y = 800, 500
        if x < mouse[0] and mouse[0] < x + 100:
            if y < mouse[1] and mouse[1] < y + 100:
                if click[0] == 1:
                    running = False
        x, y = 1375, 850
        if x < mouse[0] and mouse[0] < x + 450:
            if y < mouse[1] and mouse[1] < y + 150:
                if click[0] == 1:
                    pygame.init()
                    size = width, height = 3200, 2000
                    screen = pygame.display.set_mode(size)
                    runn = True
                    while runn:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                runn = False
                        screen.fill((255, 165, 0))
                        button4 = Button(100, 100)
                        button4.draw(800, 500)
                        levelButton1 = Button(400, 300)
                        levelButton1.draw(875, 850)
                        levelButton2 = Button(400, 300)
                        levelButton2.draw(1350, 850)
                        levelButton3 = Button(500, 400)
                        levelButton3.draw(1825, 800)
                        mouse = pygame.mouse.get_pos()
                        click = pygame.mouse.get_pressed()
                        x, y = 800, 500
                        if x < mouse[0] and mouse[0] < x + 100:
                            if y < mouse[1] and mouse[1] < y + 100:
                                if click[0] == 1:
                                    runn = False
                        x, y = 875, 850
                        if x < mouse[0] and mouse[0] < x + 400:
                            if y < mouse[1] and mouse[1] < y + 300:
                                if click[0] == 1:
                                    level1 = True
                                    board = Board(9, 5)
                                    while level1:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                level1 = False
                                        screen.fill((255, 165, 0))
                                        board.render(screen)
                                        pygame.display.flip()
                        x, y = 1350, 850
                        if x < mouse[0] and mouse[0] < x + 400:
                            if y < mouse[1] and mouse[1] < y + 300:
                                if click[0] == 1:
                                    level2 = True
                                    board = Board(9, 5)
                                    while level2:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                level2 = False
                                        screen.fill((255, 165, 0))
                                        board.render(screen)
                                        pygame.display.flip()
                        x, y = 1825, 800
                        if x < mouse[0] and mouse[0] < x + 500:
                            if y < mouse[1] and mouse[1] < y + 400:
                                if click[0] == 1:
                                    level3 = True
                                    board = Board(9, 5)
                                    while level3:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                level3 = False
                                        screen.fill((255, 165, 0))
                                        board.render(screen)
                                        pygame.display.flip()
                        pygame.display.flip()



        pygame.display.flip()
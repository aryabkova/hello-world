import random, pygame, sys
from pygame.locals import *

# вводим постоянные переменные:

SPEED = 30 # скорость работы (кадров в секунду)
DISPLAYWIDTH = 700 # ширина окна в пикселях
DISPLAYHEIGHT = 690 # высота окна в пикселях
REVEALSPEED = 7 # скорость открытия карточек
CARDSIZE = 100 # размер карточки в пикселях
GAPS = 10 # расстояние между карточками в пикселях
FIELDWIDTH = 6 # количество карточек в столбце
FIELDHEIGHT = 6 # количество карточек в строке
XMARGIN = int((DISPLAYWIDTH - (FIELDWIDTH * (CARDSIZE + GAPS))) / 2)
YMARGIN = int((DISPLAYHEIGHT - (FIELDHEIGHT * (CARDSIZE + GAPS))) / 2)

# определяем цвета по схеме RGB:

GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
LIGHTBLUE = (0, 140, 255)

BGCOLOR = NAVYBLUE # цвет фона
LIGHTBGCOLOR = LIGHTBLUE # цвет фона для мигания при выигрыше
BOXCOLOR = WHITE # цвет карточек
HIGHLIGHTCOLOR = BLUE # цвет обводки карточек

# карточки:
CAT = 'CAT'
DEER = 'DEER'
DOG = 'DOG'
DONKEY = 'DONKEY'
ELK = 'ELK'
FOX = 'FOX'
GUEPARD = 'GUEPARD'
GIRAFFE = 'GIRAFFE'
HIP = 'HIP'
HORSE = 'HORSE'
LION = 'LION'
MONKEY = 'MONKEY'
PIG = 'PIG'
SHEEP = 'SHEEP'
WOLF = 'WOLF'
ZEBRA = 'ZEBRA'
ELEPH = 'ELEPH'
GOAT = 'GOAT'

ALLCARDS = [CAT, DEER, DOG, DONKEY, ELK, FOX, GUEPARD, GIRAFFE, HIP, HORSE, LION, MONKEY, PIG, SHEEP, WOLF, ZEBRA, ELEPH, GOAT]

def main():
    global FPSCLOCK, DISPLAY # отмечаем, что переменные глобальные, поскольку используются в других функциях
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT)) # устанавливаем экран игры

    mouseX = 0 # координата мышки Х
    mouseY = 0 # координата мышки Y
    pygame.display.set_caption('Memory Puzzle') # название окна

    myField = getRandomCards()
    checkOpenCards = generateOpenCardsData(False)

    Selection = None # если None, то открыта только одна карточка

    DISPLAY.fill(BGCOLOR) # устанавливаем цвет фона
    startAnimation(myField)

    while True:
        CLICK = False # клик мышки

        DISPLAY.fill(BGCOLOR) # чтобы стереть все, что было раньше
        getFeild(myField, checkOpenCards)

        for event in pygame.event.get(): # цикл контроля движения мышки и нажатия клавиш выхода
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE): # если нажимаем на эскейп или на крестик, то выход
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION: # движение мышки
                mouseX, mouseY = event.pos # запоминаем координаты
            elif event.type == MOUSEBUTTONUP: # клик мышкой
                mouseX, mouseY = event.pos
                CLICK = True

        cardX, cardY = coordsXYcard(mouseX, mouseY)
        # регулирование клика мышки:
        if cardX != None and cardY != None:

            # если карточки не открыты:
            if not checkOpenCards[cardX][cardY]:
                drawAroundCard(cardX, cardY) # сохраняем значения и обводим карточку

            # курсор на карточке и делается клик мышкой:
            if not checkOpenCards[cardX][cardY] and CLICK:
                openCard(myField, [(cardX, cardY)])
                checkOpenCards[cardX][cardY] = True # карточка открыта

                if Selection == None: # значит была открыта только первая карточка, сохраняем координаты второй
                    Selection = (cardX, cardY)
                else: # значит вторая, поэтому проверяем их совпадение
                    card1 = myField[Selection[0]][Selection[1]]
                    card2 = myField[cardX][cardY]

                    if card1 != card2:
                        # если карточки не совпадают, то закрываем их
                        pygame.time.wait(1000) # 1000 milliseconds = 1 sec
                        closeCards(myField, [(Selection[0], Selection[1]), (cardX, cardY)])
                        checkOpenCards[Selection[0]][Selection[1]] = False
                        checkOpenCards[cardX][cardY] = False
                    else: # если совпадают, то убираем
                        pygame.time.wait(1000)
                        checkOpenCards[Selection[0]][Selection[1]] = '1'
                        checkOpenCards[cardX][cardY] = '1'
                    if hasWon(checkOpenCards): # проверяем, все ли карточки найдены
                        gameWonAnimation()

                        myField = getRandomCards()
                        checkOpenCards = generateOpenCardsData(False)

                        getFeild(myField, checkOpenCards)
                        pygame.display.update()
                        pygame.time.wait(1000)

                        startAnimation(myField)
                    Selection = None

        pygame.display.update()
        FPSCLOCK.tick(SPEED)


def generateOpenCardsData(val): # генерируем список булевых значений в зависимости от размера игрового поля
    checkOpenCards = []
    for i in range(FIELDWIDTH):
        checkOpenCards.append([val] * FIELDHEIGHT)
    return checkOpenCards

def getRandomCards(): # получаем список фигур, формируем игровое поле
    random.shuffle(ALLCARDS) # смешивание элементов
    cards = ALLCARDS * 2 # берем нужное количество и делаем для каждой карточки дубль
    random.shuffle(cards) # и снова перемешиваем
    # создаем игровое поле с рандомным расположением значков (по столбцам)
    feild = []
    for x in range(FIELDWIDTH):
        column = []
        for y in range(FIELDHEIGHT):
            column.append(cards[0])
            del cards[0] # удаляем карточку, которую уже взяли
        feild.append(column)
    return feild

def splitIntoGroupsOf(groupSize, List): # делаем списки списков определенной длинны
    result = []
    for i in range(0, len(List), groupSize):
        result.append(List[i:i + groupSize]) # возвращаются элементы с i-го по groupSize
    return result

def leftTopCoords(cardX, cardY): # переводим координаты карточек в пиксельные координаты
    left = cardX * (CARDSIZE + GAPS) + XMARGIN # верхняя левая координата карточки
    top = cardY * (CARDSIZE + GAPS) + YMARGIN
    return (left, top)

def coordsXYcard(x, y): # переводим писксельные координаты в координаты карточки
    for cardX in range(FIELDWIDTH):
        for cardY in range(FIELDHEIGHT):
            left, top = leftTopCoords(cardX, cardY)
            cardRect = pygame.Rect(left, top, CARDSIZE, CARDSIZE)
            if cardRect.collidepoint(x, y): # возвращает True если находится внутри карточки (находим карточку, на которой мышка)
                return (cardX, cardY)
    return (None, None)

def getCards(shape, cardX, cardY):
    left, top = leftTopCoords(cardX, cardY) # получаем пиксельные координаты
    # импорт картинок:
    if shape == CAT:
        DISPLAY.blit(pygame.transform.scale(pygame.image.load('cat.jpg'), (CARDSIZE, CARDSIZE)),[left,top])
    elif shape == DEER:
        DISPLAY.blit(pygame.transform.scale(pygame.image.load('deer.jpg'), (CARDSIZE, CARDSIZE)),[left,top])
    elif shape == DOG:
        DISPLAY.blit(pygame.transform.scale(pygame.image.load('dog.jpg'), (CARDSIZE, CARDSIZE)),[left,top])
    elif shape == DONKEY:
        DISPLAY.blit(pygame.transform.scale(pygame.image.load('donk.jpg'), (CARDSIZE, CARDSIZE)),[left,top])
    elif shape == ELK:
        DISPLAY.blit(pygame.transform.scale(pygame.image.load('elk.jpg'), (CARDSIZE, CARDSIZE)),[left,top])
    elif shape == FOX:
        DISPLAY.blit(pygame.transform.scale(pygame.image.load('fox.jpg'), (CARDSIZE, CARDSIZE)),[left,top])
    elif shape == GUEPARD:
        DISPLAY.blit(pygame.transform.scale(pygame.image.load('gep.jpg'), (CARDSIZE, CARDSIZE)),[left,top])
    elif shape == GIRAFFE:
        DISPLAY.blit(pygame.transform.scale(pygame.image.load('giraf.jpg'), (CARDSIZE, CARDSIZE)),[left,top])
    elif shape == HIP:
        DISPLAY.blit(pygame.transform.scale(pygame.image.load('hip.jpg'), (CARDSIZE, CARDSIZE)),[left,top])
    elif shape == HORSE:
        DISPLAY.blit(pygame.transform.scale(pygame.image.load('hors.jpg'), (CARDSIZE, CARDSIZE)),[left,top])
    elif shape == LION:
        DISPLAY.blit(pygame.transform.scale(pygame.image.load('lion.jpg'), (CARDSIZE, CARDSIZE)),[left,top])
    elif shape == MONKEY:
        DISPLAY.blit(pygame.transform.scale(pygame.image.load('monk.jpg'), (CARDSIZE, CARDSIZE)),[left,top])
    elif shape == PIG:
        DISPLAY.blit(pygame.transform.scale(pygame.image.load('pig.jpg'), (CARDSIZE, CARDSIZE)),[left,top])
    elif shape == SHEEP:
        DISPLAY.blit(pygame.transform.scale(pygame.image.load('sheep.jpg'), (CARDSIZE, CARDSIZE)),[left,top])
    elif shape == WOLF:
        DISPLAY.blit(pygame.transform.scale(pygame.image.load('wolf.jpg'), (CARDSIZE, CARDSIZE)),[left,top])
    elif shape == ZEBRA:
        DISPLAY.blit(pygame.transform.scale(pygame.image.load('zebra.jpg'), (CARDSIZE, CARDSIZE)),[left,top])
    elif shape == ELEPH:
        DISPLAY.blit(pygame.transform.scale(pygame.image.load('elef.jpg'), (CARDSIZE, CARDSIZE)),[left,top])
    elif shape == GOAT:
        DISPLAY.blit(pygame.transform.scale(pygame.image.load('goat.jpg'), (CARDSIZE, CARDSIZE)),[left,top])

def drawBoxCovers(feild, boxes, coverage): # прорисовываем карточки
    # boxes - лист с коорддинатами х у
    for box in boxes:
        left, top = leftTopCoords(box[0], box[1])
        pygame.draw.rect(DISPLAY, BGCOLOR, (left, top, CARDSIZE, CARDSIZE))
        shape = feild[box[0]][box[1]]
        getCards(shape, box[0], box[1])
        if coverage > 0:
            pygame.draw.rect(DISPLAY, BOXCOLOR, (left, top, coverage, CARDSIZE))
    pygame.display.update()
    FPSCLOCK.tick(SPEED)


def openCard(feild, cardsToOpen): # карточки открываются
    for coverage in range(CARDSIZE, (-REVEALSPEED) - 1, -REVEALSPEED):
        drawBoxCovers(feild, cardsToOpen, coverage)

def closeCards(feild, cardsToClose): # карточки закрываются
    for coverage in range(0, CARDSIZE + 1, REVEALSPEED):
        drawBoxCovers(feild, cardsToClose, coverage)

def getFeild(feild, opened): # рисуем игровое поле
    for cardX in range(FIELDWIDTH):
        for cardY in range(FIELDHEIGHT):
            left, top = leftTopCoords(cardX, cardY)
            if not opened[cardX][cardY]:
                # рисуем закрытую карточку.
                pygame.draw.rect(DISPLAY, BOXCOLOR, (left, top, CARDSIZE, CARDSIZE))
            elif opened[cardX][cardY] == '1':
                pygame.draw.rect(DISPLAY, BGCOLOR, (left, top, CARDSIZE, CARDSIZE))
            else:
                # открываем карточку
                shape = feild[cardX][cardY]
                getCards(shape, cardX, cardY)

def drawAroundCard(cardX, cardY): # подсвечиваем карточку
    left, top = leftTopCoords(cardX, cardY)
    pygame.draw.rect(DISPLAY, HIGHLIGHTCOLOR, (left - 5, top - 5, CARDSIZE + 10, CARDSIZE + 10), 4)


def startAnimation(feild): # рандомное открытие карточек вначале для запоминания
    closedBoxes = generateOpenCardsData(False)
    boxes = []
    for x in range(FIELDWIDTH):
        for y in range(FIELDHEIGHT):
            boxes.append((x, y))
    random.shuffle(boxes)
    cardGroups = splitIntoGroupsOf(6, boxes)

    getFeild(feild, closedBoxes)
    for boxGroup in cardGroups:
        openCard(feild, boxGroup)
        closeCards(feild, boxGroup)


def gameWonAnimation(): # при выигрыше
    color1 = LIGHTBGCOLOR
    color2 = BGCOLOR
    for i in range(20):
        color1, color2 = color2, color1 # swap colors
        DISPLAY.fill(color1)
        pygame.init()
        pygame.draw.rect(DISPLAY, BOXCOLOR, (100, 200, 500, 300))
        pygame.draw.rect(DISPLAY, GRAY, (150, 410, 180, 55))
        pygame.draw.rect(DISPLAY, GRAY, (375, 410, 180, 55))
        heading = pygame.font.SysFont('verdana', 48)
        text1 = heading.render('Ура!!!', 1, RED)
        text2 = heading.render('Вы выиграли!', 1, RED)
        variant = pygame.font.SysFont('verdana', 30)
        text3 = variant.render('Новая игра', 1, WHITE)
        text4 = variant.render('Выйти', 1, WHITE)

        place1 = text1.get_rect(center=(370, 250))
        place2 = text2.get_rect(center=(370, 320))
        place3 = text3.get_rect(center=(242, 435))
        place4 = text3.get_rect(center=(500, 435))

        DISPLAY.blit(text1, place1)
        DISPLAY.blit(text2, place2)
        DISPLAY.blit(text3, place3)
        DISPLAY.blit(text4, place4)
        pygame.time.wait(5000)
        pygame.display.update()
        pygame.time.wait(250)


def hasWon(checkOpenCards): # проверяет, открыты ли все карточки
    for i in checkOpenCards:
        if False in i:
            return False # возвращает False если какие-то закрыты
    return True


if __name__ == '__main__':
    main()
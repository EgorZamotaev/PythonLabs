
import sys

sys.path.insert(0, '/home/egor/Documents/PythonLabs/Lab3/3.1')
sys.setrecursionlimit(3500)

import main_game
import pygame
from pygame import *

FINISH_COLOR = '#0000ff'
NPC_COLOR = '#ff0033'
PLATFORM_COLOR = "#412227"
PLATFORM_COLOR2 = "#FFFFFF"
MAZE_SIZE = 10
WIN_WIDTH = 1010 # Ширина создаваемого окнa
WIN_HEIGHT = 1010  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#FA8072"
PLATFORM_WIDTH = 10
PLATFORM_HEIGHT = 10

maze = main_game.maze_generation()
level = maze[0]
door = (maze[1][0], maze[1][1])
door1 = maze[1][0]
door2 = maze[1][1]
print(door1, door2)
out = (maze[2][0], maze[2][1])
out1 = maze[2][0]
out2 = maze[2][1]
print(out)
print(level)
for i in range(len(level)):
    for j in range(len(level)):
        if level[i][j] == 0:
            level[i][j] = 1
        else:
            level[i][j] = 0


def search_path(data, x, y, short_path={}, full_path={},
                count=0):  # data-лабиринт; х,у - точка, где мы сейчас находимся
    # short_path - {key=точка куда идём: value=откуда идём}
    # full_path - {key=точка : value=кол-во шагов до точки}
    # count - номер шага
    full_path[(x, y)] = count  # Записываем точку и сколько шагов до неё на данном этапе
    if x == out1 and y == out2:  # Точка выхода из лабиринта
        return full_path, short_path
    walks = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up,left, down, right,
    for walk_X, walk_Y in walks:
        if data[x + walk_X][y + walk_Y] == 0 and (0 < x + walk_X < 100 and 0 < y + walk_Y < 100):  # Если ячейка свободна
            # и мы не вышли за границы лабиринта
            check = full_path.get((x + walk_X, y + walk_Y))  # Смотрим на точку, куда хотим пойти и сколько до неё шагов
            # Если check=None, значит в точке ещё не были
            if check != None and check > count:  # Если мы были уже в этой точке и расстояние до неё больше, чем номер шага
                # на данном этапе
                full_path[
                    (x + walk_X, y + walk_Y)] = count  # Перезаписываем full_path, т.к нашли более короткую дистанцию
                short_path[(x + walk_X, y + walk_Y)] = (x, y)  # Пепрезаписываем short_path, потому что нашли точку, из
                # которой в данную можно попасть короче
                search_path(data, x + walk_X, y + walk_Y, short_path, full_path,
                            count + 1)  # Увеличиваем шаг и запускаем
                # рекурсивно функцию
            else:
                if (x + walk_X, y + walk_Y) not in full_path.keys():  # Если в токе, куда собираемся пойти еще не были
                    short_path[(x + walk_X, y + walk_Y)] = (x, y)  # записываем {куда идём:откуда идём}
                    search_path(data, x + walk_X, y + walk_Y, short_path, full_path, count + 1)  # запускаем рекурсию
                    # с шагом +1
    return full_path, short_path


def short_path(data, path=[], start=door, end=out):  # Сюда прилетает short_path из search_path, когда нашли выход
    # data=short_path, start - координата точки входа, end - выхода
    # path - короткий путь в виде списка координат из лабиринта
    """Здесь мы рекурсивно пробегаемся из конечной точки в начальную, восстанавливая путь по лабиринту:
    берём {точка, куда пришли(допустим А) : точка откуда пришли (в точку А) - Б}"""
    if len(path) == 0:
        path.append(end)
    path.append(data[end])
    if data[end] == start:
        return path
    else:
        short_path(data, path, start, data[end])
    return path


p = search_path(level, door1, door2)
print(p)

if p is None:
    print('No Exit!!!')
else:
    short = short_path(p[1])
    short.reverse()
    for walk in short:
        level[walk[0]][walk[1]] = 3  # Здесь мы просто указываем в графе путь к выходу цифрой 3
    for see in level:
        print(see)

pygame.init()
screen = pygame.display.set_mode(DISPLAY)
bg = Surface(DISPLAY)
bg.fill(Color(BACKGROUND_COLOR))
screen.blit(bg, (0, 0))
platforms = []

x = y = 0
for row in level:
    for col in row:
        if col == 1:
            pf = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
            pf.fill(Color(PLATFORM_COLOR))
            screen.blit(pf, (x, y))
        if col == 3:
            pf = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
            pf.fill(Color(PLATFORM_COLOR2))
            screen.blit(pf, (x, y))
        x += PLATFORM_WIDTH
    y += PLATFORM_HEIGHT
    x = 0


pf = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
pf.fill(Color(NPC_COLOR))
screen.blit(pf, (door2*10, door1*10))

pf = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
pf.fill(Color(FINISH_COLOR))
screen.blit(pf, (out2*10, out1*10))

while True:
    pygame.display.update()
    for i in pygame.event.get():
        if i.type == QUIT:
            pygame.quit()
            exit()


from npc import NPC
import pygame
from pygame import *
from blocks import Platform
from random import randrange, randint
from finish import Finish

WIN_WIDTH = 1010  # Ширина создаваемого окнa
WIN_HEIGHT = 1010  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#FA8072"
PLATFORM_WIDTH = 10
PLATFORM_HEIGHT = 10
MAZE_SIZE = 50


def neighbours(x_start, y_start, maze_size):
    neighbour = []

    if x_start + 2 <= maze_size - 2:
        neighbour.append([x_start + 2, y_start])
    if y_start + 2 <= maze_size - 2:
        neighbour.append([x_start, y_start+2])
    if x_start - 2 >= 0:
        neighbour.append([x_start - 2, y_start])
    if y_start - 2 >= 0:
        neighbour.append([x_start, y_start - 2])
    return neighbour


def outneighbour(neighbours, visited):
    out = []
    for i in range(len(neighbours)):
        if neighbours[i] in visited:
            out.append(i)
    out.reverse()

    for i in range(len(out)):
        neighbours.pop(out[i])
    return neighbours


def maze_generation():
    maze_size = MAZE_SIZE * 2 + 1
    level = [[0 for i in range(maze_size)] for i in range(maze_size)]

    x = randrange(1, maze_size - 2, 2)
    y = randrange(1, maze_size - 2, 2)
    level[x][y] = 1
    visited = [[x, y]]

    while len(visited) < MAZE_SIZE ** 2:
        neighbour = neighbours(x, y, maze_size)
        neighbour = outneighbour(neighbour,visited)

        if len(neighbour) == 0:
            i = 0
            while len(neighbour) == 0:
                i += 1
                next = visited[len(visited) - i]
                x = next[0]
                y = next[1]
                pas = neighbours(x, y, maze_size)
                neighbour = outneighbour(pas, visited)

        if len(neighbour) != 0:
            next = randint(0, len(neighbour) - 1)
            if neighbour[next][0] - x < 0:
                level[x-1][y] = 1
            elif neighbour[next][0] - x > 0:
                level[x+1][y] = 1
            elif neighbour[next][1] - y < 0:
                level[x][y-1] = 1
            else:
                level[x][y+1] = 1
            x = neighbour[next][0]
            y = neighbour[next][1]
            level[x][y] = 1
            visited.append([x, y])
    return level, visited[len(visited)-randint(1, len(visited)-1)], visited[len(visited)-randint(1, len(visited)-1)]


def main():
    ms = 'k'
    while True:
        pygame.init()
        maze = maze_generation()
        screen = pygame.display.set_mode(DISPLAY)
        pygame.display.set_caption('Maze game')

        bg = Surface(DISPLAY)
        bg.fill(Color(BACKGROUND_COLOR))
        screen.blit(bg, (0, 0))

        hero = NPC(maze[1][0]*10, maze[1][1]*10)
        finish = Finish(maze[2][0]*10, maze[2][1]*10)

        entites = pygame.sprite.Group()
        platforms = []
        entites.add(hero)
        entites.add(finish)
        level = maze[0]

        clock = pygame.time.Clock()

        x = y = 0
        for row in level:
            for col in row:
                if col == 0:
                    pf = Platform(x, y)
                    entites.add(pf)
                    platforms.append(pf)
                x += PLATFORM_WIDTH
            y += PLATFORM_HEIGHT
            x = 0

        stepc = 0

        while True:
            for i in pygame.event.get():
                if i.type == KEYDOWN and i.key == K_LEFT:
                    stepc += 1
                    hero.rect.x -= 10
                    for p in platforms:
                        if sprite.collide_rect(hero, p):
                            hero.rect.left = p.rect.right
                if i.type == KEYDOWN and i.key == K_RIGHT:
                    stepc += 1
                    hero.rect.x += 10
                    for p in platforms:
                        if sprite.collide_rect(hero, p):
                            hero.rect.right = p.rect.left
                if i.type == KEYDOWN and i.key == K_UP:
                    stepc += 1
                    hero.rect.y -= 10
                    for p in platforms:
                        if sprite.collide_rect(hero, p):
                            hero.rect.top = p.rect.bottom
                if i.type == KEYDOWN and i.key == K_DOWN:
                    hero.rect.y += 10
                    stepc += 1
                    for p in platforms:
                        if sprite.collide_rect(hero, p):
                            hero.rect.bottom = p.rect.top
                if i.type == QUIT:
                    pygame.quit()
                    exit()
            pygame.display.update()
            screen.blit(bg, (0, 0))
            entites.draw(screen)
            clock.tick(60)
            ms = finish.collaid(hero, stepc)
            if ms == 'kek':
                break
            pygame.display.update()


if __name__ == '__main__':
    main()

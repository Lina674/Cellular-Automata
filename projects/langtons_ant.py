import pygame, random, pygame.locals, sys

pygame.init()

width, height = 1920,1080
screen = pygame.display.set_mode((width, height))
cell_size = 10

directions = ['up', 'right', 'down', 'left']
moves = {'up' : (1,0), 'right' : (0, 1), 'down' : (-1,0), 'left' : (0,-1)}

def ninety_degrees_left(current_direction): #start : î end: <--
    current = directions.index(current_direction)
    next = (current - 1) % len(directions)
    return directions[next]

def ninety_degrees_right(current_direction):
    current = directions.index(current_direction)
    next = (current + 1) % len(directions)
    return directions[next]

def next_cell(y, x, direction):
    dy, dx = moves[direction]
    return y + dy, x + dx

def main():
    clock = pygame.time.Clock()

    h = height // cell_size
    w = width // cell_size

    grid = [[False for i in range(w)] for j in range(h)]
    
    white, black = (255,255,255), (0,0,0)

    ry = random.randint(0, h-1)
    rx = random.randint(0, w-1)
    current_pos = 'up'

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                black, white= white, black
                pygame.display.update()
       
        ant_pos = grid[ry][rx]
        if not ant_pos: #black
            grid[ry][rx] = True
            current_pos = ninety_degrees_left(current_pos)
        else: #white
            grid[ry][rx] = False
            current_pos = ninety_degrees_right(current_pos)

        ry, rx = next_cell(ry, rx, current_pos)

        ry = ry % h
        rx = rx % w
        
        screen.fill(black)
        for y in range(h):
            for x in range(w):
                color = white if grid[y][x] else black
                pygame.draw.rect(screen, color, pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size))
        
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
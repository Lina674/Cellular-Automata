import pygame, random, pygame.locals, sys

pygame.init()

width, height = 1920,1080
screen = pygame.display.set_mode((width, height))
cell_size = 10

def main():
    clock = pygame.time.Clock()
    grid = [[0 for i in range(width // cell_size)] for j in range(height // cell_size)]
    
    white, black, pink, green = (255,255,255), (0,0,0), (222,88,225), (33,167,30)

    for y in range(height // cell_size):
        for x in range(width // cell_size):
            grid[y][x] = random.randint(0, 2)\

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                black, white= white, black
                pygame.display.update()
                
        new_grid = [[0 for i in range(width // cell_size)] for j in range(height // cell_size)]
        
        for y in range(height // cell_size):
            for x in range(width // cell_size):
                # Count live(2-on) neighbors
                live_neighbors = 0
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if dy == 0 and dx == 0:
                            continue  # Skip the current cell
                        neighbor_x = (x + dx) % (width // cell_size)
                        neighbor_y = (y + dy) % (height // cell_size)
                        
                        if grid[neighbor_y][neighbor_x] == 2:
                            live_neighbors += 1

                #on, dying, off
                #2,    1,    0
                if grid[y][x] == 0 and live_neighbors == 2:  # Live cell
                    new_grid[y][x] = 2        
                
                elif grid[y][x] == 2:
                    new_grid[y][x] = 1

                elif grid[y][x] == 1:
                    new_grid[y][x] = 0

        grid = new_grid
        screen.fill(black)
        for y in range(height // cell_size):
            for x in range(width // cell_size):
                color = white if grid[y][x] == 2 else pink if grid[y][x] == 1 else black
                pygame.draw.rect(screen, color, pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size))
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
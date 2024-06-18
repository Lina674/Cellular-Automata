import pygame, random, pygame.locals, sys

pygame.init()

width, height = 1920,1080
screen = pygame.display.set_mode((width, height))
cell_size = 10

def main():
    clock = pygame.time.Clock()
    grid = [[False for i in range(width // cell_size)] for j in range(height // cell_size)]
    
    white, black = (255,255,255), (0,0,0)

    for y in range(height // cell_size):
        for x in range(width // cell_size):
            grid[y][x] = random.randint(0, 1)\

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                black, white= white, black
                pygame.display.update()
                
        new_grid = [[False for i in range(width // cell_size)] for j in range(height // cell_size)]
        
        for y in range(height // cell_size):
            for x in range(width // cell_size):
                # Count live neighbors
                live_neighbors = 0
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if dy == 0 and dx == 0:
                            continue  # Skip the current cell
                        neighbor_x = (x + dx) % (width // cell_size)
                        neighbor_y = (y + dy) % (height // cell_size)
                        live_neighbors += grid[neighbor_y][neighbor_x]

                if grid[y][x]:  # Live cell
                    if live_neighbors in [2, 3]:  # Survival
                        new_grid[y][x] = True
                    else:  # Overcrowding or underpopulation
                        new_grid[y][x] = False
                else:  # Dead cell
                    if live_neighbors == 3:  # Reproduction
                        new_grid[y][x] = True
        grid = new_grid
        screen.fill(black)
        for y in range(height // cell_size):
            for x in range(width // cell_size):
                color = white if grid[y][x] else black
                pygame.draw.rect(screen, color, pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size))
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
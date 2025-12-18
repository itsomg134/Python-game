import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)
DARK_GREEN = (0, 150, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
        self.grow = False
    
    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
    
    def change_direction(self, direction):
        # Prevent reversing
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction
    
    def check_collision(self):
        head = self.body[0]
        # Wall collision
        if head[0] < 0 or head[0] >= GRID_WIDTH or head[1] < 0 or head[1] >= GRID_HEIGHT:
            return True
        # Self collision
        if head in self.body[1:]:
            return True
        return False
    
    def eat(self):
        self.grow = True
    
    def draw(self):
        for i, segment in enumerate(self.body):
            color = GREEN if i == 0 else DARK_GREEN
            rect = pygame.Rect(segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, 
                             GRID_SIZE - 2, GRID_SIZE - 2)
            pygame.draw.rect(screen, color, rect, border_radius=3)

class Food:
    def __init__(self):
        self.position = self.random_position()
    
    def random_position(self):
        return (random.randint(0, GRID_WIDTH - 1), 
                random.randint(0, GRID_HEIGHT - 1))
    
    def respawn(self, snake_body):
        while True:
            self.position = self.random_position()
            if self.position not in snake_body:
                break
    
    def draw(self):
        rect = pygame.Rect(self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE,
                          GRID_SIZE - 2, GRID_SIZE - 2)
        pygame.draw.rect(screen, RED, rect, border_radius=5)

def draw_text(text, x, y, color=WHITE):
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=(x, y))
    screen.blit(surface, rect)

def game_over_screen(score):
    screen.fill(BLACK)
    draw_text('GAME OVER', WIDTH // 2, HEIGHT // 2 - 40, RED)
    draw_text(f'Score: {score}', WIDTH // 2, HEIGHT // 2 + 10)
    draw_text('Press SPACE to restart', WIDTH // 2, HEIGHT // 2 + 60, BLUE)
    draw_text('Press ESC to quit', WIDTH // 2, HEIGHT // 2 + 100, BLUE)
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                if event.key == pygame.K_ESCAPE:
                    return False
        clock.tick(FPS)

def main():
    while True:
        snake = Snake()
        food = Food()
        score = 0
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        snake.change_direction((0, -1))
                    elif event.key == pygame.K_DOWN:
                        snake.change_direction((0, 1))
                    elif event.key == pygame.K_LEFT:
                        snake.change_direction((-1, 0))
                    elif event.key == pygame.K_RIGHT:
                        snake.change_direction((1, 0))
            
            snake.move()
            
            # Check if snake ate food
            if snake.body[0] == food.position:
                snake.eat()
                food.respawn(snake.body)
                score += 10
            
            # Check collisions
            if snake.check_collision():
                running = False
            
            # Draw everything
            screen.fill(BLACK)
            
            # Draw grid
            for x in range(0, WIDTH, GRID_SIZE):
                pygame.draw.line(screen, (30, 30, 30), (x, 0), (x, HEIGHT))
            for y in range(0, HEIGHT, GRID_SIZE):
                pygame.draw.line(screen, (30, 30, 30), (0, y), (WIDTH, y))
            
            snake.draw()
            food.draw()
            
            # Draw score
            score_text = font.render(f'Score: {score}', True, WHITE)
            screen.blit(score_text, (10, 10))
            
            pygame.display.flip()
            clock.tick(FPS)
        
        # Game over
        if not game_over_screen(score):
            break
    
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
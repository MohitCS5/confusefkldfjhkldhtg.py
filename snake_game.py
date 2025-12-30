import pygame
import random

pygame.init()
w, h = 600, 400
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

snake = [[100, 100], [80, 100], [60, 100]]
food = [300, 200]
dx, dy = 20, 0
score = 0
game_over = False

#-----colors
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_SPACE:
                    # Reset game
                    snake = [[100, 100], [80, 100], [60, 100]]
                    food = [300, 200]
                    dx, dy = 20, 0
                    score = 0
                    game_over = False
            else:
                if event.key == pygame.K_UP and dy != 20:
                    dx, dy = 0, -20
                elif event.key == pygame.K_DOWN and dy != -20:
                    dx, dy = 0, 20
                elif event.key == pygame.K_LEFT and dx != 20:
                    dx, dy = -20, 0
                elif event.key == pygame.K_RIGHT and dx != -20:
                    dx, dy = 20, 0
    
    # Move snake
    if not game_over:
        head = [snake[0][0] + dx, snake[0][1] + dy]
        snake.insert(0, head)
        
        # Check food
        if head == food:
            score += 1
            food = [random.randrange(0, w//20)*20, random.randrange(0, h//20)*20]
        else:
            snake.pop()
        
        # Check walls/self
        if (head[0] < 0 or head[0] >= w or head[1] < 0 or head[1] >= h or 
            head in snake[1:]):
            game_over = True
    
    # Draw
    screen.fill(black)
    for segment in snake:
        pygame.draw.rect(screen, green, (segment[0], segment[1], 18, 18))
    pygame.draw.rect(screen, red, (food[0], food[1], 18, 18))
    
    # Score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, white)
    screen.blit(text, (10, 10))
    
    # Game over
    if game_over:
        text = font.render("Game Over - Space to restart", True, white)
        screen.blit(text, (w//2 - 150, h//2))
    
    pygame.display.flip()
    clock.tick(8)  # Slower speed

pygame.quit()

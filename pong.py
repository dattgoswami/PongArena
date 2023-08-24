import pygame
import random

pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 55)

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
        self.change_x = random.choice([-1, 1]) * 5
        self.change_y = random.choice([-1, 1]) * 5

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.y <= 0 or self.rect.y >= SCREEN_HEIGHT:
            self.change_y = -self.change_y

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([10, 60])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move_up(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    def move_down(self, pixels):
        self.rect.y += pixels
        if self.rect.y > SCREEN_HEIGHT - 60:
            self.rect.y = SCREEN_HEIGHT - 60

if __name__ == "__main__":
    ball = Ball()
    paddle_a = Paddle(10, SCREEN_HEIGHT // 2 - 30)
    paddle_b = Paddle(SCREEN_WIDTH - 20, SCREEN_HEIGHT // 2 - 30)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(ball, paddle_a, paddle_b)

    score_a = 0
    score_b = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle_a.move_up(5)
        if keys[pygame.K_s]:
            paddle_a.move_down(5)
        if keys[pygame.K_UP]:
            paddle_b.move_up(5)
        if keys[pygame.K_DOWN]:
            paddle_b.move_down(5)

        all_sprites.update()

        if pygame.sprite.collide_mask(ball, paddle_a) or pygame.sprite.collide_mask(ball, paddle_b):
            ball.change_x = -ball.change_x

        if ball.rect.x < 0:
            score_b += 1
            ball.rect.x = SCREEN_WIDTH // 2
            ball.change_x = random.choice([-1, 1]) * 5

        if ball.rect.x > SCREEN_WIDTH:
            score_a += 1
            ball.rect.x = SCREEN_WIDTH // 2
            ball.change_x = random.choice([-1, 1]) * 5

        screen.fill(BLACK)
        all_sprites.draw(screen)

        score_display = font.render(f"{score_a} - {score_b}", True, WHITE)
        screen.blit(score_display, (SCREEN_WIDTH // 2 - 50, 10))
        
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

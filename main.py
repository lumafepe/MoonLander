import pygame
import random
from preencher import moverNave

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
GROUND_HEIGHT = 40
GRAVITY = 0.05
THRUST = 1

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Lander Game')


# Lander class
class Lander:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 15
        self.width = 20
        self.height = 40
        self.image = pygame.transform.scale(pygame.image.load('lander.png'),
                                            (self.width, self.height))

    def draw(self):
        screen.blit(self.image,
                    (self.x - self.width / 2, self.y, self.width, self.height))

    def move(self, thrust_x, thrust_y):
        # Apply thrust and gravity
        self.vx += thrust_x * THRUST
        self.vy += thrust_y * THRUST

        self.vy += GRAVITY  # Gravity affects vertical velocity

        # Update position
        self.x += self.vx
        self.y += self.vy


# Generate mountains
def generate_mountains():
    points = []
    for x in range(0, WIDTH, 10):
        points.append((x, HEIGHT - GROUND_HEIGHT - random.randint(20, 100)))
    return points


# Find a random flat spot in the mountains
def generate_flat_spot(mountains):
    flat_start = random.randint(100, WIDTH - 200)
    flat_length = random.randint(50, 150)
    flat_y = min([
        y for x, y in mountains if flat_start <= x <= flat_start + flat_length
    ])

    for i in range(flat_start // 10, (flat_start + flat_length) // 10):
        mountains[i] = (mountains[i][0], flat_y)

    return flat_start, flat_length, flat_y, flat_start // 10, (
        (flat_start + flat_length) // 10) - 1


# Check if lander lands on flat spot
def check_landing(lander, flat_start, flat_length, flat_y):
    if flat_start <= lander.x <= flat_start + flat_length and lander.y + lander.height >= flat_y:
        if abs(lander.vx) < 1 and abs(lander.vy) < 1:
            return True
        return False
    return False


# Main game function
def game():
    clock = pygame.time.Clock()
    lander = Lander(WIDTH // 2, 20)
    is_first_run = True

    mountains = generate_mountains()
    flat_start, flat_length, flat_y, flat_index_start, flat_index_end = generate_flat_spot(
        mountains)

    running = True
    landed = False

    while running:
        screen.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Controls
        if is_first_run:
            is_first_run = False
        else:

            thrust_x, thrust_y = moverNave(lander.x, lander.y, lander.vx,
                                           lander.vy, flat_start,
                                           flat_start + flat_length, flat_y,
                                           GRAVITY)

            if thrust_x > 1 or thrust_x < -1:
                print(
                    "Erro: O movimento lateral deve ser um valor entre -1 e 1")
                exit()
            elif thrust_y > 1 or thrust_y < 0:
                print(
                    "Erro: O movimento vertical deve ser um valor entre 0 e 1")
                exit()
            else:
                thrust_y = -thrust_y

            # Move the lander
            lander.move(thrust_x, thrust_y)

        # Draw mountains
        mountains_image = pygame.image.load("moon-surface.png").convert_alpha()
        mountains_masked_result = mountains_image.copy()
        mountains_mask_surface = pygame.Surface((WIDTH, HEIGHT))
        pygame.draw.polygon(mountains_mask_surface, WHITE,
                            [(0, HEIGHT)] + mountains + [(WIDTH, HEIGHT)])
        pygame.draw.aalines(mountains_mask_surface, WHITE, True,
                            [(0, HEIGHT)] + mountains + [(WIDTH, HEIGHT)])
        mountains_masked_result.blit(mountains_mask_surface, (0, 0), None,
                                     pygame.BLEND_RGBA_MULT)
        screen.blit(mountains_masked_result, (0, 0))
        # Draw flat spot
        #pygame.draw.rect(screen, RED, (flat_start, flat_y, flat_length, HEIGHT - flat_y))

        # Draw lander
        lander.draw()

        # Check for landing
        if lander.y + lander.height >= flat_y:
            if check_landing(lander, flat_start, flat_length, flat_y):
                landed = True
                font = pygame.font.SysFont(None, 55)
                win_text = font.render("You Landed Safely!", True, GREEN)
                screen.blit(win_text, (WIDTH // 3, HEIGHT // 2))
            else:
                landed = True
                font = pygame.font.SysFont(None, 55)
                lose_text = font.render("Crash! Game Over!", True, RED)
                screen.blit(lose_text, (WIDTH // 3, HEIGHT // 2))

        # Refresh screen
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

        if landed:
            pygame.time.wait(3000)
            running = False


# Run the game
while True:
    game()

# Quit Pygame
pygame.quit()


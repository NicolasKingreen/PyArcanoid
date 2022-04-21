import pygame
from pygame.locals import *

import random
import sys

pygame.init()

# window properties
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 520, 450
TARGET_FPS = 60

# loading sprites
BLOCK_1_SPRITE = pygame.image.load("images/block01.png")
BACKGROUND_SPRITE = pygame.image.load("images/background.jpg")
BALL_SPRITE = pygame.image.load("images/ball.png")
PADDLE_SPRITE = pygame.image.load("images/paddle.png")

# x by x block grid
BLOCKS_AMOUNT = 10


class Application:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Arcanoid")
        self.display_surface = pygame.display.set_mode(SCREEN_SIZE)
        self.is_running = False

        # paddle properties
        self.pad_rect = PADDLE_SPRITE.get_rect(topleft=(300, 440))

        # ball properties
        self.ball_rect = BALL_SPRITE.get_rect(topleft=(300, 300))
        self.dx = 6
        self.dy = 5

        # blocks grid
        self.blocks = []
        for i in range(1, BLOCKS_AMOUNT):
            for j in range(1, BLOCKS_AMOUNT):
                block = pygame.math.Vector2(i * 43, j * 20)
                self.blocks.append(block)

    def run(self):
        self.is_running = True
        while self.is_running:

            frame_time_ms = self.clock.tick(TARGET_FPS)

            # window close event
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.terminate()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.terminate()

            # paddle movement
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_a]:
                self.pad_rect.x -= 6
            if pressed_keys[K_d]:
                self.pad_rect.x += 6

            # x ball movement and collision
            self.ball_rect.x += self.dx
            for block in self.blocks:
                block_rect = BLOCK_1_SPRITE.get_rect(topleft=block)
                if self.ball_rect.colliderect(block_rect):
                    block.x = -100
                    self.dx = -self.dx

            # y ball movement and collision
            self.ball_rect.y += self.dy
            for block in self.blocks:
                block_rect = BLOCK_1_SPRITE.get_rect(topleft=block)
                if self.ball_rect.colliderect(block_rect):
                    block.x = -100
                    self.dy = -self.dy

            # ball screen borders collision
            if self.ball_rect.left < 0 or self.ball_rect.right > SCREEN_WIDTH:
                self.dx = -self.dx
            if self.ball_rect.top < 0 or self.ball_rect.bottom > SCREEN_HEIGHT:
                self.dy = -self.dy

            # ball-pad collision
            if self.ball_rect.colliderect(self.pad_rect):
                self.dy = -(random.randint(2, 5))

            # drawings
            self.display_surface.blit(BACKGROUND_SPRITE, (0, 0))
            self.display_surface.blit(BALL_SPRITE, self.ball_rect)
            self.display_surface.blit(PADDLE_SPRITE, self.pad_rect)
            for block in self.blocks:
                self.display_surface.blit(BLOCK_1_SPRITE, block)
            pygame.display.update()

        pygame.quit()
        sys.exit()

    def terminate(self):
        self.is_running = False


if __name__ == "__main__":
    Application().run()

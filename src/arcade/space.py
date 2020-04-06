import arcade
import os
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprites and Periodic Bullets Example"

PLAYER_IMAGE = ":resources:images/space_shooter/playerShip1_orange.png"
ENEMY_IMAGE = ":resources:images/space_shooter/playerShip1_green.png"

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.BLACK)

        # --- Keep track of a frame count.
        # --- This is important for doing things every x frames
        self.frame_count = 0
        self.current_frame = 0

        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # Add player ship
        self.player = arcade.Sprite(PLAYER_IMAGE, 0.5)
        self.player_list.append(self.player)

        # Add Enemies
        for width_fraction in [0.25, 0.5, 0.75]:
            self.spawn_enemy(SCREEN_WIDTH * width_fraction)

    def on_draw(self):
        """Render the screen. """
        arcade.start_render()
        self.enemy_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()

    def on_update(self, delta_time):
        """All the logic to move, and the game logic goes here. """

        # --- Add one to the frame count
        self.frame_count += 1

        # Loop through all players (for this game we only have one player)
        for player in self.player_list:
            if arcade.check_for_collision_with_list(player, self.bullet_list):
                self.player_list.remove(player)

        # Loop through each enemy that we have
        for enemy in self.enemy_list:
            enemy.center_x += enemy.speed

            # Handle Enemy - Bullet Collisions
            if arcade.check_for_collision_with_list(enemy, self.bullet_list):
                self.enemy_list.remove(enemy)

            # Change direction every 30 frames
            if self.frame_count % 30 == 0:
                self.move_enemy(enemy)

            # Fire bullet every 60 frames
            if self.frame_count % 60 == 0:
                self.spawn_bullet(enemy, -1)

        # Loop through each bullet that we have
        for bullet in self.bullet_list:
            # Get rid of the bullet when it flies off-screen
            if bullet.top < 0:
                bullet.remove_from_sprite_lists()

        # Update all bullets
        self.bullet_list.update()

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        self.player.center_x = x
        self.player.center_y = 20

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        """
        if self.frame_count > self.current_frame + 120:
            self.current_frame = self.frame_count
            if key == arcade.key.SPACE:
                self.spawn_bullet(self.player, 1)

    def spawn_enemy(self, x):
        """Spawn enemy at given x co-ordinate"""
        enemy = arcade.Sprite(ENEMY_IMAGE, 0.5)
        enemy.center_x = x
        enemy.center_y = SCREEN_HEIGHT - enemy.height
        enemy.angle = 180
        enemy.speed = 0
        self.enemy_list.append(enemy)

    def move_enemy(self, enemy):
        margin = 240
        speed = 5
        if enemy.center_x < margin:
            enemy.speed = speed
        elif enemy.center_x > SCREEN_WIDTH - margin:
            enemy.speed = -1 * speed
        else:
            enemy.speed = random.choice([-1 * speed, speed])

    def spawn_bullet(self, ship, direction):
        """Spawns a bullet. +1 travels up, -1 travels down."""
        bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png")
        bullet.center_x = ship.center_x
        bullet.angle = 90 * direction
        bullet.top = ship.bottom
        bullet.change_y = 5 * direction

        if direction == 1:
            bullet.bottom = ship.top
        else:
            bullet.top = ship.bottom

        self.bullet_list.append(bullet)

MyGame()
arcade.run()

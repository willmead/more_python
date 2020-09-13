import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Chess Timer"


class Timer(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.times = [10, 10]
        self.current_player = 0
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()

        output_0 = f"Player 1: {self.times[0]:.0f}"
        output_1 = f"Player 2: {self.times[1]:.0f}"

        arcade.draw_text(output_0, 150, 300, arcade.color.BLACK, 30)
        arcade.draw_text(output_1, 450, 300, arcade.color.BLACK, 30)

    def on_update(self, delta_time):
        self.times[self.current_player] -= delta_time

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.current_player = (self.current_player + 1) % 2


window = Timer()
arcade.run()

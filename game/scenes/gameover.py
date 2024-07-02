class GameOver:
    def __init__(self):
        self.text = "you lose"
        self.bg_colour = (30, 30, 30)

    def handle_input(self, event):
        self.text = "you lose"

    def update(self):
        pass


    def render(self, screen):
        screen.fill(self.bg_colour)

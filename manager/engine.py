from view.view import init
from models.world import World

class GameEngine:
    def __init__(self):
        self.world = World()

    def start_game(self):
        self.world.generate_world()


            
            
            
        
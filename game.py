import pygame

class Game:
    """
    This class is responsible for managing the game, for example
    it is responsible for starting and stopping the game, handling inputs to 
    said game and other such processes. There can only be one game class, 
    hence it is a singleton. 
    """
    block_size = 8  # one block 8px by 8px
    # units are blocks
    map_h = 64 # 2d map of player moving with walls. Height of the map?
    map_w = 32 # width of the map?
    # units are pixels
    win_h = 1024 # total pixel height of game window
    win_w = 512 # same but for width

    def __new__(cls, *args, **kwds):
        """
        Ensures that there is only one instance of the class,
        because there can only be one game object.
        """
        if not hasattr(cls, '_instance'):
            cls._instance = super(Game, cls).__new__(cls, *args, **kwds)
        return cls._instance

    def __init__(self, setup={}):
        """

        """
        assert isinstance(setup, dict)
        assert all(isinstance(x, int) and x > 0 for x in setup.values()) # values can't be 0 and non-integer

        win_h = setup.get("win_h", win_h)
        win_w = setup.get("win_w", win_w)
        block_size = setup.get("block_size", block_size)

        assert win_h % block_size == 0
        assert win_w % block_size == 0
        # assert map_h % 
        
        pygame.init()

        self._screen = pygame.display.set_mode((win_w, win_h))
        self._clock = pygame.time.Clock()
        self._running = True

    def draw_map():
        pass


    def run_loop():
        pass

    def handle_input():
        pass

    def exit():
        pass
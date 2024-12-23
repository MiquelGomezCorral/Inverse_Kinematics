from dataclasses import dataclass

@dataclass
class Settings:
    BACKGROUND_COLOR: tuple[int] = (23, 56, 102)
    REFERENCE_FPS: int = 1200

    WIDTH: float = 1024
    HEIGHT: float = 1024
    MARGIN: float = 100

    MOVING_SPEED: float = 0.5

    SMOOT_FACTOR: float = 0.05
    N_TENTACLES: int = 5
    N_LIMBS: int = 5
    TOTAL_LENGTH: float = 500
    THICKNESS: float = 15
    MAX_BEND_LIMB: float = 10

@dataclass
class Colors:
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    DARK_BLUE = (23, 56, 102)
    LIGHT_BLUE = (68, 190, 242)

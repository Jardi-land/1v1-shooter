import configparser as cp

class Config:
    def __init__(self, config_file) -> None:
        self.MAX_HEALTH: int
        self.WEAPON_COOLDOWN: int
        self.GRAVITY_MODE: str
        
        self.death_cooldown: int
        self.end_screen_cd: int

        self.file = config_file
        self.load(self.file)

    def load(self, file):
        Cfg = cp.ConfigParser()
        Cfg.read(file)
        self.MAX_HEALTH = Cfg.get('Gameplay', 'MAX_HEALTH')
        self.WEAPON_COOLDOWN = Cfg.get('Gameplay', 'WEAPON_CD')
        self.GRAVITY_MODE = Cfg.get('Gameplay', 'GRAVITY_MODE')

        self.death_cooldown = Cfg.getint('GameConfig', 'DEATH_CD')
        self.end_screen_cd = Cfg.getint('GameConfig', 'ENDSCREEN_CD')



cfg = Config('config.ini')

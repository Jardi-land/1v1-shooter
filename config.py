import configparser as cp

class Config:
    def __init__(self, config_file) -> None:
        self.MAX_HEALTH: int
        self.WEAPON_COOLDOWN: int
        self.GRAVITY_MODE: str
        
        
        self.file = config_file
        self.load(self.file)

    def load(self, file):
        Cfg = cp.ConfigParser()
        Cfg.read(file)
        self.MAX_HEALTH = Cfg.get('GameVars', 'MAX_HEALTH')
        self.WEAPON_COOLDOWN = Cfg.get('GameVars', 'WEAPON_COOLDOWN')
        self.GRAVITY_MODE = Cfg.get('GameVars', 'GRAVITY_MODE')


cfg = Config('config.ini')

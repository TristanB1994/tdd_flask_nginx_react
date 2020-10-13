#services/users/project/config.py

class BaseConfig:
    """Base configuration"""
    pass

class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    TESTING = True

class ProductionConfig(BaseConfig):
    """Production configuration"""
    pass

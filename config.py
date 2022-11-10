import os 

class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL ="https://api.themoviedb.org/3/movie/{}?api_key={}"
    MOVIE_API_KEY = '242b84c8d52802538efe1de50a81b05d'
    SECRET_KEY = 'some key'
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:Yerasulbek2004@localhost/postgres"
    UPLOADED_PHOTOS_DEST = "app/static/photos"

    # email configurations
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # simplemde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    """
    Test configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    """
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://collins:11946@localhost/watchlist_test"

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:Yerasulbek2004@localhost/postgres"
    DEBUG = True

config_options = {
    "development": DevConfig,
    "production": ProdConfig,
    "test": TestConfig
}
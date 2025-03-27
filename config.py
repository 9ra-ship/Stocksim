#import os


#class Config(object):
 #   """Configuration for the app"""

#SQLALCHEMY_DATABASE_URI = os.environ.get(
 #   'DATABASE_URL', "postgresql://postgres:stockproject@localhost:5432/stocksim-db"
#)

#SQLALCHEMY_TRACK_MODIFICATIONS = False
#SQLALCHEMY_ECHO = False
#SECRET_KEY = os.environ.get("SECRET_KEY", "secretkey_local")
#DEBUG_TB_INTERCEPT_REDIRECTS = False
import os


class Config(object):
    """Configuration for the app"""

    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:stockproject@localhost:5432/stocksim-db".replace("postgres://", "postgresql://", 1)
    print(SQLALCHEMY_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SECRET_KEY = "IYhz0yHeP9zWsUV5VkdCbB4DFIrkKwcm4sAM651Z"
    DEBUG_TB_INTERCEPT_REDIRECTS = False



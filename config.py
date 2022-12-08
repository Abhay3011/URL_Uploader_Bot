import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("BOT_TOKEN", "5989031691:AAE2bAYkf8imF855W9QWxyFpX0MAjc6HZyU") # Make a bot from https://t.me/BotFather and enter the token here
    
    APP_ID = int(os.environ.get("API_ID", "9544521")) # Get this value from https://my.telegram.org/apps
    
    API_HASH = os.environ.get("API_HASH", "5cf32e97dc94510e46524f2286c95116") # Get this value from https://my.telegram.org/apps
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "1358657527")) # Your(owner's) telegram id
    
    MONGO_STR = os.environ.get("MONGO_STR", "mongodb+srv://test:test@cluster0.09gee3a.mongodb.net/?retryWrites=true&w=majority") # Get from MongoDB Atlas

    DOWNLOAD_LOCATION = "app//DOWNLOADS//" # The download location for users. (Don't change anything in this field!)

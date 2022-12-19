class Config(object):
    LOGGER = True

  # Get this value from my.telegram.org/apps
    API_ID = 22270544
    API_HASH = "12fd6c5d681c662e28da50bbcb8ebd06"

    CASH_API_KEY = "AODBD27CNF8D2I"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://ydflceto:AHStxsAqXBZK2ANvuL32GBxjzF1MbN4N@mel.db.elephantsql.com/ydflceto"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001548616072)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb://mongo:eZsAIhOmfjc1IklOmwOj@containers-us-west-158.railway.app:7165"  # Get ths value from cloud.mongodb.com

  # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/8312d1ac6a1f769ba425a.jpg"

    SUPPORT_CHAT = "hindi_english_chatting_xD"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5950919429:AAHLcyUz-qESC104UlleoZXD9UCdhZ9MPgk"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "WOFB20FBW0XNQ1DN"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 5803150076  # User id of your telegram account (Must be integer)

  # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = (8)

class Production(Config):
    LOGGER = True

class Development(Config):
    LOGGER = True

class Config(object):
    LOGGER = True

    API_ID = 
    API_HASH = ""
    TOKEN = ""
    OWNER_ID = 
    OWNER_USERNAME = ""
    SUPPORT_CHAT = ""
    JOIN_LOGGER = ()
    EVENT_LOGS = ()

    DB_URI = ""
    MONGO_DB_URI = ""
    LOAD = []
    NO_LOAD = ["rss"]
    WEBHOOK = False
    INFOPIC = True
    URL = None

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = 
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = 
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = 
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = 
    WOLVES = 

    DONATION_LINK = ""
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    ALLOW_EXCL = True
    CASH_API_KEY = ""
    TIME_API_KEY = ""
    SPAMMERS = None
    ALLOW_CHATS = True
    START_IMG = "https://te.legra.ph/file/ffd0e51afa72af992ab12.jpg"
    HEROKU_API_KEY = None
    HEROKU_APP_NAME = None
    TEMP_DOWNLOAD_DIRECTORY = "./"
    ARQ_API_KEY = "LJMETG-DPHBCX-DGHJCD-TMFIGB-ARQ"
    ARQ_API_URL = "https://arq.hamker.in"
    ALLOW_EXCL = None
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

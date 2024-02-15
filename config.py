from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "22225617"))
API_HASH = getenv("API_HASH", "ef16f7597376f1689663304c954e4493")

BOT_TOKEN = getenv("BOT_TOKEN", "6752162515:AAF3t_0lR9F08-1czfMpy4vf_kxtThA3haQ")
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

OWNER_ID = int(getenv("OWNER_ID", "6072149828"))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/MrAK_LinkZz")

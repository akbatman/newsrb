# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "11978076"))
API_HASH = getenv("API_HASH", "bc7a1ff026c4305bcf4f38807aabbec5")
BOT_TOKEN = getenv("BOT_TOKEN", "7011801575:AAEMFzMCkY4chFms4APxFvh_lZDYlK26LH0")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5264572437").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://ffdr44:ffdr44@cluster0.utngb9a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002084218578")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002084218578"))

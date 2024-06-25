# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "11978076"))
API_HASH = getenv("API_HASH", "bc7a1ff026c4305bcf4f38807aabbec5")
BOT_TOKEN = getenv("BOT_TOKEN", "7011801575:AAEMFzMCkY4chFms4APxFvh_lZDYlK26LH0")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5264572437").split()))
MONGO_DB = getenv("MONGO_DB", "AQC2xVwAt5TKeq9_p3kKS7CBrd3P8F3KHFBgHVC5ElcY9tZByDZkN-BaxbvIolTfIhgNEF60Rp769R1lP00sSe4iiHlXH17qwi171BcypUP4_Xrr6vkKUH2o5ixG8j9iF1qk7-vNUCVNkxZflk3GiL6jtyzopJ67SUWYxS7uup5oGIq54y2Jkzp9q8Kc6HnLIoUq_2OvMTR675Gdx7sH80FCIyzZbM1hWcljZtkU5vb2KqjhBNPKEVRYm-6S1mi8mpCp6obf8iCS9GMyr8AaZ3kG-88FxjuNm0hwxjSIV7E_F9TL-yMMdlEV9bopK6n3sEDvp2E7ubRFolLilVX9eEODkGpDFwAAAAE5ywAVAA")
LOG_GROUP = getenv("LOG_GROUP", "-1002084218578")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002084218578"))

import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "7946647"))
    API_HASH = os.environ.get("API_HASH", "3d564ea96a493b54f8aa5ebb3408bb9f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6063715300:AAF4lLZBi--8xRWm-mPRPkkZyl0S38HyH2A")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQALXLszKvFehR7CpmBHIW2rqt4_lZOhFRgyDwM9CidZa_KDPY3B_pCGlvjEapuJytMmtv8EXtxFSQ8zPOF9m74SIJJmarjF-fzgD7Rao1BTcM5HdhkCoyk-_vpBWXD4Zfg41p1z_81XLY40OT1QHo8AdO_Mwp8aiqEQ2xBNteoZeL_HLKjMso0YVO6s5C9ewZgJdR3na2FrRK9r6CkWQFsNKzHH28RDIvNnq6clxqbE_oCWM_XBPNzvdCz-YuERQYkV9pCERGGjc7CMFjF3sVHoKYauiUThFcuIuhyINmW3yganglPJpIWbbbR30aQRHeRwj8oytOykOsI1-OQF1K_ba_7VcwA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Yunus_Music1_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "1811862899")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"

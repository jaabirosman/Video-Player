##Config

from os import getenv

from dotenv import load_dotenv

load_dotenv()
SESSION_NAME = getenv('SESSION_NAME', 'BAACRFmkdxY_JlcXTn7RVSuKPQxwqGBiI0QX0FIv_wflLe1tqQEc22g7wvZizGb2vix0qjcqcDPVvcwKeBGp_ypFhLd5osVnMvg8rc_WidAmjactq0zfSItxMuaZ-Bp_H1YbrS_4q5hHW1K9t9iLpprsiEqpQaaV4_cuVPGk2-i-IiPxn9l-4CnoSBoMgq8Skr6n09Nf5nNm-Uj0rMg3Olp5ekxDrzWOq5JNj328qaokh8-Y6_ILt563CjFs6S_0trCylD9R-b_bGRb2z4wmkceYpTjk1vmpd0K_A3GUBHGpbLyMuQmP9WoUhqOtBiYpBRvkAEkIjww3fIGDIp9fxh8uAAAAATTDl_YA')
BOT_TOKEN = getenv('BOT_TOKEN', '5218047095:AAF96BLvhSAagO3WNAY_j3-a8lY6ux9Ws48')
API_ID = int(getenv('API_ID', '15499461'))
API_HASH = getenv('API_HASH','ff93948d3b7c3091e8d573275a4ed80f')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '54000'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ . , : ; !').split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Mosia_Mk_Bot:mosia@cluster0.91lut.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '1008271006').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001150107625'))
ASS_ID = int(getenv("ASS_ID", '5180200950'))
OWNER_ID = list(map(int, getenv('OWNER_ID', '1008271006').split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "osmanigroupbot")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "teamosmani")
GROUP = getenv("GROUP", "osmanigroupbot")
CHANNEL = getenv("CHANNEL", "teamosmani")

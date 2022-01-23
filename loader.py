from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from utils.db_api import database
from utils.db_api import users
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

usrs = users.Db()
usrs.create_table_users()
usrs.update_admin(id=1094578892, admin=1)
ege_math = database.Database("data/ege_math.db", "ege_math", 18)
ege_math.initialize()

refinf = database.Reference_information("data/reference_information.db", "default", 50)
refinf.initialize()
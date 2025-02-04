from environs import Env
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent


env = Env()
env.read_env()

with env.prefixed("BOT__"):
    TOKEN = env.str("TOKEN", "")


TG_MANAGER_ID = env.int("TG_MANAGER_ID", 0)

import sqlite3
from telethon import TelegramClient
import time
from dataclasses import dataclass
db_file = 'auto.db'
@dataclass
class Config:

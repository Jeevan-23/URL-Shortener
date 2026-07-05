from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = int(os.getenv("SECRET_KEY"))
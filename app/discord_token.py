import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")
token = os.getenv('TOKEN')

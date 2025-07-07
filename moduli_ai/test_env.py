from dotenv import load_dotenv
import os

load_dotenv()
print("USER:", os.getenv("LIVEONPLUS_USER"))
print("PASS:", os.getenv("LIVEONPLUS_PASSWORD"))

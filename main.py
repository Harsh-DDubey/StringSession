from pyrogram import Client as c
from dotenv import load_dotenv
import os

load_dotenv()

API_ID = int(os.getenv("API_ID"))  
API_HASH = os.getenv("API_HASH")

print("\n\n Enter Phone number when asked.\n\n")

i = c("wbb", api_id=API_ID, api_hash=API_HASH, in_memory=True)

with i:
    ss = i.export_session_string()
    print("\nHERE IS YOUR STRING SESSION, COPY IT, DON'T SHARE!!\n")
    print(f"\n{ss}\n")

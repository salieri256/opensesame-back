from fastapi import FastAPI
from src.routers import user, log, door
import nfc
from src.libs.read_nfc_id import onConnected

app = FastAPI()

app.include_router(user.router)
app.include_router(log.router)
app.include_router(door.router)

clf = nfc.ContactlessFrontend('usb')
clf.connect(rdwr={'on-connected': onConnected})
clf.close()
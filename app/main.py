from fastapi import FastAPI
import uvicorn
from . import config

app = FastAPI(title="A FastAPI Project")

if __name__ == "__main__" and not config.DEBUG:
    uvicorn.run(app, host="0.0.0.0", port=1228)

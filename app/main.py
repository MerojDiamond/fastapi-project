import uvicorn
from fastapi import FastAPI

import app.config as config

app = FastAPI(title="A FastAPI Project")

if __name__ == "__main__" and not config.DEBUG:
    uvicorn.run(app, host="0.0.0.0", port=1228)

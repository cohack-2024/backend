import uvicorn
from fastapi import FastAPI


app = FastAPI()

uvicorn.run(app, host="0.0.0.0", port=80)

from fastapi import FastAPI

app = FastAPI()

@app.get('/replay/{sym}')
async def get_coin_data(sym: str):
    # call relay engine
    pass 

@app.get('/health')
async def get_health():
    return {"status":"running"}

from fastapi import FastAPI

app = FastAPI(title="MyGameVault API", version="0.1.0")

@app.get("/test")
def test() -> dict[str, str]:
    return {"status": "LUFERACHO"}




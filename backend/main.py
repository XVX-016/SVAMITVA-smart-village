from fastapi import FastAPI

app = FastAPI(title="SVAMITVA Smart Village Intelligence Platform")

@app.get("/")
def root():
    return {"status": "Backend running"}

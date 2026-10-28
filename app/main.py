from fastapi import FastAPI
app = FastAPI(title="Flame-in-Free-Fall")
@app.get("/")
def root():
    return {"message": "Flame in Freefall - NASA Space Apps 2026 - Team Umbra0nxy", "docs": "/docs", "note": "Not an operational safety system"}
@app.get("/search")
def search(q: str):
    return {"query": q, "results": [{"exp": "FLEX-1", "fuel": "n-heptane", "note": f"Blue spherical flame for {q}"}]}


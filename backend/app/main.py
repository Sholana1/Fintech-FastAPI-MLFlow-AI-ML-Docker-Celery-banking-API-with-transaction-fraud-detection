from fastapi import FastAPI

app = FastAPI(
    title="Flow Bank",
    description="Flow banking API built with FastAPI"
)

@app.get("/")
def home():
    return {"message": "Welcome to the flow bank api"}
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI CI/CD!"}

@app.get("/ai")
def ai_info():
    return {"future_role": "AI Engineer", "name": "MohammadHossein"}

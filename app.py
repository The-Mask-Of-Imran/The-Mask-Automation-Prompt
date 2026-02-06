from fastapi import FastAPI

app = FastAPI(title="The Mask Automation - Core")

@app.get("/")
def root():
    return {"message": "The Mask Automation Core is running on Render!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
from fastapi import FastAPI

# This creates our application. Everything else attaches to it.
app = FastAPI(title="Real-Time Meeting Intelligence Engine")


# "@app.get" means: when a browser sends a GET request to this URL,
# run the function below and send back what it returns.
@app.get("/api/health")
def health_check():
    return {"status": "ok", "message": "Backend is running"}
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="SchedulerRX API")

# Configure CORS (This allows your React frontend to talk to this backend)
origins = [
    "http://localhost:5173",  # Your local React app
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to SchedulerRX API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
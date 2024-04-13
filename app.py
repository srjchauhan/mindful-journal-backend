# create fast api app
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import journal, user

app = FastAPI(
    title="Journal",
    description="Journal",
    version="1.0.0",

)
app.include_router(journal.router)
app.include_router(user.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "healthy"}



if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", reload=True ,host="0.0.0.0", port=8000)
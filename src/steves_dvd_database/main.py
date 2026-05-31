
import uvicorn


def main():
    uvicorn.run(
        "steves_dvd_database.app:app",
        host="127.0.0.1",
        port=8000,
        reload=False,
    )

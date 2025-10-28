from route import app_routes


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app_routes.app, host="127.0.0.1", port=8008)
import uvicorn


if __name__ == '__main__':
    uvicorn.run("core:app", port=8000, reload=True)
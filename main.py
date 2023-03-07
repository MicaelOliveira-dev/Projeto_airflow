import uvicorn


def inicia_api():
    if __name__ == '__main__':
        uvicorn.run("app:app", host="0.0.0.0", port=8000)


inicia_api()
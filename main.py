from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def get_start() -> dict[str, str]:
    return {
        'Первое сообщение' : 'Здесь будет красиво'
    }

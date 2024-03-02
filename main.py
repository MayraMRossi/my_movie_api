from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from middlewares.jwt_bearer import JWTBearer
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI()
#TITULO SWAGGER
app.title = 'Mi Aplicación con FastAPI'
app.version = '0.0.1'



app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)


Base.metadata.create_all(bind=engine)



movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': 'En un exuberante planeta llamado Pandora...',
        'year': 2009,
        'rating': 7.8,
        'category': 'Accion'
    },
    {
        'id': 2,
        'title': 'Avatar',
        'overview': 'En un exuberante planeta llamado Pandora...',
        'year': 2009,
        'rating': 7.8,
        'category': 'Accion'
    }
]

# METODO GET
@user_router.get('/',tags=['home'])
def message():
#    return {'saludo':'Hello May'}
    return HTMLResponse('<h1>Hello May</h1>')
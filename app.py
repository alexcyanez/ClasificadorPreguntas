from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from utils import clasificar, generar_respuesta
from utils import Pregunta, Respuesta


app = FastAPI()

c = [
	'legal',
	'contable',
	'medica'
]


@app.get('/')
def index(): 
	return {"message": "Hello user!"}


@app.post('/preguntar', response_model=Respuesta)
def preguntar(p: Pregunta):
	clase = clasificar(p.pregunta)
	if clase not in c:
		raise HTTPException(
			status_code=400,
		 	detail='La pregunta no está dentro de las categorias, por favor intente con otra pregunta'
		 	)
	resp = generar_respuesta(clase, p.pregunta)

	return Respuesta(categoria=clase, respuesta=resp)
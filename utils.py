import os
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

# Se carga el archivo .env y en caso de que no se cuente con uno, se puede agregar la variable directamente
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY', 'TuClaveSINoTienes.env')

#Se selecciona el modelo a usar y se inicializa OpenAi

MODEL = 'gpt-4o-mini'
openai = OpenAI()

# Se crean las categorias y los promts a utilizar en base a cada una de las categorias:
#Se crea una lista con las categorias:

categorias = [
	'legal',
	'contable',
	'medica'
]

# Creo tres templates de prompts, uno para cada categoria

prompts_cat = {
	"legal": "Eres un abogado experto. Responde profesionalmente a la siguiente consulta legal (si no conoce la respuesta dilo): \n\n{pregunta}",
	"contable": "Eres un contador experto. Brinda una reespuesta clara y no muy técnica a la siguiente consulta contable (si no conoces la respuesta dilo):\n\n{pregunta}",
	"medica": "Eres un médico general con gran experiencia. Da una respuesta comprensible para público no médico a la siguiente consulta médica(si no conoces la respuesta dilo):\n\n{pregunta}"
}

# Después creo dos modelos basados en el BaseModel de pydantic para dar una estructura a la respuesta
class Pregunta(BaseModel):
	pregunta: str # Se agrega el tipo de dato ya que es un requisito de pydantic

class Respuesta(BaseModel):
	categoria: str
	respuesta: str

prompt_clasificador = """Clasifica la siguiente pregunta en alguna de las siguientes categorias: 'legal', 'contable', 'medica' u 'otro'.
	Pregunta: {q}
	Debes contestar con una sola palabra de las categorias antes mencionadas
	"""

def clasificar(pregunta: str) -> str:
	""" la función recibe un string pregunta : str, lo manda a la API de OpenAI
	para clasificar en uno de las categorias definidas y
	devuelve un string con una de las categorias definidas.
	"""
	sys_promt = "Eres un experto clasificador de preguntas."
	completion = openai.chat.completions.create(
			model = MODEL,
			messages = [
				{"role": "system", "content":sys_promt},
				{"role": "user", "content": prompt_clasificador.format(q=pregunta)}
			]
		)
	cat = completion.choices[0].message.content

	return cat


def generar_respuesta(categoria:str, pregunta:str) -> str:
	""" 
		La función recibe una categoria: str y la pregunta:str para poder contestarla
		Devuelve un string que es la respuesta a la pregunta de entrada
	"""
	sys_prompt = "Eres un experto asistente en el área correspondiente."
	prompt = prompts_cat[categoria].format(pregunta=pregunta)
	completion = openai.chat.completions.create(
			model = MODEL,
			messages = [
				{"role": "system", "content":sys_prompt},
				{"role": "user", "content": prompt}
			],
			temperature = 0.5
		)
	respuesta = completion.choices[0].message.content
	return respuesta

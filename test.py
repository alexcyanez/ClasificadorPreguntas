import requests
import json

url = 'http://127.0.0.1:8000/preguntar'

headers = {
	'accept': 'application/json',
	'Content-Type': 'application/json'
}

pregunta1 = {
	"pregunta": "A que rama del derecho pertenece la compra-venta?" 
} # Bien clasificada

pregunta2 = {
	"pregunta": "¿Qué es litigio?"
} # Bien clasificada

pregunta3 = {
	"pregunta": "¿Qué hacer en caso de una fractura?"
}

pregunta4 = {
	"pregunta": "¿Cómo funciona el paracetamol?"
}

pregunta5 = {
	"pregunta": "¿Cómo debo llevar la contabilidad de mi empresa?"
}

pregunta6 = {
	"pregunta": "¿Me puedes ayudar a crear un estado financiero?"
}


response = requests.post(
		url = url,
		headers = headers,
		data = json.dumps(pregunta3)
	)

print(response.json())
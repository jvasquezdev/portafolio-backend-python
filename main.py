from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Inicialización de la aplicación FastAPI
app = FastAPI(
    title="Motor Computacional Python",
    description="Microservicio encargado de generar secuencias matemáticas complejas."
)

# Configuración de políticas CORS para permitir la conexión del Orquestador (Angular)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/fibonacci")
def get_fibonacci_sequence():
    """
    Genera los primeros 50 números de la secuencia de Fibonacci.

    Returns:
        Un diccionario JSON estructurado con coordenadas (x: iteración, y: valor),
        optimizado para ser renderizado por librerías de gráficos en el frontend.
    """
    limit = 50
    sequence = []
    a, b = 0, 1

    for i in range(limit):
        # Estructuramos el dato pensando en los ejes X e Y del futuro gráfico
        sequence.append({
            "iteration": i,
            "value": a
        })
        a, b = b, a + b

    return {"source": "Python 3.10+", "data": sequence}
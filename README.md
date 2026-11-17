# portafolio-backend-python
# 🐍 Servicio de Cálculo con Python y FastAPI

Este repositorio (`portafolio-backend-python`) es un microservicio desarrollado con **Python** y **FastAPI**. Su función es procesar cálculos matemáticos y devolver los resultados en formato JSON para que el frontend de Angular pueda consumirlos.

En esta versión, el servicio calcula la secuencia de Fibonacci y expone los datos necesarios para su visualización con Chart.js en el frontend.

## 🏛️ Rol en la arquitectura

Este microservicio se ejecuta en el puerto `8000` y es consumido por el cliente [portafolio-frontend](https://github.com/jvasquezdev/portafolio-frontend).

Recibe peticiones HTTP, ejecuta el cálculo solicitado y devuelve una respuesta en formato JSON. El frontend utiliza estos datos para renderizar la información de forma dinámica con Chart.js.

## 🚀 Requisitos previos

Para ejecutar este proyecto localmente necesitas:

- **Python 3.10 o superior**
- **Pip**
- **python3-venv** para crear entornos virtuales en Debian/Ubuntu

## ⚙️ Instalación y configuración

Se recomienda ejecutar el proyecto dentro de un entorno virtual para no instalar las dependencias de forma global en tu sistema.

1. Clona el repositorio:

```bash
git clone [https://github.com/jvasquezdev/portafolio-backend-python.git](https://github.com/jvasquezdev/portafolio-backend-python.git)
cd portafolio-backend-python
```

2. Crea el entorno virtual:

```bash
python3 -m venv .venv
```

3. Activa el entorno virtual:

En Linux, WSL o macOS:

```bash
source .venv/bin/activate
```

En Windows con PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

4. Instala las dependencias:

```bash
pip install fastapi uvicorn
```

## 🏃‍♂️ Ejecución del servidor

Ejecuta el servicio en el puerto `8000` para que el frontend pueda comunicarse correctamente con este backend:

```bash
uvicorn main:app --port 8000 --reload
```

La API estará disponible en:

```text
http://localhost:8000/api/fibonacci
```

También puedes acceder a la documentación interactiva generada automáticamente por FastAPI en:

```text
http://localhost:8000/docs
```

## 🛠️ Tecnologías utilizadas

- **Lenguaje:** Python 3
- **Framework:** FastAPI
- **Servidor ASGI:** Uvicorn
- **Formato de respuesta:** JSON
- **Visualización:** Los datos son consumidos por Chart.js en el frontend

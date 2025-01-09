# Elige Tu Propia AventurIA

Genera libros interactivos al estilo "Elige tu propia Aventura" utilizando algoritmos de Machine Learning. Este proyecto cuenta con un frontend en [Next.js](https://nextjs.org/) para la experiencia interactiva y un backend en Python para la generación de contenido basado en ML.

## 🚀 Características

- **Generación de Historias**: Crea narrativas personalizadas y ramificadas basadas en entradas del usuario.
- **Interfaz Intuitiva**: Diseñada con Next.js para ofrecer una experiencia visual atractiva y responsiva.
- **Modelo de ML**: Utiliza modelos de lenguaje como GPT para generar texto coherente y creativo.
- **Selección de Opciones**: Permite a los usuarios decidir el curso de la historia en tiempo real.
- **API REST**: Backend en Python con FastAPI para manejar la lógica y las solicitudes del frontend.

## 🛠️ Tecnologías Usadas

### Frontend
- **[Next.js](https://nextjs.org/)**: Framework React para construir interfaces de usuario.
- **TailwindCSS**: Estilización moderna y responsiva.
- **Axios**: Para realizar solicitudes al backend.

### Backend
- **[Python](https://www.python.org/)**: Lenguaje base del backend.
- **Flask**: Framework para crear APIs rápidas y escalables.
- **Langchain**: Para modelos de Machine Learning.
- **Hugging Face Transformers**: Modelos de lenguaje pre-entrenados.

### Infraestructura
- **Docker**: Para contenerización y despliegue.

## ⚙️ Instalación y Configuración

### Requisitos Previos
- Node.js (v16+)
- Python (v3.9+)
- Docker y Docker Compose
- Yarn o npm para el frontend

### Clonar el Repositorio
```bash
git clone https://github.com/tuusuario/elige-tu-propia-aventura-ml.git
cd elige-tu-propia-aventura-ml


Configuración del Frontend
Ir a la carpeta frontend:

```bash
cd frontend
Instalar dependencias:

```bash
npm install
# o con Yarn
yarn install

Crear un archivo .env.local y configurar las variables:
env
```bash
NEXT_PUBLIC_API_URL=http://localhost:8000

Iniciar el servidor de desarrollo:
```bash
npm run dev
# o con Yarn
yarn dev


Configuración del Backend
Ir a la carpeta backend:
```bashcd backend
Crear un entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: venv\Scripts\activate

Instalar dependencias:
```bash
pip install -r requirements.txt

Configurar el archivo .env:
env
```bash


Iniciar el servidor de desarrollo:

```bash
uvicorn main:app --reload

Uso de Docker
Construir y levantar los contenedores:

```bash
docker-compose up --build
🧪 Ejecución de Tests
Frontend

```bash
npm run test
# o con Yarn
yarn test

Backend
```bash
pytest

📂 Estructura del Proyecto
plaintext

```bash
elige-tu-propia-aventura-ml/
├── frontend/         # Código del frontend (Next.js)
├── backend/          # Código del backend (Python)
├── docker-compose.yml
├── README.md
└── .gitignore

📖 Contribuir
Haz un fork del repositorio.
Crea una rama con tu feature: git checkout -b mi-feature.
Haz commit de tus cambios: git commit -m 'Añadir mi feature'.
Haz push a la rama: git push origin mi-feature.
Abre un Pull Request.

📝 Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

css
Copiar código

Este contenido es ideal para un archivo `README.md` que puedes usar directamente. Copia todo y pégalo en tu editor de texto favorito para guardarlo con ese nombre. 😊
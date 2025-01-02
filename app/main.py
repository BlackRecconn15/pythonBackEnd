from fastapi import FastAPI
from app.routers import users, products, purchases
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost:5173",  # Tu frontend en desarrollo
    "http://127.0.0.1:5173",  # Alternativa si usas 127.0.0.1
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluye las rutas
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(purchases.router, prefix="/purchases", tags=["Purchases"])

print("Rutas registradas:", app.openapi().get("paths"))  # Depuración

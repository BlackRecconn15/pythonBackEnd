from .user import create_user, get_users
from .product import create_product, get_products
from .purchase import create_purchase

# Opcional: agrupa todos los métodos CRUD en un solo módulo
__all__ = ["create_user", "get_users", "create_product", "get_products","create_purchase"]

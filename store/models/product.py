from store.models.base import CreateBaseModel
from store.schemas.product import ProductIn


class ProductModel(CreateBaseModel,ProductIn):
    pass


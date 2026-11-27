from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):
    CAPACITY = 50

    def __init__(self, name: str, location: str):
        super().__init__(name, location,self.CAPACITY)

    @property
    def store_type(self):
        return "FurnitureStore"

    @property
    def stats_title(self):
        return "**Furniture for sale:"
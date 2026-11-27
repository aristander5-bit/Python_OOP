from project.stores.base_store import BaseStore


class ToyStore(BaseStore):
    CAPACITY = 100

    def __init__(self, name: str , location: str):
        super().__init__(name, location, self.CAPACITY)

    @property
    def store_type(self):
        return "ToyStore"

    @property
    def stats_title(self):
        return "**Toys for sale:"
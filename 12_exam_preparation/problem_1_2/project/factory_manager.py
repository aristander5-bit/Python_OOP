from typing import List
from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    def __init__(self, name: str):
        self.name = name
        self.income: float = 0.0
        self.products: List[BaseProduct] = []
        self.stores: List[BaseStore] = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type == "Chair":
            product = Chair(model, price)
        elif product_type == "HobbyHorse":
            product = HobbyHorse(model, price)
        else:
            raise Exception("Invalid product type!")

        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type == "FurnitureStore":
            store = FurnitureStore(name, location)
        elif store_type == "ToyStore":
            store = ToyStore(name, location)
        else:
            raise Exception(f"{store_type} is an invalid type of store!")

        self.stores.append(store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        # 1. ПЪРВО проверяваме дали складът има достатъчно капацитет за ВСИЧКИ подадени продукти
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        # 2. СЛЕД ТОВА филтрираме съвпадащите по тип
        valid_products = []
        for product in products:
            if store.store_type == "FurnitureStore" and product.sub_type == "Furniture":
                valid_products.append(product)
            elif store.store_type == "ToyStore" and product.sub_type == "Toys":
                valid_products.append(product)

        if not valid_products:
            return "Products do not match in type. Nothing sold."

        for product in valid_products:
            self.products.remove(product)
            store.products.append(product)

        store.capacity -= len(valid_products)
        total_price = sum(p.price for p in valid_products)
        self.income += total_price

        return f"Store {store.name} successfully purchased {len(valid_products)} items."

    def unregister_store(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if not store:
            raise Exception("No such store!")

        if len(store.products) > 0:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store.name}, location: {store.location}."

    def discount_products(self, product_model: str):
        matching_products = [p for p in self.products if p.model == product_model]
        for product in matching_products:
            product.discount()

        return f"Discount applied to {len(matching_products)} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if not store:
            return "There is no store registered under this name!"
        return store.store_stats()

    def statistics(self):
        products_summary = {}
        for product in self.products:
            if product.model not in products_summary:
                products_summary[product.model] = 0
            products_summary[product.model] += 1

        products_sum_price = sum(p.price for p in self.products)

        stats = [
            f"Factory: {self.name}",
            f"Income: {self.income:.2f}",
            "***Products Statistics***",
            f"Unsold Products: {len(self.products)}. Total net price: {products_sum_price:.2f}",
        ]

        for model in sorted(products_summary.keys()):
            stats.append(f"{model}: {products_summary[model]}")

        stats.append(f"***Partner Stores: {len(self.stores)}***")
        for store in sorted(self.stores, key=lambda s: s.name):
            stats.append(store.name)

        return "\n".join(stats)
from project.category import Category
from project.document import Document
from project.topic import Topic



class Storage:
    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> None:
        self.__edit_object(category_id, self.categories, new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        self.__edit_object(topic_id, self.topics, new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        self.__edit_object(document_id, self.documents, new_file_name)

    def delete_category(self, category_id: int) -> None:
        self.__delete_object(category_id, self.categories)

    def delete_topic(self, topic_id: int) -> None:
        self.__delete_object(topic_id, self.topics)

    def delete_document(self, document_id: int) -> None:
        self.__delete_object(document_id, self.documents)

    def get_document(self, document_id: int) -> Document:
        return self.__find_object_by_id(document_id, self.documents)

    def __repr__(self) -> str:
        return "\n".join(str(d) for d in self.documents)

    def __edit_object(self, object_id, objects_collection, *new_values) -> None:
        curr_obj = self.__find_object_by_id(object_id, objects_collection)
        if curr_obj:
            curr_obj.edit(*new_values)

    def __delete_object(self, object_id, objects_collection) -> None:
        curr_obj = self.__find_object_by_id(object_id, objects_collection)
        if curr_obj:
            objects_collection.remove(curr_obj)


    @staticmethod
    def __find_object_by_id(object_id, objects_collection)-> Category | Topic | Document | None:
        return next((o for o in objects_collection if o.id == object_id), None)


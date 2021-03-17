class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        filtered_category = [category for category in self.categories if category.id == category_id][0]
        filtered_category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        filtered_topic = [topic for topic in self.topics if topic.id == topic_id][0]
        filtered_topic.topic = new_topic
        filtered_topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        filtered_document = [doc for doc in self.documents if doc.id == document_id][0]
        filtered_document.file_name = new_file_name

    def delete_category(self,category_id):
        filtered_category = [category for category in self.categories if category.id == category_id][0]
        self.categories.remove(filtered_category)

    def delete_topic(self, topic_id):
        filtered_topic = [topic for topic in self.topics if topic.id == topic_id][0]
        self.topics.remove(filtered_topic)

    def delete_document(self, document_id):
        filtered_document = [doc for doc in self.documents if doc.id == document_id][0]
        self.documents.remove(filtered_document)

    def get_document(self, document_id):
        filtered_document = [doc for doc in self.documents if doc.id == document_id][0]
        return filtered_document.__repr__()

    def __repr__(self):
        res = '\n'.join([doc.__repr__()for doc in self.documents])
        return res








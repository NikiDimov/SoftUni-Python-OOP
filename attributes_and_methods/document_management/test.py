from OOP.attributes_and_methods.document_management.category import Category
from OOP.attributes_and_methods.document_management.document import Document
from OOP.attributes_and_methods.document_management.storage import Storage
from OOP.attributes_and_methods.document_management.topic import Topic
c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize project")
d1.add_tag("urgent")
d1.add_tag("work")
storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)
print(c1)
print(t1)
print(storage.get_document(1))
print(storage)
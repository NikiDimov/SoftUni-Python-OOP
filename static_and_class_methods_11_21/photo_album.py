from math import ceil


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label):
        for page in self.photos:
            if len(page) < 4:
                page.append(label)
                return f"{label} photo added successfully on page {self.photos.index(page) + 1} " \
                       f"slot {page.index(label) + 1}"
        return "No more free slots"

    def display(self):
        result = "-----------\n"
        for page in self.photos:
            result += ("[] " * len(page)).strip() + "\n-----------\n"
        return result.strip()


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

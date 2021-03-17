class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = []
        for _ in range(pages):
            self.photos.append([])

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(photos_count // 4)

    def add_photo(self, label):
        if not len(self.photos[-1]) == 4:
            for page in self.photos:
                if len(page) != 4:
                    page.append(label)
                    break
            return f"{label} photo added successfully on" \
                   f" page {self.photos.index(page) + 1} slot {page.index(label) + 1}"
        return "No more free spots"

    def display(self):
        res = "-----------\n"
        for p in self.photos:
            res += (''.join(["[] " for s in p])).strip()
            res += "\n-----------\n"
        return res


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())

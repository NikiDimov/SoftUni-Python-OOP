from OOP.defining_classes.spoopify.song import Song


class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song: Song):
        if not song.single and not self.published and song not in self.songs:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f"Cannot add songs. Album is published."
        if song in self.songs:
            return f"Song is already in the album."

    def remove_song(self, song_name: str):
        if not self.published:
            for s in self.songs:
                if s.name == song_name:
                    self.songs.remove(s)
                    return f"Removed song {song_name} from album {self.name}."
            return "Song is not in the album."
        return "Cannot remove songs. Album is published."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self):
        res = f"Album {self.name}\n"
        for s in self.songs:
            res += "== " + s.get_info() + "\n"
        return res

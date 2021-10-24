class Music:
    def __init__(self, title, artist, lyrics):
        self.title, self.artist, self.lyrics = title, artist, lyrics

    def print_info(self):
        return f"This is \"{self.title}\" from \"{self.artist}\""

    def play(self):
        return self.lyrics


song = Music("title", "artist", "lyrics")
print(song.print_info())
print(song.play())

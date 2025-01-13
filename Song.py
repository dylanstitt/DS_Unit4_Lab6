import time

class Song:

    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"{self.title} by {self.artist}"

    def play(self):
        return time.sleep(round(self.duration / 100, 2))

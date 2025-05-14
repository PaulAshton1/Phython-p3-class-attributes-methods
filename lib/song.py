class Song:
    count = 0
    artists = []
    genre = []
    genre_count = {}
    artist_count = {}

    def __init__(self, artist, genre):
        self.artist = artist
        self.genre = genre


    @classmethod
    def add_song_to_count(cls):
        cls.count += 1


    @classmethod
    def add_genre(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1    


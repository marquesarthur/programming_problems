from collections import defaultdict


def get_most_listened(song_lst, song_genres_map):

    result = defaultdict(int)

    _max_value = 0
    for song in song_lst:
        if song in song_genres_map:
            genre = song_genres_map[song]
            if genre not in result:
                result[genre] = 0

            result[genre] += 1

            _max_value = max(_max_value, result[genre])

    most_listened = [key for key,
                     value in result.items() if value == _max_value]

    return most_listened


def favourite_genres(user_songs, song_genres):
    song_genres_map = {}

    for genre, song_lst in song_genres.items():
        for song_id in song_lst:
            song_genres_map[song_id] = genre

    result = {}
    for user, songs in user_songs.items():
        result[user] = get_most_listened(songs, song_genres_map)

    return result


userSongs = {
    "David": ["song1", "song2", "song3", "song4", "song8"],
    "Emma":  ["song5", "song6", "song7"]
}

songGenres = {
    "Rock":    ["song1", "song3"],
    "Dubstep": ["song7"],
    "Techno":  ["song2", "song4"],
    "Pop":     ["song5", "song6"],
    "Jazz":    ["song8", "song9"]
}


print(favourite_genres(userSongs, songGenres))

userSongs = {
   "David": ["song1", "song2"],
   "Emma":  ["song3", "song4"]
}
songGenres = {}
print('')
print(favourite_genres(userSongs, songGenres))
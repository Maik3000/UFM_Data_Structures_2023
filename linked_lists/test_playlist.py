from playlist import Playlist, Song, Node

# Creamos instancia de la clase 
my_playlist = Playlist()

song1 = Song(1, "Sin frenos", "Eladio Carrion", "Destilar")
my_playlist.insert_at_end(Node(song1))

song2 = Song(2, "La trampa es ley", "Lit Killah", "Destilar")
my_playlist.insert_at_end(Node(song2))

song3 = Song(3, "Slow", "Tiago PZK", "Destilar")
my_playlist.insert_at_end(Node(song3))


print("La cantidad de canciones en la playlist es:", my_playlist.playlist_len())

print("\n Primera canción ")
my_playlist.play()

print("\n Siguiente canción")
my_playlist.next()

print("\n Anterior canción")
my_playlist.previous()

print("\n Canción Aleatoria")
my_playlist.play_shuffle()

print("\n Cancion por nombre")
my_playlist.search_by_name("Slow")





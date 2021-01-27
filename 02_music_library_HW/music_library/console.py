import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()

album_1 = Album("Sgt Peppers Lonely Hearts Club Band", "Beatles", "Pop/Rock")
album_2 = Album("Best of the Pogues", "Pogues", "Folk")

print(album_1.__dict__)

album_repository.save(album_1)


res = album_repository.select_all()

for album in res:
    print(album.__dict__)

pdb.set_trace() 

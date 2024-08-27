from bintrees import RBTree # type: ignore

class MusicIndex:
    def __init__(self):
        self.primary_index = RBTree()  # Índice primário usando uma Árvore B
        self.secondary_index_title = {}  # Índice secundário para títulos
        self.secondary_index_artist = {}  # Índice secundário para artistas
    
    def add_music(self, music_id, title, artist, album, file_path):
        # Adiciona à árvore B (índice primário)
        self.primary_index.insert(music_id, (title, artist, album, file_path))
        
        # Adiciona aos índices secundários
        if title in self.secondary_index_title:
            self.secondary_index_title[title].append(music_id)
        else:
            self.secondary_index_title[title] = [music_id]
        
        if artist in self.secondary_index_artist:
            self.secondary_index_artist[artist].append(music_id)
        else:
            self.secondary_index_artist[artist] = [music_id]
    
    def remove_music(self, music_id):
        # Remove da árvore B (índice primário)
        if music_id in self.primary_index:
            title, artist, album, file_path = self.primary_index.pop(music_id)
            
            # Remove dos índices secundários
            self.secondary_index_title[title].remove(music_id)
            if len(self.secondary_index_title[title]) == 0:
                del self.secondary_index_title[title]
            
            self.secondary_index_artist[artist].remove(music_id)
            if len(self.secondary_index_artist[artist]) == 0:
                del self.secondary_index_artist[artist]
    
    # Módulo de Lógica de Busca
    
    def search_by_id(self, music_id):
        """
        Busca uma música pelo ID (índice primário).
        """
        return self.primary_index.get(music_id, None)
    
    def search_by_title(self, title):
        """
        Busca músicas pelo título (índice secundário).
        Retorna uma lista de músicas que correspondem ao título.
        """
        music_ids = self.secondary_index_title.get(title, [])
        return [self.primary_index[music_id] for music_id in music_ids]
    
    def search_by_artist(self, artist):
        """
        Busca músicas pelo artista (índice secundário).
        Retorna uma lista de músicas que correspondem ao artista.
        """
        music_ids = self.secondary_index_artist.get(artist, [])
        return [self.primary_index[music_id] for music_id in music_ids]
    
    def search_by_title_and_artist(self, title, artist):
        """
        Busca músicas pelo título e artista.
        Retorna uma lista de músicas que correspondem ao título e artista.
        """
        title_ids = set(self.secondary_index_title.get(title, []))
        artist_ids = set(self.secondary_index_artist.get(artist, []))
        
        # Intersecção de IDs para encontrar músicas que correspondem a ambos título e artista
        matching_ids = title_ids.intersection(artist_ids)
        return [self.primary_index[music_id] for music_id in matching_ids]

# Exemplo de uso do módulo de busca
music_index = MusicIndex()

# Adicionando músicas
music_index.add_music(1, "Song Title 1", "Artist A", "Album X", "path/to/song1.mp3")
music_index.add_music(2, "Song Title 2", "Artist B", "Album Y", "path/to/song2.mp3")
music_index.add_music(3, "Song Title 1", "Artist C", "Album Z", "path/to/song3.mp3")

# Buscando por ID
print(music_index.search_by_id(1))

# Buscando por título
print(music_index.search_by_title("Song Title 1"))

# Buscando por artista
print(music_index.search_by_artist("Artist A"))

# Buscando por título e artista
print(music_index.search_by_title_and_artist("Song Title 1", "Artist A"))

# Removendo uma música
music_index.remove_music(2)



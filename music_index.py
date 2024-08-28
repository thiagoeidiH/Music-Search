from bintrees import RBTree  # type: ignore

class IndiceMusical:
    def __init__(self):
        self.indice_primario = RBTree()
        self.indice_secundario_titulo = {}
        self.indice_secundario_artista = {}
        self.indice_secundario_album = {}  
    
    def adicionar_musica(self, id_musica, titulo, artista, album):
        self.indice_primario.insert(id_musica, (titulo, artista, album))
        
        if titulo in self.indice_secundario_titulo:
            self.indice_secundario_titulo[titulo].append(id_musica)
        else:
            self.indice_secundario_titulo[titulo] = [id_musica]
        
        if artista in self.indice_secundario_artista:
            self.indice_secundario_artista[artista].append(id_musica)
        else:
            self.indice_secundario_artista[artista] = [id_musica]
        
        if album in self.indice_secundario_album:
            self.indice_secundario_album[album].append(id_musica)
        else:
            self.indice_secundario_album[album] = [id_musica]
    
    def remover_musica(self, id_musica):
        if id_musica in self.indice_primario:
            titulo, artista, album = self.indice_primario.pop(id_musica)
            
            self.indice_secundario_titulo[titulo].remove(id_musica)
            if len(self.indice_secundario_titulo[titulo]) == 0:
                del self.indice_secundario_titulo[titulo]
            
            self.indice_secundario_artista[artista].remove(id_musica)
            if len(self.indice_secundario_artista[artista]) == 0:
                del self.indice_secundario_artista[artista]

            self.indice_secundario_album[album].remove(id_musica)
            if len(self.indice_secundario_album[album]) == 0:
                del self.indice_secundario_album[album]
    
    def buscar_por_id(self, id_musica):
        return self.indice_primario.get(id_musica, None)
    
    def buscar_por_titulo(self, titulo):
        ids_musica = self.indice_secundario_titulo.get(titulo, [])
        return [self.indice_primario[id_musica] for id_musica in ids_musica]
    
    def buscar_por_artista(self, artista):
        ids_musica = self.indice_secundario_artista.get(artista, [])
        return [self.indice_primario[id_musica] for id_musica in ids_musica]
    
    def buscar_por_album(self, album):  # Nova função de busca por álbum
        ids_musica = self.indice_secundario_album.get(album, [])
        return [self.indice_primario[id_musica] for id_musica in ids_musica]

    def buscar_por_titulo_e_artista(self, titulo, artista):
        ids_titulo = set(self.indice_secundario_titulo.get(titulo, []))
        ids_artista = set(self.indice_secundario_artista.get(artista, []))
        ids_correspondentes = ids_titulo.intersection(ids_artista)
        return [self.indice_primario[id_musica] for id_musica in ids_correspondentes]

indice_musical = IndiceMusical()

indice_musical.adicionar_musica(1, "Scientist", "Coldplay", "A rush of blood to the head")
indice_musical.adicionar_musica(2, "Shallow", "Lady Gaga", "A Star Is Born")
indice_musical.adicionar_musica(3, "Poker Face", "Lady Gaga", "A Star Is Born")
indice_musical.adicionar_musica(4, "Trem Bala", "Ana Vilela", "Ana Vilela")

print(indice_musical.buscar_por_id(1))

print(indice_musical.buscar_por_titulo("Shallow"))

print(indice_musical.buscar_por_artista("Lady Gaga"))

print(indice_musical.buscar_por_album("Ana Vilela"))

print(indice_musical.buscar_por_titulo_e_artista("Poker Face", "Lady Gaga"))

indice_musical.remover_musica(2)

print(indice_musical.buscar_por_id(2))

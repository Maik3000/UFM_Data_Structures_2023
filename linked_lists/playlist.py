class Node:
    def __init__(self, song=None, next_node=None):
        self.song = song
        self.next_node = next_node


class Song:
    def __init__(self, id, name, artist, album):
        self.id = id
        self.name = name
        self.artist = artist
        self.album = album


class Playlist:
    

    def traverse(self):
            '''
            Navigates every node in the list.

            Args:
                None

            Returns:
                None
            '''
            
            current_node = self.start

            while current_node is not None:
                print(current_node)
                current_node = current_node.next


    def traverse_iter(self):
        '''
        Iterates trough the list using the __iter__ method.

        Args:
            None

        Returns:
            None
        '''

        for current_node in self:
            print(current_node)


    def insert_at_beginning(self, new_node: Node):
        '''
        Inserts a node at the start of the linked list.

        Args:
            new_node (Node): node to be inserted

        Returns:
            None
        '''

        new_node.next = self.start
        self.start = new_node


    def insert_at_end(self, new_node: Node):
        '''
        Inserts a node at the end of the linked list.

        Args:
            new_node (Node): node to be inserted

        Returns:
            None
        '''

        if self.start is None:
            self.start = new_node

        else:
            for current_node in self:
                pass

            current_node.next = new_node


    def insert_before(self, reference_node: str, new_node: Node):
        '''
        Inserts a node before the position of the reference node given.

        Args:
            reference_node (str): value of node used as reference
            new_node (Node): node to be inserted

        Returns:
            None
        '''

        if self.start is None:
            print('Empty linked list...')
            return

        if self.start.data == reference_node:
            return self.insert_at_beginning(new_node)

        previous_node = self.start

        for current_node in self:

            if current_node.data == reference_node:
                previous_node.next = new_node
                new_node.next = current_node
                return
            
            previous_node = current_node

        print('Reference node {} not found in linked list...'.format(reference_node))


    def delete(self, reference_node: str):
        '''
        Deletes a node given a value reference.

        Args:
            reference_node (str): value of node used as reference
            
        Returns:
            None
        '''

        if self.start is None:
            print('Empty linked list...')
            return   

        if self.start.data == reference_node:
            self.start = self.start.next
            return
        
        previous_node = self.start

        for current_node in self:

            if current_node.data == reference_node:
                previous_node.next = current_node.next
                return

            previous_node = current_node

        print('Reference node {} not found in linked list...'.format(reference_node))
    

#improvement code, implementation of playlist

    def __init__(self):
        self.start_node = None
        self.current_node = None
        self.previous_node = None
        self.next_node = None
        self.length = 0

    def playlist_len(self):
        return self.length

    def insert_at_end(self, node):
        if self.start_node is None:
            self.start_node = node
            self.current_node = node
            self.length += 1
        else:
            current = self.start_node
            while current.next_node is not None:
                current = current.next_node
            current.next_node = node
            self.length += 1

    def play(self):
        if self.current_node is None:
            print("La lista de reproducción está vacía.")
        else:
            print("Reproduciendo: ", self.current_node.song.name)

    def next(self):
        if self.current_node is None:
            print("La lista de reproducción está vacía.")
        else:
            self.previous_node = self.current_node
            self.current_node = self.current_node.next_node
            if self.current_node is None:
                print("Fin de la lista de reproducción.")
            else:
                print("Reproduciendo: ", self.current_node.song.name)

    def previous(self):
        if self.current_node is None:
            print("La lista de reproducción está vacía.")
        else:
            self.current_node = self.previous_node
            if self.current_node is None:
                print("Inicio de la lista de reproducción.")
            else:
                print("Reproduciendo: ", self.current_node.song.name)

    def play_shuffle(self):
        import random
        if self.start_node is None:
            print("La lista de reproducción está vacía.")
        else:
            random_node = self.start_node
            for i in range(random.randint(0, self.length - 1)):
                random_node = random_node.next_node
            self.current_node = random_node
            print("Reproduciendo al azar: ", self.current_node.song.name)

    def search_by_name(self, name):
        current = self.start_node
        while current is not None:
            if current.song.name == name:
                self.current_node = current
                print("Reproduciendo: ", self.current_node.song.name)
                return
            current = current.next_node
        print("No se encontró la canción.")

    def search_by_artist(self, artist):
        
        current_node = self.head
        matching_songs = []

        while current_node is not None:
            if current_node.data.artist == artist:
                matching_songs.append(current_node.data.title)
            current_node = current_node.next_node

        if len(matching_songs) == 0:
            print("No se encontraron canciones del artista {artist} en la playlist.")
        else:
            print("Canciones del artista {artist}:")
            for song in matching_songs:
                print("- {song}")

        return matching_songs
        
    def delete(self, reference_node: str):
            if self.start is None:
                print('Linked List vacía...')
                return
            if self.start.data.name == reference_node:
                self.start = self.start.next
                return
            previous_node = self.start
            for current_node in self:
                if current_node.data.name == reference_node:
                    previous_node.next = current_node.next
                    return
                previous_node = current_node
            print('Node de referencia {} no encontrado...'.format(reference_node))

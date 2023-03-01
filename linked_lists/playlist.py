import random

class Song:
    '''
    Song object.

    Args:
        id (int): unique identifier for song
        name (str): name of song
        artist (str): artist who performed the song
        album (str): album that contains the song

    Attributes:
        id (int): unique identifier for song
        name (str): name of song
        artist (str): artist who performed the song
        album (str): album that contains the song
    '''

    def __init__(self, id: int, name: str, artist: str, album: str):
        self.id = id
        self.name = name
        self.artist = artist
        self.album = album

    def __repr__(self):
        return '| ID: {} | Name: {} | Artist: {} | Album: {} |'.format(self.id, self.name, self.artist, self.album)


class Node:
    '''
    Node object.

    Args:
        data (Song): song object to store in node

    Attributes:
        data (Song): value stored in node
        next (Node): pointer to next node in list
        prev (Node): pointer to previous node in list
    '''

    def __init__(self, data: Song):
        self.data = data
        self.next = None
        self.prev = None


    def __repr__(self):
        return str(self.data)


class Playlist:
    '''
    Playlist object.

    Args:
        None

    Attributes:
        start (Node): pointer to first node in playlist
        current (Node): pointer to current node in playlist
        length (int): length of playlist
    '''

    def __init__(self):
        self.start = None
        self.current = None
        self.length = 0


    def __iter__(self):
        node = self.start

        while node is not None:
            yield node
            node = node.next


    def __repr__(self):
        nodes = ["START"]

        for node in self:
            nodes.append(str(node.data))

        nodes.append("NIL")
        return " <--> ".join(nodes)


    def traverse(self):
        '''
        Navigates every node in the playlist.

        Args:
            None

        Returns:
            None
        '''
        
        current_node = self.start

        while current_node is not None:
            print(current_node)
            current_node = current_node.next
    


    def play(self):
        '''
        Plays the first song in the playlist.

        Args:
            None

        Returns:
            None
        '''

        if self.start is None:
            print('Empty playlist...')
            return

        self.current = self.start
        print('Playing:', self.current)


    def show_details(self):
        '''
        Shows the data information for the song currently playing.

        Args:
            None

        Returns:
            None
        '''

        if self.current is None:
            print('No song is currently playing...')
            return

        print('Currently playing:', self.current.data)


    def next(self):
        '''
        Plays the next song in the playlist.

        Args:
            None

        Returns:
            None
        '''

        if self.current is None:
            print('No song is currently playing...')
            return

        if self.current.next is None:
            print('End of playlist...')
            return

        self.current = self.current.next
        print('Playing:', self.current)


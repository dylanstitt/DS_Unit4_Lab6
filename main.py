# Dylan Stitt
# Unit 4 Lab 6
# Music Playlist

from QueueClass import Queue
from Song import Song
import os

def getContent(filename):
    with open(filename, 'r') as file:
        content = file.read().splitlines()
        newContent = []
        for i in range(len(content)):
            newContent.append(content[i].split(' - '))
            newContent[i][2] = newContent[i][2].replace(':', '')

    return newContent

def createSong(content, queue):
    for i in content:
        queue.enqueue(Song(i[0], i[1], int(i[2])))

def main():
    queue = Queue()
    songContent = getContent('playlist.txt')
    createSong(songContent, queue)

    for i in range(len(queue)):
        song = queue.dequeue()
        print(f'Now Playing: {song}')

        if len(queue) != 0:
            print(f'Up Next: {queue.first()}')
        else:
            print(f'Up Next: End of Playlist')

        song.play()
        os.system('cls')

if __name__ == '__main__':
    main()

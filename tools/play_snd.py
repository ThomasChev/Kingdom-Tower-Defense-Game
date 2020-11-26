import pygame # pygame-1.9.6-cp38-cp38-win_amd64.whl
import os
from collections import deque

snd_dir = "game_assets/sounds/"
_songs = deque([os.path.join(snd_dir, "13_Tazer.mp3"), os.path.join(snd_dir, "08_T_Station.mp3"), os.path.join(snd_dir, "04_Shamburger.mp3")])

def play_sound(*args):
    """
    call pygame.mixer fonction with sounds located in snd_dir
    """ 

    if len(args) == 3:
        a,b,c = args[0],args[1],args[2]
        pygame.mixer.Channel(a).play(pygame.mixer.Sound(os.path.join(snd_dir, b)), maxtime=c)
    elif len(args) == 2:
        a,b = args[0],args[1]
        pygame.mixer.Channel(a).play(pygame.mixer.Sound(os.path.join(snd_dir, b)))

def play_next_song():
    """
    change sound when previous sound is finished
    """ 
    global _songs
    _songs.rotate(-1) # move current song to the back of the list (equal to: _songs = _songs[1:] + [_songs[0]])
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
import logging
import os
from typing import Dict

import music21 as m21
from tqdm import tqdm

logger = logging.getLogger(__name__)


def load_songs_in_kern(path_params: Dict[str, str]):
    """Going through all files and load the files which have the correct format.

    Args:
        path_params (str): The path under which the audio files are stored
    """

    songs = []

    dataset_path = path_params["path"]
    for path, _, files in tqdm(os.walk(dataset_path)):
        for file in files:
            if file.endswith("krn"):
                full_song_name = os.path.join(path, file)
                song = m21.converter.parse(full_song_name)
                songs.append(song)

    return songs


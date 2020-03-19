""" This function deletes the local copies of the downloaded, converted, and trimmed audio files,
which are unnecessary after the analysis has been performed. """
import os

def audio_delete(file_name):
    """Deletes the local copies of the audio files. """
    os.remove(file_name)
    os.remove(file_name[:-4]+".wav")
    os.remove(file_name[:-4]+"_trim.wav")

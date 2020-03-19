""" Download mp3 from AWS and convert the mp3 to wav file for further analysis. """

from urllib.request import urlretrieve
from pydub import AudioSegment

def url_read(file_name):
    """ Download the mp3 file. """

    file_url = "https://s3-ap-southeast-1.amazonaws.com/bucket/"+file_name

    urlretrieve(file_url, file_name)

def mp3_convert(file_name):
    """Convert mp3 to wav file.

    pydub requires installation of ffmpeg. I used "fink install ffmpeg" """

    file_export = AudioSegment.from_mp3(file_name)
    file_export.export(file_name[:-4]+".wav", format="wav")

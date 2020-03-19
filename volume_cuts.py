""" These functions detect and then remove empty or low-volume audio at the beginnings and
 ends of a wav file.  """
from pydub import AudioSegment

def detect_leading_silence(sound, silence_threshold, chunk_size=10):
    """ Iterate over audio chunks until you find the first one with sound

    sound is a pydub.AudioSegment
    silence_threshold in dBFS
    chunk_size in ms
    """
    trim_ms = 0 # ms

    assert chunk_size > 0 # to avoid infinite loop
    while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold and trim_ms < len(sound):
        trim_ms += chunk_size

    return trim_ms

def silence_cut(file_name, silence_threshold):
    """ Start and end times of the audio that passes the volume cut are returned
     and the trimmed wav file is created."""
    file_name_base = file_name[:-4]
    sound = AudioSegment.from_file(file_name_base+".wav", format="wav")
    # The audio start times are moved to 50 ms earlier and the end times to 50 ms later.
    # This provides some moderate space to prevent abrupt audio jumps and cuts.
    start_trim = detect_leading_silence(sound, silence_threshold)-50
    if start_trim < 0:
        start_trim = 0
    end_trim = detect_leading_silence(sound.reverse(), silence_threshold)-50

    start_time = start_trim/1000
    duration = len(sound)
    end_time = (duration-end_trim)/1000
    trimmed_sound = sound[start_trim:duration-end_trim]
    trimmed_sound.export(file_name_base+"_trim.wav", format="wav")

    return start_time, end_time

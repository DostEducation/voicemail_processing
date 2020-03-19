# Voicemail Processing:
A machine learning pipeline to identify and transcribe user voicemails

`voicemail_classifier.py` is a program that automatically classifies a voicemail and outputs valid/invalid, the valid probability, the time at which the voice begins and ends speaking, and the gender of the speaker.  The gender is assumed to be either an adult male or adult female.

(Note: This program will not correctly identify that there are multiple speakers or a child speaker.  However, when there are multiple speakers within a single voicemail, the gender of the primary speaker is typically identified correctly.)

## The pipeline:
The algorithm follows these steps by calling these other scripts:
1) `url_read_convert.py`: Downloads an mp3 voicemail defined as FILE_NAME that is stored at [https://s3-ap-southeast-1.amazonaws.com/bucket/](https://s3-ap-southeast-1.amazonaws.com/bucket) and converts it into a local .wav file.
2) `volume_cuts.py`: Performs an audio cut at the beginnings and ends of the wav file by removing low-volume content without information and
outputs a "trim.wav" file with these ends removed.
3) `librosa_feature_extraction.py`: Extracts the audio features to be used by the validity/gender models.
4) `model_apply.py`: Unpickles and applies the models to the voicemail features and returns a dictionary with the voicemail characteristics.
5) `delete_intermediary.py`: Removes the local copies of the mp3, wav, and trim.wav files.

## Installation notes:
When first running this, the required python3 packages that are missing will likely be told to you while you attempt to run `voicemail_classifier.py`.  However, the `pydub` conversion from mp3 to wav file will likely also need an installation of `ffmpeg`, which I was able to locally install on my mac with `fink install ffmpeg`.

### Credits:
Thanks Dr. Jeff Cumings for volunteering your time to work with [Dost Education](www.dosteducation.com) on this project.

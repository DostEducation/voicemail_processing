""" These functions extract the MFCC audio features of each trimmed wav file, and returns the
 medians and interquartile ranges of each of the 50 coefficients, plus the trimmed audio length. """
import librosa
import librosa.display
import scipy.stats
import numpy as np
import pandas as pd

def mfccs_features(file_name):
    """ Extract a 50 MFCC feature time-series for the audio and return the median, interquartile
     range, and duration.  Return a series of 0's for all features when the trimmed audio is 0. """
    file_name_base = file_name[:-4]
# try and except are used to handle when the trim.wav files have been cut to 0.
    try:
# Use "_trim.wav" instead of ".wav" for when you want to use the trimmed audio files.
        audio_series, sample_rate = librosa.load(file_name_base+"_trim.wav")
        duration = librosa.get_duration(y=audio_series, sr=sample_rate)
        mfccs = librosa.feature.mfcc(y=audio_series, sr=sample_rate, n_mfcc=50)
        c_iqr = list(scipy.stats.iqr(mfccs, axis=1))
        c_med = list(np.median(mfccs, axis=1))
    except:
        c_iqr = [0] * 50
        c_med = [0] * 50
        duration = 0
    return [file_name_base+"_trim.wav"]+c_iqr+c_med+[str(duration)]

def features_writer(file_name):
    """ Return the feature list converted into a dataframe with labeled columns. """
    feature_list = mfccs_features(file_name)
    return pd.DataFrame([feature_list], columns=['Filename', 'IQR1', 'IQR2', 'IQR3', 'IQR4',\
     'IQR5', 'IQR6', 'IQR7', 'IQR8', 'IQR9', 'IQR10', 'IQR11', 'IQR12', 'IQR13', 'IQR14',\
     'IQR15', 'IQR16', 'IQR17', 'IQR18', 'IQR19', 'IQR20', 'IQR21', 'IQR22', 'IQR23', 'IQR24',\
     'IQR25', 'IQR26', 'IQR27', 'IQR28', 'IQR29', 'IQR30', 'IQR31', 'IQR32', 'IQR33', 'IQR34',\
     'IQR35', 'IQR36', 'IQR37', 'IQR38', 'IQR39', 'IQR40', 'IQR41', 'IQR42', 'IQR43', 'IQR44',\
     'IQR45', 'IQR46', 'IQR47', 'IQR48', 'IQR49', 'IQR50', 'MED1', 'MED2', 'MED3', 'MED4',\
     'MED5', 'MED6', 'MED7', 'MED8', 'MED9', 'MED10', 'MED11', 'MED12', 'MED13', 'MED14',\
     'MED15', 'MED16', 'MED17', 'MED18', 'MED19', 'MED20', 'MED21', 'MED22', 'MED23', 'MED24',\
     'MED25', 'MED26', 'MED27', 'MED28', 'MED29', 'MED30', 'MED31', 'MED32', 'MED33', 'MED34',\
     'MED35', 'MED36', 'MED37', 'MED38', 'MED39', 'MED40', 'MED41', 'MED42', 'MED43', 'MED44',\
     'MED45', 'MED46', 'MED47', 'MED48', 'MED49', 'MED50', 'Duration'])

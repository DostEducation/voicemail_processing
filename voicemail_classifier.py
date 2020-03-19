""" The raw input voicemail mp3 is read in and a dictionary with all of the output voicemail
 characteristics is generated."""
from url_read_convert import url_read, mp3_convert
from volume_cuts import silence_cut
from librosa_feature_extraction import features_writer
from model_apply import model_apply
from delete_intermediary import audio_delete

#The file name of the original mp3 file, and the threshold value in dBFS for audio to be
#defined as above the background noise.  -24 dBFS is the value that works best for me.
FILE_NAME = "1571928000.6456833_0.mp3"
SILENCE_THRESHOLD = -24
VALIDATOR_MODEL = "final_validator_model.sav"
GENDER_MODEL = "final_gender_model.sav"

def main():
    """ The mp3 is read in, converted, background noise cut, features extracted, and the models
     are applied to output the Valid/Invalid, Valid Probability, and Gender characteristics. """
    url_read(FILE_NAME)
    mp3_convert(FILE_NAME)
    start_time, end_time = silence_cut(FILE_NAME, SILENCE_THRESHOLD)
    features_data = features_writer(FILE_NAME)
    output_dict = model_apply(features_data, start_time, end_time, VALIDATOR_MODEL,\
     GENDER_MODEL)
    audio_delete(FILE_NAME)

    print(output_dict)
    return output_dict

if __name__ == "__main__":
    main()

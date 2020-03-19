""" This set of functions unpickle the trained validation and gender models and applies
 the audio features to these to produce a dictionary that describes the output predictions. """
import pickle

def model_load(model_filename):
    """ Unpickle the model files. """
    return pickle.load(open(model_filename, 'rb'))

def model_apply(features_data, start_time, end_time, valid_name, gender_name):
    """ Define the models, seperate the features dataframe, apply the models and output a
     dictionary including mp3 file name, and the predictions of Validity, valid probability,
     and gender. """
    validator_model = model_load(valid_name)
    gender_model = model_load(gender_name)

    file_name = features_data["Filename"][0]
    audio_features = features_data.drop(columns=["Filename"])

    valid_out = validator_model.predict(audio_features)[0]
    valid_prob = round(validator_model.predict_proba(audio_features)[0, 1], 2)

    if valid_out == "Yes":
        gender_out = gender_model.predict(audio_features)[0]
    else:
        gender_out = None

    return {"Filename" : file_name[:-9]+".mp3", "Audio_Begins" : str(start_time)+" s",\
     "Audio_Ends" : str(end_time)+" s", "Valid?" : valid_out, "Valid_Score" : valid_prob,\
     "Gender?" : gender_out}

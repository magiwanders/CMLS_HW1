import numpy as np
import librosa
import os
import matplotlib.pyplot as plt
import sklearn.svm
import IPython.display as ipd
import scipy as sp
from pathlib import Path
import pandas as pd
import re
import json
from multiprocessing import Pool
import numpy as np
import time
from tqdm import tqdm
from p_tqdm import p_map
import multiprocessing


metadata = pd.read_csv('UrbanSound8K.csv')
metadata.head()


def compute_mfcc(audio, fs, win_length, hop_size, n_mfcc):
    # Compute the spectrogram of the audio signal
    X = np.abs(librosa.stft(
        audio,
        window='hamming',
        n_fft=win_length,
        hop_length=hop_size,)
        )

    # Find the weights of the mel filters
    mel = librosa.filters.mel(
        sr=fs,
        n_fft=win_length,
        n_mels=40,
        fmin=0,
        fmax=fs,
    )

    # Apply the filters to spectrogram
    melspectrogram = np.dot(mel, X)
    # Take the logarithm
    log_melspectrogram = np.log10(melspectrogram + 1e-16)

    # Apply the DCT to log melspectrogram to obtain the coefficients
    mfcc = sp.fftpack.dct(log_melspectrogram, axis=0, norm='ortho')[1:n_mfcc+1]
    return mfcc


def extract_features(x, fs, win_length, hop_size, n_mfcc):
    mfcc = compute_mfcc(x, fs, win_length, hop_size, n_mfcc);

    # take the statistics over time of the mfccs
    min = np.min(mfcc, axis=1);
    max = np.max(mfcc, axis=1);
    mean = np.mean(mfcc, axis=1);
    median = np.median(mfcc, axis=1);
    variance = np.var(mfcc, axis=1);

    # in total I should have 25*5 = 125 features per audio frame
    features = np.empty((0,125))
    ext_features = np.hstack([min, max, mean, median, variance])
    features = np.vstack([features,ext_features])

    return features


# Assume that the dataset is in the current directory
dataset_path = Path(".")

Fs = 22050;

win_length = int(np.ceil(0.0232*Fs))   # should return a 512 samples window
hop_size = int(0.5*win_length)

n_mfcc = 25;

mfcc_data = []

# Se qualcuno conosce il modo intelligente di fare quanto sotto sostituisca pure
print(dataset_path.iterdir())
list_of_folds = []
for current_fold_dir in dataset_path.iterdir():
  if current_fold_dir.is_dir() and "fold" in str(current_fold_dir):
    list_of_folds.append(current_fold_dir)

print(list_of_folds)

def scan_folder(current_fold_dir):
  #   # Check if the directory is really a directory
    if current_fold_dir.is_dir():
      # Save the current fold number
      current_fold_number = re.findall('[0-9-]+', str(current_fold_dir)) # Extract the fold number with regex
      #print("Scanning fold {} of 10" .format(current_fold_number))#, end='\x1b[1K\r') # Status printing with line clearing

      mfcc_data_folder = []
      # For each audio file in current_fold_dir
      l=0
      for current_audio_dir in (current_fold_dir).iterdir():
        l+=1
        # Check if it's really a file and not a fold
        if not current_audio_dir.is_dir() and os.path.splitext(current_audio_dir)[1] == '.wav':
          filename = current_audio_dir.stem + '.wav'
          #print("Currently processing: {}" .format(filename))
          #print("Scanning fold {} of 10" .format(current_fold_number))#, end='\x1b[1K\r') # Status printing with line clearing

          x, sr = librosa.load(current_audio_dir, sr=Fs)

          features = extract_features(x, Fs, win_length, hop_size, n_mfcc)

          metadata_row = metadata.loc[metadata['slice_file_name']==filename].values.tolist()
          label = metadata_row[0][-1];
          label_id = metadata_row[0][-2];
          fold = metadata_row[0][-3]

          mfcc_data_folder.append([features, features.shape, label_id, label, fold])

    # print("Che cos'è sta roba:")
    # print(np.asarray(mfcc_data_folder).shape)
    mfcc_data_folder = np.asarray(mfcc_data_folder)
    return [mfcc_data_folder.shape[0], mfcc_data_folder]

if __name__ == '__main__':
    mfcc_data_folder_array = np.asarray(p_map(scan_folder, list_of_folds))

dim = np.sum(np.asarray(mfcc_data_folder_array[:,0]))
mfcc_data_folder_array = np.asarray(mfcc_data_folder_array[:,1])
#print(mfcc_data_folder_array[0].shape)

i=0
j=0
for folder in mfcc_data_folder_array:
    j=0
    for sound in folder:
        mfcc_data.append(mfcc_data_folder_array[i][j])
        j+=1
    i+=1

mfcc_data = np.asarray(mfcc_data)
print(mfcc_data.shape)

cols=["features", "shape","label_id", "label", "fold"]
mfcc_pd = pd.DataFrame(data = mfcc_data, columns=cols)

mfcc_pd.head()

mfcc_json = mfcc_pd.to_json(r'prova_feature.json', orient='index')
# parsed = json.loads(mfcc_json)
# json.dumps(parsed, indent=4)

mfcc_pd_loaded = pd.read_json(r'prova_feature.json', orient='index')

mfcc_pd_loaded.head()

labels = set(mfcc_pd['label'])
print(labels)
cnt = [[label,list(mfcc_pd['label']).count(label)] for label in labels]
dict_cnt = dict(cnt)
dict_cnt

ll = [mfcc_pd['features'][i].ravel() for i in range(mfcc_pd.shape[0])]
mfcc_pd['sample'] = pd.Series(ll, index=mfcc_pd.index)
del mfcc_pd['features']

mfcc_pd.head()

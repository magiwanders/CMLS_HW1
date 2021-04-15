# CMLS_HW1
Folder structure:
* [src folder](src/): Colab notebooks for dataset analysis, feature extraction, training and testing   
* [guidelines folder](guidelines/): all the guidelines and requirements for the homework

## Overleaf link to the report
https://www.overleaf.com/5477346787fvnmpnppjygz


## Misc stuff
[Authors' Paper](http://www.justinsalamon.com/uploads/4/3/9/4/4394963/salamon_urbansound_acmmm14.pdf)
[k nearest neighbours](https://scikit-learn.org/stable/modules/neighbors.html#classification)  
[GMM](https://scikit-learn.org/stable/modules/mixture.html)  
[SVM](https://scikit-learn.org/stable/modules/svm.html#svm-classification)  

| Type                       | Feature                    | Librosa                       | Essentia                            |
|----------------------------|----------------------------|-------------------------------|-------------------------------------|
|                            |                            | librosa.feature               | f                                   |
| Basic Descriptors          | Audio Waveform             | np.max/np.min ?               | //                                  |
|                            | Audio Power                | ~ [rms(y, S)](https://librosa.org/doc/main/generated/librosa.feature.rms.html#librosa.feature.rms)                   | [InstantPower(array)](https://essentia.upf.edu/reference/std_InstantPower.html)                 |
| Basic Spectral Descriptors | Audio Spectral Envelope    | /                             | ~ [Envelope(signal)](https://essentia.upf.edu/reference/std_Envelope.html)                  |
|                            | Audio Spectrum Centroid    | [spectral_centroid(y, sr, ...)](https://librosa.org/doc/main/generated/librosa.feature.spectral_centroid.html#librosa.feature.spectral_centroid) | [SpectralCentroidTime(array)](https://essentia.upf.edu/reference/std_SpectralCentroidTime.html)         |
|                            | Audio Spectrum Spread      | /                             | ~ [DistributionShape(centralMoments)](https://essentia.upf.edu/reference/std_DistributionShape.html) |
| Audio Harmonicity          | Harmonic Ratio             | /                             | /                                   |
|                            | Upper Limit of Harmonicity | /                             | /                                   |
| Other non MPEG-7           | Zero Crossing Rate         | [zero_crossing_rate(y)](https://librosa.org/doc/main/generated/librosa.feature.zero_crossing_rate.html#librosa.feature.zero_crossing_rate)         | [ZeroCrossingRate(signal)](https://essentia.upf.edu/reference/std_ZeroCrossingRate.html)            |
|                            | Spectral Roll off Freq     | [spectral_rolloff(y, sr, ...)](https://librosa.org/doc/main/generated/librosa.feature.spectral_rolloff.html#librosa.feature.spectral_rolloff)  | [RollOff(spectrum)](https://essentia.upf.edu/reference/std_RollOff.html)                   |
|                            | Spectral Flux              | /                             | [Flux(spectrum)](https://essentia.upf.edu/reference/std_Flux.html)                      |
| Timbral Descriptors        | Log Attack Time            | /                             | [LogAttackTime(signal)](https://essentia.upf.edu/reference/std_LogAttackTime.html)               |
|                            | Temporal Centroid          | /easy to do by hand           | ~ [TCToTotal(envelope)](https://essentia.upf.edu/reference/std_TCToTotal.html)               |
|                            | MFCC                       | [mfcc(y, sr, ...)](https://librosa.org/doc/main/generated/librosa.feature.mfcc.html#librosa.feature.mfcc)              | [MFCC(spectrum)](https://essentia.upf.edu/reference/std_MFCC.html)                      |
| Altro                      | Altro                      | [reference](https://librosa.org/doc/main/feature.html)                     | [reference](https://essentia.upf.edu/algorithms_reference.html)                           |
|                            |                            |                               | [how to work with python](https://essentia.upf.edu/essentia_python_tutorial.html)             |
|                            | Altra roba interessante    |                               |                                     |
|                            | [Urban sound classif.1](https://towardsdatascience.com/urban-sound-classification-part-1-99137c6335f9)      |                               |                                     |
|                            | [Urban sound classif.2](https://towardsdatascience.com/urban-sound-classification-part-2-sample-rate-conversion-librosa-ba7bc88f209a)      |                               |                                     |

# CMLS_HW1


[k nearest neighbours](https://scikit-learn.org/stable/modules/neighbors.html#classification)  
[GMM](https://scikit-learn.org/stable/modules/mixture.html)  
[SVM](https://scikit-learn.org/stable/modules/svm.html#svm-classification)  

| Type                       | Feature                    | Librosa                       | Essentia                            |
|----------------------------|----------------------------|-------------------------------|-------------------------------------|
|                            |                            | librosa.feature               | f                                   |
| Basic Descriptors          | Audio Waveform             | np.max/np.min ?               | //                                  |
|                            | Audio Power                | ~ rms(y, S)                   | InstantPower(array)                 |
| Basic Spectral Descriptors | Audio Spectral Envelope    | /                             | ~ Envelope(signal)                  |
|                            | Audio Spectrum Centroid    | spectral_centroid(y, sr, ...) | SpectralCentroidTime(array)         |
|                            | Audio Spectrum Spread      | /                             | ~ DistributionShape(centralMoments) |
| Audio Harmonicity          | Harmonic Ratio             | /                             | /                                   |
|                            | Upper Limit of Harmonicity | /                             | /                                   |
| Other non MPEG-7           | Zero Crossing Rate         | zero_crossing_rate(y)         | ZeroCrossingRate(signal)            |
|                            | Spectral Roll off Freq     | spectral_rolloff(y, sr, ...)  | RollOff(spectrum)                   |
|                            | Spectral Flux              | /                             | Flux(spectrum)                      |
| Timbral Descriptors        | Log Attack Time            | /                             | LogAttackTime(signal)               |
|                            | Temporal Centroid          | /easy to do by hand           | ~ TCToTotal(envelope)               |
|                            | MFCC                       | mfcc(y, sr, ...)              | MFCC(spectrum)                      |
| Altro                      | Altro                      | [reference](https://librosa.org/doc/main/feature.html)                     | [reference](https://essentia.upf.edu/algorithms_reference.html)                           |
|                            |                            |                               | [how to work with python](https://essentia.upf.edu/essentia_python_tutorial.html)             |
|                            | Altra roba interessante    |                               |                                     |
|                            | [Urban sound classif.1](https://towardsdatascience.com/urban-sound-classification-part-1-99137c6335f9)      |                               |                                     |
|                            | [Urban sound classif.2](https://towardsdatascience.com/urban-sound-classification-part-2-sample-rate-conversion-librosa-ba7bc88f209a)      |                               |                                     |

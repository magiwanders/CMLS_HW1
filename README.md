# CMLS_HW1
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
| Altro                      | Altro                      | reference                     | reference                           |
|                            |                            |                               | how to work with python             |
|                            | Altra roba interessante    |                               |                                     |
|                            | Urban sound classif.1      |                               |                                     |
|                            | Urban sound classif.2      |                               |                                     |

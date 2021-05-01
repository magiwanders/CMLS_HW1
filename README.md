# CMLS HW1 - Urban Sound Classification with Support Vector Machines
## Folder structure:
* [source code folder](src/): contains all Colab notebooks for dataset analysis, feature extraction, training and validation. * 
* [report folder](report/): contains the report of the work, which explains in detail the reasoning behind the implementaion. Both the Latex code and compiled PDF are provided. 
* [guidelines folder](guidelines/): contains all the guidelines and requirements for the homework.

## Summary
The implementation of the classifier was divided into different steps, clearly separeted one from the other.
The first step was the preliminary study of the dataset, based on the analysis of the .csv file, that helped to obtain the statistical information about the distribution of the classes.
This was followed by the feature extraction. For this purpose, the features extracted were the MFCCs, and in particular, for the evaulation, the statistics considered were:

1. Minimum
2. Maximum
3. Mean
4. Median
5. Variance

All the data were saved in a JSON file, in order to make the training part independent from the feature extraction.

Finally, the classifier were trained using Support Vector Machines (SVMs) with 10-fold cross validation. To make the feature computation and training procedure faster, parallelization was applied whenever possible.

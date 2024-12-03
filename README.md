# INFO 5871 Final Project
## Fairness in fNIRS: How Underrepresentation Affects Augmentation
By Anna Rahn

### Data Processing
The original data is available in MATLAB structures here: https://figshare.com/articles/dataset/Open_access_fNIRS_dataset_for_classification_of_the_unilateral_finger-_and_foot-tapping/9783755/1

The authors provide an example of preprocessing, feature extraction, classification here: https://github.com/JaeyoungShin/fNIRS-dataset. I use this script as a base for saving the preprocessed data, timestamps, and labels. My version is saved as matlab_data_processing_and_classification.m

### Generating Synthetic Data
DoppelGANger is a generative adversarial network (GAN) that generates multivariate time-series data. ydata-synthetic implements this architecture in their package and provides an example here: https://github.com/ydataai/ydata-synthetic/blob/dev/examples/timeseries/DoppelGANger_FCC_MBA_Dataset.ipynb. I use this notebook as a base for augmenting the fNIRS dataset, and my version is saved as DoppelGANger.ipynb.

### Evaluating Synthetic Data
demographics.py generates a statistical overview of the dataset, including how many examples there are of each trial and label. The script also creates bar charts of both channel and label distribution to enable visual comparison.

Another method of evaluating synthetic data is testing the utility, or the usefulness in other applications. The tsai package provides many useful classification and prediction functions with an example here: https://colab.research.google.com/github/timeseriesAI/tsai/blob/master/tutorial_nbs/01_Intro_to_Time_Series_Classification.ipynb. I use this notebook as a base for classifying existing samples and predicting the label for new, unseen samples.

### Future Directions
I plan on testing both the real and reduced-demographic datasets on downstream applications such as prediction. This will allow me to explore how underrepresentation affects other machine learning models, and see if synthetic data can help improve this performance. Additionally, I used only 10 of the 30 total participants in the original MATLAB data - I will explore how the inclusion of all participants affects the existing results.
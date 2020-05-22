# Brainhack School 2020 Project

Team contributors: Stephanie Alley

![Brain visual](brain-image.jpg)

## Summary

## Project definition

### Background
I am a third year PhD student at Polytechnique with a background in MRI. My primary goal for this project is to become more proficient with tools that further open, reproducible science. Even the most valiant attempts at sharing data and code can fall short in terms of reproducibility, so I aim to incorporate multiple tools and strategies to promote the reliable reproducibility of this project.

One important source of variability across studies is a lack of standardization in preprocessing steps. This project will focus on the effect that preprocessing choices may have on the prediction performance of a machine learning model. Specifically, two processing steps that affect the extraction of functional signal will be examined: atlas choice and confound removal.

The impact of these choices will be assessed by evaluating the prediction performance of a machine learning model. This model will be based on the Support Vector Regressor model used in Week 1 for age prediction. A separate model will be trained for each preprocessing option. The prediction performance will then be evaluated by calculating the accuracy and mean absolute error of each model.

### Tools
* Python
* Docker
* Git/GitHub
* Nilearn
* DataLad
* Jupyter notebooks
* Visualization (plotly)

### Data
rs-fMRI brain development dataset based on viewing of short animated film (obtained from OpenNeuro as ds000228)<sup>1</sup>
* 155 subjects
  * 122 children
  * 33 adults

### Deliverables
* README.md
* Jupyter notebook
* Python script
* Requirements.txt
* Presentation slides

## References
1. Richardson, H., Lisandrelli, G., Riobueno-Naylor, A., & Saxe, R. (2018). Development of the social brain from age three to twelve years. Nature Communications, 9(1). https://doi.org/10.1038/s41467-018-03399-2

# Brainhack School 2020 Project

Team contributors: Stephanie Alley

![Brain visual](brain-image.jpg)

## Summary
Functional MRI (fMRI) is an important modality for studying brain function. Machine learning models are often used to analyze fMRI data, whether it be a simple classification or regression problem or something more complex. While the focus of a study is often centered on the model architecture, data preprocessing also plays a vital role in a model's success. This project will explore the effect that various preprocessing options may have on the prediction performance of a machine learning model for age prediction using resting state fMRI.

## Project definition

### Background
I am a third year PhD student at Polytechnique with a background in MRI. My primary goal for this project is to become more proficient with tools that further open, reproducible science. Even the most valiant attempts at sharing data and code can fall short in terms of reproducibility, so I aim to incorporate multiple tools and strategies to promote the reliable reproducibility of this project.

One important source of variability across studies is a lack of standardization in preprocessing steps. This project will focus on the effect that preprocessing choices may have on the prediction performance of a machine learning model. Specifically, two processing steps that affect the extraction of functional signal will be examined: atlas choice and confound removal.

The impact of these choices will be assessed by evaluating the prediction performance of a machine learning model. This model will be based on the Support Vector Regressor model used in Week 1 for age prediction. A separate model will be trained for each preprocessing option. The prediction performance will then be evaluated by calculating the accuracy and mean absolute error of each model.

### Tools
* Python for processing, analysis, and visualization
* Docker for creating an isolated environment for the processing and analysis that can be shared to improve reproducibility
* Git/GitHub for version control of the project, including the markdown document and the code
* Nilearn for implementation of the machine learning model
* DataLad for version control of the data through processing and analysis
* Jupyter notebooks for accessibility and sharing of the code, analysis, and visualizations
* Visualization (plotly) for creating interactive figures
* Binder for incorporating the GitHub repository, Docker file, and Jupyter notebooks into a live environment that can be easily shared

### Data
rs-fMRI brain development dataset based on viewing of short animated film (obtained from OpenNeuro as ds000228)<sup>1</sup>
* 155 subjects
  * 122 children
  * 33 adults

### Deliverables
* GitHub repository containing all items related to the project, including the markdown document, Docker file, requirements.txt, and Jupyter notebooks
* Complete markdown document (README.md) containing all of the relevant project information
* Docker file to specify the Docker image
* requirements.txt to specify the Python environment
* Jupyter notebook containing the code for the processing and analysis, as well as the visualizations
* Interactive notebook using Binder for reproducible sharing of the entire project
* Presentation slides for final project presentation

#### Week 3 deliverable: data visualization
The deliverable for week 3 can be launched on [Binder](https://mybinder.org/v2/gh/stephaniealley/stephaniealley_bhs2020_data_visualization/master). This interactive figure makes use of plotly and ipywidgets to display regression plots that illustrate the prediction performance of the SVR model on unseen (test set) data. Plots can be viewed for each atlas and confound option included in this portion of the project analysis.

## Results

### Progress overview
* Week 2: Implementing and practicing strategies and tools learned in Week 1</br>
The project was envisioned as an extension of the machine learning tutorial presented in Week 1. Initially, a directory structure was created that adheres to the TIER guidelines. A Jupyter notebook was created to contain the code and visualizations. The pre-processed developmental fMRI data was fetched through nilearn. DataLad datasets were created for both the Original_Data and Analysis_Data directories in order to keep track of data manipulation throughout the analysis. Notable changes to the notebook code and/or the data were consistently tracked using Git/Github and DataLad in order to become more familiar with and accustomed to using these tools.
* Week 3: Expanding upon original machine learning tutorial</br>
In order to explore the effects that various processing options might have on the prediction performance of a machine learning model, four different atlases were chosen from which to extract features: functional (BASC multiscale), structural (AAL), clustering method (Craddock), and linear decomposition (MSDL). Furthermore, the inclusion/exclusion of various confound options was explored: all confounds, CSF signal, WM signal, global signal, and motion correction. Python code was added/modified, particularly using nilearn and scikit-learn, in order to investigate these processing options. Plotting functions provided by seaborn, matplotlib and nilearn were explored to examine options for visualization of results.
* Week 4: Visualization of results and project reproducibility</br>
An interactive figure depicting linear regression plots of model performance on unseen test data was created using plotly. A new Jupyter notebook, bhs2020_project_presentation.ipynb, was created to create the final project presentation using RISE. Binder was used to reproduce the interactive figure as well as the project as a whole.

## References
1. Richardson, H., Lisandrelli, G., Riobueno-Naylor, A., & Saxe, R. (2018). Development of the social brain from age three to twelve years. Nature Communications, 9(1). https://doi.org/10.1038/s41467-018-03399-2

2. Bellec, P., Rosa-Neto, P., Lyttelton, O. C., Benali, H., & Evans, A. C. (2010). Multi-level bootstrap analysis of stable clusters in resting-state fMRI. NeuroImage, 51(3), 1126–1139. https://doi.org/10.1016/j.neuroimage.2010.02.082

3. Bellec, P. (2013). Mining the hierarchy of resting-state brain networks: Selection of representative clusters in a multiscale structure. Proceedings - 2013 3rd International Workshop on Pattern Recognition in Neuroimaging, PRNI 2013, (August), 54–57. https://doi.org/10.1109/PRNI.2013.23

4. Tzourio-Mazoyer, N., Landeau, B., Papathanassiou, D., Crivello, F., Etard, O., Delcroix, N., … Joliot, M. (2002). Automated anatomical labeling of activations in SPM using a macroscopic anatomical parcellation of the MNI MRI single-subject brain. NeuroImage, 15(1), 273–289. https://doi.org/10.1006/nimg.2001.0978

5. Craddock, R. C., James, G. A., Holtzheimer, P. E., Hu, X. P., & Mayberg, H. S. (2012). A whole brain fMRI atlas generated via spatially constrained spectral clustering. Human Brain Mapping, 33(8), 1914–1928. https://doi.org/10.1002/hbm.21333

6. Varoquaux, G., Gramfort, A., Pedregosa, F., Michel, V., & Thirion, B. (2011). Multi-subject dictionary learning to segment an atlas of brain spontaneous activity. Lecture Notes in Computer Science (Including Subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 6801 LNCS, 562–573. https://doi.org/10.1007/978-3-642-22092-0_46

**<img width="791" alt="image" src="https://user-images.githubusercontent.com/104863800/183230189-40d510cd-e433-4dd3-8df7-b5e9e0e40923.png">
**

# Group Members:
* Deeksha Rai
* Fabio Bauer
* Jasper Hilliard
* Mrugsen Gopnarayan
* Prerita Chawla
* Rafe Sharif

### Mentors & TAs
* Dr. Kohitij Kar (Project Mentor)
* Dr. Emeka Ogbuju (Project TA)
* Alish Dipani (Pod TA)


## Abstract

The human visual cortex has a hierarchical representation of stimuli. While the early visual areas (V1, V2, V3) capture orientation and edge detection, later visual areas (V4, Lat Occ) govern initial steps of object recognition. Previous studies have reported a difference in fMRI responses between natural and urban landscapes in certain parts of the brain (Andrews et al. 2015, Gwang-Won Kim et al. 2010). Correspondingly, differential representation shall also be seen for natural (deers, potatoes, trees) and man-made (hat, pen, chair) stimuli in the later visual areas. By utilizing the Kay images fMRI dataset (Kay 2008), here we introduce natural against man-made visual input to address the level of representation such complex stimuli have at each of these levels. We first test our hypothesis by feeding the image dataset into a deep neural net, CORnet-S, to provide us with the possible predictions of encoding in the model layers. Next, we generate dissimilarity matrices (RDM) of the model layers and the Kay image fMRI data to compute the correlations. This will serve to give us a representational similarity analysis (RSA) of the model and the brain. If indeed there is an intrinsic difference between the representation of natural and man-made stimuli, this might indicate that the brain has perhaps developed two-distinct systems for their representations which can be directed through evolution. Further analysis may facilitate the contributory role of evolution towards this paradigm.


## Introduction
## Methods
## Results
## Discussion


### Conclusions
The dissimilarity appeared to be uniform throughout all
the layers. For certain layers, such as V1 and V2, there was no
detectible difference in dissimilarity across categories. However, for
the LatOcc and V4 cortices, there was a measurable effect size
characterized by a bimodal distribution in the dissimilarities of the
response data.

Check root directory for more details on conclusions, plots and visuals.

### Limitations 
This study's lack of time series data, as well as the
RDM process removes a lot of detail from our conclusions.

Despite removal of many unsuitable images, there may be confounding
factors present that could explain some of the differences between
responses to manmade/natural images.

### Futher research 
The results of this brief study have affirmed our
expectation that RSM would be a useful tool for analyzing the brain's
encoding of two different categories of image data. There is opportunity
for a random control trial, for example a study where the stimuli are
tightly controlled for confounding variables, and the image contents
differ ONLY in that one group is natural and the other manmade.
Alternatively, this RSM analysis may be redone as a matched-pairs design
using the original Kay dataset, where each natural image is paired with
a manmade one of similar color and complexity. Any unpaired data would
be thrown out. Both of these alternative studies may yield a more
pronounced effect size and be less subject to confounding variables.

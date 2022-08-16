**<img width="791" alt="image" src="https://user-images.githubusercontent.com/104863800/183230189-40d510cd-e433-4dd3-8df7-b5e9e0e40923.png">
**

## Group Members:
* Deeksha Rai
* Fabio Bauer
* Jasper Hilliard
* Mrugsen Gopnarayan
* Prerita Chawla
* Rafe Sharif

## Mentors & TAs
* Dr. Kohitij Kar (Project Mentor)
* Dr. Emeka Ogbuju (Project TA)
* Alish Dipani (Pod TA)


## Abstract

The human visual cortex has a hierarchical representation of visual stimuli. While the early visual areas (V1, V2) capture orientation and edge detection, later visual areas (V4, Lat Occ, inferior temporal (IT)) govern steps of object recognition. Previous studies have reported that separate brain regions are activated when natural and urban landscapes are viewed. Correspondingly, it is reasonable to expect a differential representation of natural (deers, potatoes, trees) and man-made (hat, pen, chair) stimuli in the later visual areas. We used the Kay images and parsed them into these descriptive categories. To assess the validity of this hypothesis, we first fed Kay images into a deep neural network, CORnet-S which showed distinct representations of the image categories in model layers that correspond to the human brain V4 and IT visual areas. This led us to further test the hypothesis on fMRI BOLD responses to the Kay images, which as expected showed distinct representation of natural and man-made images in later visual areas (V4, LatOcc). However, results obtained from the fMRI dataset had less correlation differences as compared to that of the deep net. This might suggest noisy fMRI dataset which can be addressed by dimensionality reduction in future analyses. Also, unavailability of the IT layer BOLD responses limited our analysis. Overall, the results suggest that the human visual cortex does process natural and manmade images differently. This categorical representation is progressively established in V4, LatOcc, and IT that correspond to later visual areas.


## Introduction

The human brain has evolved in a natural environment but is gradually being exposed to more and more manmade settings. Several studies have highlighted that natural images incite brain regions that are separate from urban images (Andrews et al. 2015, Kim et al. 2010). While these studies have probed how the human brain in general responds to natural vs manmade images, not many have explored the nature of response of the human visual cortex in response to viewing these images. In addition, the level of visual hierarchy at which natural images can be differentiated from manmade ones remains to be addressed. Since the later visual areas (V4, lateral occipital (LatOcc), and inferior temporal (IT) layer) are responsible for encoding complex visual features, we hypothesize that these layers can gradually assort images into natural and manmade categories.
As a proof-of-concept, differences in correlations were seen after feeding these images into a deep neural network, CORnet-S, a close mimic of the ventral visual stream (Kubilius et al. 2019). Results from the deep net were further corroborated by obtaining similar categorical differences in the human brain fMRI data in response to viewing these images. 

## Methods

We use the Kay dataset (Kay et al. 2008) that includes z-scored fMRI BOLD responses (of two subjects) to 1750 normalized grayscale, passively viewed images where each image was repeated 13 times. 
These images were manually relabelled into natural and manmade categories. Representational Dissimilarity Matrices (RDMs) were plotted from the layerwise correlations obtained for the deep net and the BOLD responses. Resulting RDMs were compared through bar plots and histograms for the two image classes across all the layers.

## Results

We found differences in correlations for natural and manmade images across layers V4 and IT of the deep net. This was most pronounced for the IT layer. However, correlation differences for the human visual cortex were seen, although to a lower extent, in V4 and LatOcc. No BOLD responses were available for the IT layer.
V1 and V2 layers showed no correlation differences between natural and manmade images in both CORnet-S and the fMRI responses.

## Discussion

Our study suggests that the human visual cortex is indeed capable of recognising natural images as distinct from manmade images. This is achieved progressively across V4 and LatOcc. 
In the deep net, CORnet-S, this distinction starts in V4 and is highest in the IT layer. This aligns with previous studies which hold IT responsible for core object recognition (Dicarlo et al. 2012). While the availability of IT layer fMRI data would have allowed us uniform comparison with the model, it is clear that both the brain and the machine utilize V4 layer for forming crude levels of distinction between natural and manmade images. In addition, lower correlation differences obtained in the fMRI data could either point towards probable noise in the BOLD responses that can be processed in future analyses or towards the lack of trial wise dataset for each subject.
This categorical representation in the later visual areas can be a result of the recent development of manmade settings in the background of natural environments that humans have always been accustomed to, necessitating the development of two distinct mechanistic systems for their representation in the brain. Future studies can further investigate this assumption.

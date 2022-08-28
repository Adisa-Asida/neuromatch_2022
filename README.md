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

The human visual cortex processes visual stimuli hierarchically. Early visual areas (V1, V2) detect stimulus orientation and edges and later areas of the ventral pathway (V4, Lat Occ, inferior temporal) are responsible for encoding object recognition. Viewing urban and natural scenes leads to significant differences in BOLD response of higher visual areas. Here we asked if this distinction in representation of complex natural and man made visual stimuli extends to earlier visual areas and if state-of-the art convolutional neural networks (CNN) incorporate such a distinction accurately. To assess this, we used an open source fMRI data set of V1-4 and LatOcc BOLD responses to 1750 passively viewed natural and man made images. The same images were fed into the pretrained CORNET-S, a CNN designed to accurately model hierarchical human visual processing layer-wise. To identify differences in representations within and between the human visual cortex and the CNN, we computed representational dissimilarity matrices. The BOLD response to the manmade and natural images show increasing correlation differences for the two categories starting in V4. Such differences were also observed in the CORnet-S. Our results suggest that the human visual cortex does process natural and manmade images differently starting from V4 and that a representational difference is similarly modeled by CORnet-S. In both, categorical representation is progressively more significant with later processing stages.


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

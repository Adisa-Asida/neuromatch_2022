# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 13:28:47 2022

@author: fabio.bauer
"""

# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt
#import pandas as pd
#from IPython.display import display
"""
import os, requests, tarfile
from scipy.stats import zscore
import matplotlib as mpl


from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
"""

fnames = ["kay_labels.npy", "kay_labels_val.npy", "kay_images.npz"]
urls = ["https://osf.io/r638s/download",
        "https://osf.io/yqb3e/download",
        "https://osf.io/ymnjv/download"]



with np.load("kay_images.npz") as dobj:
  dat = dict(**dobj)
labels = np.load('kay_labels.npy')
val_labels = np.load('kay_labels_val.npy')   

category_labels = np.load("label_list.npy", allow_pickle = True)
#category_labels[category_labels[:, 0].argsort()]


#cornet_v1 = np.load(r"C:\Users\fabio.bauer\Desktop\NMA_Project\Kay_natural_images\CORnet-features\CORnet-S_V1_output_feats.npy")
#cornet_v2 = np.load(r"C:\Users\fabio.bauer\Desktop\NMA_Project\Kay_natural_images\CORnet-features\CORnet-S_V2_output_feats.npy")
#cornet_v4 = np.load(r"C:\Users\fabio.bauer\Desktop\NMA_Project\Kay_natural_images\CORnet-features\CORnet-S_V4_output_feats.npy")

#df = pd.DataFrame.from_dict(dat["responses"])
#display(df)
#%%

#Natural and artificial stimuli label mask
lbls_artificial = category_labels[category_labels[:, 1] == "artificial"]
lbls_natural = category_labels[category_labels[:, 1] == "natural"]
lbls_other = category_labels[category_labels[:, 1] == "other"]

#Extract artnat stimuli, sort by stimulus and set as int
lbls_artnat = np.vstack(( lbls_artificial,lbls_natural,))
lbls_artnat[lbls_artnat[:, 0].argsort()]
stimuli_artnat = np.array([int(x) for x in lbls_artnat[:,0]])

#subset artificial and natural stimuli from responses
responses = dat["responses"][stimuli_artnat,:] 
#responses = dat["responses"]

#Extract ROI labels
kay_roi_v1 = dat["roi"] == 1
kay_roi_v2 = dat["roi"] == 2
kay_roi_v4 = dat["roi"] == 6
kay_roi_lo = dat["roi"] == 7

#Extract ROI responses
kay_v1 = responses[:,kay_roi_v1] 
kay_v2 = responses[:,kay_roi_v2] 
kay_v4 = responses[:,kay_roi_v4] 
kay_lo = responses[:,kay_roi_lo] 


#correlations
kay_corrv1 = np.corrcoef(kay_v1)
kay_corrv2 = np.corrcoef(kay_v2)
kay_corrv4 = np.corrcoef(kay_v4)
kay_corrvlo = np.corrcoef(kay_lo)

#RDMs
RDM_v1 = 1 - kay_corrv1
RDM_v2 = 1 - kay_corrv2
RDM_v4 = 1 - kay_corrv4
RDM_lo = 1 - kay_corrvlo
#%%
#%%
plt.subplot(2,2,1)
plt.imshow(RDM_v1[0:1129,0:1129])
plt.title('MRI v1')
plt.colorbar(label='dissimilarity')

plt.subplot(2,2,2)
plt.imshow(RDM_v2[0:1129,0:1129])
plt.title('MRI v2')
plt.colorbar(label='dissimilarity')

plt.subplot(2,2,3)
plt.imshow(RDM_v4[0:1129,0:1129])
plt.title('MRI v4')
plt.colorbar(label='dissimilarity')

plt.subplot(2,2,4)
plt.imshow(RDM_lo[0:1129,0:1129])
plt.title('MRI LatOcc')
plt.colorbar(label='dissimilarity')

plt.tight_layout()
plt.savefig('RDM_cornet.png', dpi=1000)
#%%
def upT(RD):
  ioffdiag = np.triu_indices(RD.shape[0], k=1,m=RD.shape[1])  # indices of off-diagonal elements
  rdm1_offdiag = RD[ioffdiag]
  return rdm1_offdiag
def compareSM(kay,net):
    cornet=net[0:1130,0:1130]
    d1=upT(cornet)
    d2=upT(kay)
    return np.corrcoef(d1,d2)[1,0]
#%%
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(10,8))

avg_art=np.ndarray.flatten(tri(kay_corrv1[0:345,0:345]))
avg_art_nat=np.ndarray.flatten(tri(kay_corrv1[345:1129,0:345]))
avg_nat=np.ndarray.flatten(tri(kay_corrv1[345:1129,345:1129]))
ax1.hist(avg_art,100,[-0.3,0.3],density=True,color='red',alpha=0.6)
ax1.hist(avg_art_nat,100,[-0.3,0.3],density=True,color='blue',alpha=0.6)
ax1.set_ylabel('V1')

avg_art=np.ndarray.flatten(tri(kay_corrv2[0:345,0:345]))
avg_art_nat=np.ndarray.flatten(tri(kay_corrv2[345:1129,0:345]))
avg_nat=np.ndarray.flatten(tri(kay_corrv2[345:1129,345:1129]))
ax2.hist(avg_art,100,[-0.3,0.3],density=True,color='red',alpha=0.6)
ax2.hist(avg_art_nat,100,[-0.3,0.3],density=True,color='blue',alpha=0.6)
ax2.set_ylabel('V2')

avg_art=np.ndarray.flatten(tri(kay_corrv4[0:345,0:345]))
avg_art_nat=np.ndarray.flatten(tri(kay_corrv4[345:1129,0:345]))
avg_nat=np.ndarray.flatten(tri(kay_corrv4[345:1129,345:1129]))
ax3.hist(avg_art,100,[-0.3,0.3],density=True,color='red',alpha=0.6)
ax3.hist(avg_art_nat,100,[-0.3,0.3],density=True,color='blue',alpha=0.6)
ax3.set_ylabel('V4')
#plt.hist(avg_art,100)

#% Just IT
avg_art=np.ndarray.flatten(tri(kay_corrvlo[0:345,0:345]))
avg_art_nat=np.ndarray.flatten(tri(kay_corrvlo[345:1129,0:345]))
avg_nat=np.ndarray.flatten(tri(kay_corrvlo[345:1129,345:1129]))

ax4.hist(avg_art,100,[-0.3,0.3],density=True,color='red',alpha=0.6)
ax4.hist(avg_art_nat,100,[-0.3,0.3],density=True,color='blue',alpha=0.6)
ax4.set_ylabel('LatOcc')
ax4.set_xlabel('Correlation')
#plt.hist(avg_art,100)

# #RDMs
# RDM_v1 = 1 - (kay_v1 @ kay_v1.T) / kay_v1.shape[1]
# RDM_v2 = 1 - (kay_v2 @ kay_v2.T) / kay_v2.shape[1]
# RDM_v4 = 1 - (kay_v4 @ kay_v4.T) / kay_v4.shape[1]
# RDM_lo = 1 - (kay_lo @ kay_lo.T) / kay_lo.shape[1]

#%%
dif=np.zeros((4,1))
dif[0]=Diff_mode(kay_corrv1)
dif[1]=Diff_mode(kay_corrv2)
dif[2]=Diff_mode(kay_corrv4)
dif[3]=Diff_mode(kay_corrvlo)
#%%

#plot
plt.subplot(2,2,1)
plt.imshow(RDM_v1, vmin=-2.0, vmax=2.0)
plt.title('v1')
plt.colorbar(label='dissimilarity')

plt.subplot(2,2,2)
plt.imshow(RDM_v2, vmin=-2.0, vmax=2.0)
plt.title('v2')
plt.colorbar(label='dissimilarity')

plt.subplot(2,2,3)
plt.imshow(RDM_v4, vmin=-2.0, vmax=2.0)
plt.title('v4')
plt.colorbar(label='dissimilarity')

plt.subplot(2,2,4)
plt.imshow(RDM_lo, vmin=-2.0, vmax=2.0)
plt.title('LatOcc')
plt.colorbar(label='dissimilarity')

plt.tight_layout()
plt.savefig('RDM_V124_fmri.png', dpi=600)

#%%

#flatten to plot
artificial_v1 = np.ndarray.flatten(RDM_v1[0:345,0:345])
natural_v1 = np.ndarray.flatten(RDM_v1[345:,345:])

artificial_v2 = np.ndarray.flatten(RDM_v2[0:345,0:345])
natural_v2 = np.ndarray.flatten(RDM_v2[345:,345:])

artificial_v4 = np.ndarray.flatten(RDM_v4[0:345,0:345])
natural_v4 = np.ndarray.flatten(RDM_v4[345:,345:])

artificial_lo = np.ndarray.flatten(RDM_lo[0:345,0:345])
natural_lo = np.ndarray.flatten(RDM_lo[345:,345:])


#plot histograms
#fig, (ax1, ax2, ax3, ax4) = plt.subplots(2, 2, figsize=(10,4))
plt.suptitle("Distributions for natural and artificial stimuli in fMRI", fontsize=12)

plt.subplot(2,2,1)
plt.hist(artificial_v1, 1000, density=True, range = [0.25, 1.7], color = "blue", alpha = 0.3)
plt.hist(natural_v1, 1000, density=True, range = [0.25, 1.7], color = "orange", alpha = 0.3)
plt.title('v1')

plt.subplot(2,2,2)
plt.hist(artificial_v2, 1000, density=True, range = [0.25, 1.7], color = "blue", alpha = 0.3)
plt.hist(natural_v2, 1000, density=True, range = [0.25, 1.7], color = "orange", alpha = 0.3)
plt.title('v2')

plt.subplot(2,2,3)
plt.hist(artificial_v4, 1000, density=True, range = [0.25, 1.7], color = "blue", alpha = 0.3)
plt.hist(natural_v4, 1000, density=True, range = [0.25, 1.7], color = "orange", alpha = 0.3)
plt.title('v4')

plt.subplot(2,2,4)
plt.hist(artificial_lo, 1000, density=True, range = [0.25, 1.7], color = "blue", alpha = 0.3)
plt.hist(natural_lo, 1000, density=True, range = [0.25, 1.7], color = "orange", alpha = 0.3)
plt.title('LatOcc')

"""
plt.legend([l1, l2, l3, l4],     # The line objects
           labels=line_labels,   # The labels for each line
           loc="center right",   # Position of legend
           borderaxespad=0.1,    # Small spacing around legend box
           title="Legend Title"  # Title for the legend
           )
lines_labels = [ax.get_legend_handles_labels() for ax in fig.axes]
lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
fig.legend(lines, labels)
plt.legend(handles, labels, loc='upper center')
"""
plt.savefig('Hist_V124lo_fmri.png', dpi=600)
plt.tight_layout()






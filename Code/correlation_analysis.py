# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 17:46:38 2022

@author: mrugs
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as st
def cnn_order(BadIT,cnnlist):
    OldIT=np.zeros((np.shape(BadIT)))
    for i in range(len(cnnlist)):
        OldIT[i]=BadIT[int(np.where(cnnlist == i)[0])]
    return OldIT
#%%
labels=pd.read_csv('C:\\Users\\mrugs\\Documents\\Courses\\NMA\\kay_images\\labels\labels.csv')
imglist=pd.Series.to_numpy(labels["Image"])
#%%
cnnlist=np.loadtxt('imglist.txt')
cnnlist=np.array([int(x) for x in cnnlist])

#%% Load cnn data
BadV1=np.load("CORnet-S_V1_output_feats.npy")
BadV2=np.load("CORnet-S_V2_output_feats.npy")
#oldV2=np.load("CORnet-S_V2_output_feats.npy")
BadV4=np.load("CORnet-S_V4_output_feats.npy")
BadIT=np.load("CORnet-S_IT_output_feats.npy")
#oldV43=np.load("p_CORnet-S_V4_output_feats.npy")

#%% reorient cnn 
oldV1=cnn_order(BadV1, cnnlist)
oldV2=cnn_order(BadV2, cnnlist)
#oldV2=np.load("CORnet-S_V2_output_feats.npy")
oldV4=cnn_order(BadV4, cnnlist)
oldIT=cnn_order(BadIT, cnnlist)
#%%
v1=oldV1[imglist]
v2=oldV2[imglist]
v4=oldV4[imglist]
IT=oldIT[imglist]
#%% Find Correlations

corr_v1=np.corrcoef(v1)
corr_v2=np.corrcoef(v2)
corr_v4=np.corrcoef(v4)
corr_IT=np.corrcoef(IT)
#%%
rdm_v1=1-abs(corr_v1)
rdm_v2=1-abs(corr_v2)
rdm_v4=1-abs(corr_v4)
rdm_IT=1-abs(corr_IT)

#%% Just v4
avg_art=np.ndarray.flatten(corr_v4[0:345,0:345])
avg_art_nat=np.ndarray.flatten(corr_v4[345:1129,0:345])
avg_nat=np.ndarray.flatten(corr_v4[345:1129,345:1129])
plt.hist(avg_nat,100,[0.3,0.8],density=True)
plt.hist(avg_art_nat,100,[0.3,0.8],density=True)

#plt.hist(avg_art,100)
plt.show()
#%% Just IT
avg_art=np.ndarray.flatten(corr_IT[0:345,0:345])
avg_art_nat=np.ndarray.flatten(corr_IT[345:1129,0:345])
avg_nat=np.ndarray.flatten(corr_IT[345:1129,345:1129])
#%%

plt.hist(avg_nat,100,[0.0,0.6],density=True,color='red',alpha=0.6)
plt.hist(avg_art_nat,100,[0.0,0.6],density=True,color='blue',alpha=0.6)
plt.axvline(x=st.mode(avg_art_nat))
plt.axvline(x=st.mode(avg_nat))
plt.xlabel('Correlation')
#plt.hist(avg_art,100)
plt.show()
#%%
plt.subplot(2,2,1)
plt.imshow(rdm_v1[0:1129,0:1129])
plt.title('Cornet-S v1')
plt.colorbar(label='dissimilarity')

plt.subplot(2,2,2)
plt.imshow(rdm_v2[0:1129,0:1129])
plt.title('Cornet-S v2')
plt.colorbar(label='dissimilarity')

plt.subplot(2,2,3)
plt.imshow(rdm_v4[0:1129,0:1129])
plt.title('Cornet-S v4')
plt.colorbar(label='dissimilarity')

plt.subplot(2,2,4)
plt.imshow(rdm_IT[0:1129,0:1129])
plt.title('Cornet-S IT')
plt.colorbar(label='dissimilarity')

plt.tight_layout()
plt.savefig('RDM_cornet.png', dpi=1000)
#%%
plt.subplot(1,2,1)
image = plt.imshow(rdm_IT, vmin=0.0, vmax=1.0)
# plt.set_xticks([344,1129])
# plt.set_yticks([344,1129])
#cbar = plt.colorbar(image, label='disimilarity')
plt.subplot(1,2,2)
image = plt.imshow(rdm_IT, vmin=0.0, vmax=1.0)
# plt.set_xticks([344,1129])
# plt.set_yticks([344,1129])
cbar = plt.colorbar(image, label='disimilarity')
plt.tight_layout()

#%% Correlation difference hist
def upT(RD):
  ioffdiag = np.triu_indices(RD.shape[0], k=1,m=RD.shape[1])  # indices of off-diagonal elements
  rdm1_offdiag = RD[ioffdiag]
  return rdm1_offdiag
#%% Just v4
def Diff_mode(corrD):
    avg_art=upT(corrD[0:344,0:344])
    avg_art_nat=upT(corrD[345:1129,0:345])
    avg_nat=upT(corrD[345:1129,345:1129])
    diff=[np.median(avg_art)-np.median(avg_art_nat)]
    return diff
def tri(sq):
    return sq
    
#%%
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(10,8))

avg_art=np.ndarray.flatten(tri(corr_v1[0:345,0:345]))
avg_art_nat=np.ndarray.flatten(tri(corr_v1[345:1129,0:345]))
avg_nat=np.ndarray.flatten(tri(corr_v1[345:1129,345:1129]))
ax1.hist(avg_art,100,[0.0,0.8],density=True,color='red',alpha=0.6)
ax1.hist(avg_art_nat,100,[0.0,0.8],density=True,color='blue',alpha=0.6)
ax1.set_ylabel('V1')

avg_art=np.ndarray.flatten(tri(corr_v2[0:345,0:345]))
avg_art_nat=np.ndarray.flatten(tri(corr_v2[345:1129,0:345]))
avg_nat=np.ndarray.flatten(tri(corr_v2[345:1129,345:1129]))
ax2.hist(avg_art,100,[0.0,0.8],density=True,color='red',alpha=0.6)
ax2.hist(avg_art_nat,100,[0.0,0.8],density=True,color='blue',alpha=0.6)
ax2.set_ylabel('V2')

avg_art=np.ndarray.flatten(tri(corr_v4[0:345,0:345]))
avg_art_nat=np.ndarray.flatten(tri(corr_v4[345:1129,0:345]))
avg_nat=np.ndarray.flatten(tri(corr_v4[345:1129,345:1129]))
ax3.hist(avg_art,100,[0.0,0.8],density=True,color='red',alpha=0.6)
ax3.hist(avg_art_nat,100,[0.0,0.8],density=True,color='blue',alpha=0.6)
ax3.set_ylabel('V4')
#plt.hist(avg_art,100)

#% Just IT
avg_art=np.ndarray.flatten(tri(corr_IT[0:345,0:345]))
avg_art_nat=np.ndarray.flatten(tri(corr_IT[345:1129,0:345]))
avg_nat=np.ndarray.flatten(tri(corr_IT[345:1129,345:1129]))

ax4.hist(avg_art,100,[0.0,0.8],density=True,color='red',alpha=0.6)
ax4.hist(avg_art_nat,100,[0.0,0.8],density=True,color='blue',alpha=0.6)
ax4.set_ylabel('IT')
ax4.set_xlabel('Correlation')
#plt.hist(avg_art,100)

#%% Diff plot
dif=np.zeros((4,1))
dif[0]=Diff_mode(corr_v1)
dif[1]=Diff_mode(corr_v2)
dif[2]=Diff_mode(corr_v4)
dif[3]=Diff_mode(corr_IT)

#%%
cate=np.array(['V1','V2','V4','LatOcc'])
y = np.array([-0.00680292,-0.00438011,0.00937553,0.0656807])
z = np.array([0.00102368,0.000240777,0.00548728,0.0148679])

sns.barplot(cate,z)
plt.ylabel('Difference in correlation')
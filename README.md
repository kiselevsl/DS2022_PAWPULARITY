# PAWPULARITY IDS22

This repository contains the code for Pawpularity IDS2022 project made by Viacheslav Kiselev

## Required packkages

* Fasai
* Pytorch
* Pandas
* timm
* NumPy
* sklearn
* gc

## Models

Models have to be dowmloaded separately from kaggle: <https://kaggle.com/datasets/596d79d4d3157fb51c835e39323470ebb563a8632c0a6ec1c4bb2cbbf9270690> (~9 Gb)

## How to run

**Install the required packages** ;)

**PC_version.ipynb** - kagle notebook changed in a way to be run on the PC, inside it has traning, learning rate optimization and test cells. Somethings should be changed in order to run the notebook, code contains commetns in such places.

**Kaggle_version.ipynb** - same thing as PC version but paths can be left the same, in order to be run, the dataset mentioned in Models section must be added to the notebook enviroment together with Pawpularity competition: <https://www.kaggle.com/competitions/petfinder-pawpularity-score>. Also it is comprised out of several versions of kagle notebooks because training and saving models in one go on kaggle is impossible since it required more memory than offered in the output directory. Also two more dataset need to be added one for swin_trasnofrmer: <https://www.kaggle.com/datasets/tanlikesmath/swin-transformer> and another one for timm: <https://www.kaggle.com/datasets/kozodoi/timm-pytorch-image-models>

**Feature_anal.ipynb** - notebook used for feature analysis and illustrations creation does not require many chages apart from chaging the path to the csv files 


import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import mean_squared_error
import gc
from fastai.vision.all import *

def seed(n):
    set_seed(n, reproducible=True)
    torch.manual_seed(n)
    torch.cuda.manual_seed(n)
    torch.backends.cudnn.deterministic = True
    torch.use_deterministic_algorithms = True

# PRETRAINED='beit_large_patch16_224
seed(228)

IMG_SIZE = 224
N_FOLDS = 10
BATCH_SIZE = 32

df = pd.read_csv("train.csv")
df["Jpg"] = df["Id"].apply(lambda x: ("D:\data_semen\project\train}/train'", x + ".jpg"))
df['norm_score'] = df['Pawpularity']/100

df.describe()
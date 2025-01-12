import os
import glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
# import wandb
from gen_call import main

import torch
print('torch.__version__', torch.__version__)
# run = wandb.init(anonymous="must")
# artifact_uri = 'img2dataset'  # @param ["img2dataset", "kaggle dataset"] {allow-input: false}
# if artifact_uri == 'img2dataset':
#     artifact_uri = 'divedeepai/img2dataset_train_transformer/trained-dalle:latest'
# else:
#     artifact_uri = "divedeepai/dalle_train_transformer/trained-dalle:v51"
# artifact = run.use_artifact(artifact_uri, type='model')
# artifact_dir = artifact.download(root='/output/')

# @markdown # **3** Try out the model. @markdown #### Results will be saved in the outputs directory. Refresh (right
# click the folder -> refresh) if you dont see the result inside the folder.

checkpoint_path = "/input/dalle.pt"

text = "women silk dress"  # @param {type:"string"}
# green silk dress with puff shoulders
# black womens handbag with orange handle

num_images = 1  # @param {type:"integer"}
batch_size = 1  # @param {type:"integer"}

text_cleaned = text.replace(" ", "_")
_folder = f"/output/"

# input_img_path = "/input/img.jpg"
# !python /content/DALLE-pytorch/generate.py --dalle_path=$checkpoint_path --text="$text" --num_images=$num_images
# --batch_size=$batch_size --outputs_dir="$_folder" ; wait;


main(dalle_path=checkpoint_path, text=text, num_images=num_images, batch_size=batch_size, outputs_dir=_folder)

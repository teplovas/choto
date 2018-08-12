import sys, os
from PIL import Image, ImageFilter
import keras
import cv2
import numpy as np
from keras.applications import VGG16

data = sys.argv[1]
embeds = sys.argv[2]


def renormalize_picture(pict):
    im = cv2.resize(cv2.imread(pict), (224, 224)).astype(np.float32)
    im = np.expand_dims(im, axis=0)
    return im

def get_embeddings_for_data(picture, model):
    res = model.predict(renormalize_picture(picture))
    return res

def get_model():
     return VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

if __name__ == "__main__":
    model = get_model()
    with open(embeds, "w") as out_file:
        for sample in os.listdir(data):
	    embeds = get_embeddings_for_data(os.path.join(data, sample), model)
	out_file.write("\t".join([str(x) for x in embeds]) + "\n")

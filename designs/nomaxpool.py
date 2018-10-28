import numpy as np

from skimage.transform import resize

from keras.models import Model
from keras.optimizers import Adam
from keras.layers import BatchNormalization
from keras.layers import Input, concatenate, Conv2D, MaxPooling2D, Conv2DTranspose

from designs.components.loss_functions import dice_coef_loss
from designs.components.loss_functions import dice_coef


# CITATION
# - U-Net: https://arxiv.org/pdf/1505.04597.pdf
#   Note: they use 20 input layers.


# resize input matrix
resize_image_height_to = 128
resize_image_width_to = 128


# MODEL
def build():
    print("NO MAX POOL")
    print('using model: straight up convolution, ditched the maxpooling') 

    # expected input shape
    inputs = Input((resize_image_height_to, resize_image_width_to, 1)) #  1 channel, x rows, y = x columns

    conv1 = Conv2D(64, (3, 3), activation='relu', padding='same')(inputs) # -> convolution to  features: 32     window: 3
    conv2 = Conv2D(64, (3, 3), activation='relu', padding='same')(conv1)  # -> convolution to  features: 32     window: 9
    conv3 = Conv2D(128, (5, 5), activation='relu', padding='same')(conv2)  # -> convolution to  features: 64     window: 18
    conv4 = Conv2D(128, (5, 5), activation='relu', padding='same')(conv3)  # -> convolution to  features: 64     window: 18
    conv5 = Conv2D(128, (5, 5), activation='relu', padding='same')(conv4) # -> convolution to  features: 128    window: 54 
    conv6 = Conv2D(264, (5,5), activation='relu', padding='same')(conv5) # -> convolution to  features: 128    window: 162
    conv7 = Conv2D(264, (5,5), activation='relu', padding='same')(conv6) # -> convolution to  features: 256    window: 486
    conv8 = Conv2D(128, (5,5), activation='relu', padding='same')(conv7) # -> convolution to  features: 256    window: 1458
    conv9 = Conv2D(128, (5,5), activation='relu', padding='same')(conv8) # -> convolution to  features: 256    window: 1458
    cake0 = concatenate([conv1,
                         conv2,
                         conv3,
                         conv4,
                         conv5,
                         conv6,
                         conv7,
                         conv8,
                         conv9], axis=-1)

    conv10 = Conv2D(1, (1, 1), activation='sigmoid')(cake0)

    model = Model(inputs=[inputs], outputs=[conv10])
    model.compile(optimizer=Adam(lr=1e-3), loss=dice_coef_loss, metrics=[dice_coef])

    return model




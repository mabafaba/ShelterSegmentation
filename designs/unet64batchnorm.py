import numpy as np

from skimage.transform import resize

from keras.models import Model
from keras.optimizers import Adam
from keras.layers import BatchNormalization
from keras.layers import Input, concatenate, Conv2D, MaxPooling2D, Conv2DTranspose

from designs.components.loss_functions import dice_coef_loss
from designs.components.loss_functions import dice_coef


# CITATION
# - https://blog.deepsense.ai/deep-learning-for-satellite-imagery-via-image-segmentation/
# - https://deepsense.ai/wp-content/uploads/2017/04/architecture_overview.png
#   Note: they use 20 input layers.


# resize input matrix
resize_image_height_to = 128
resize_image_width_to = 128

#Model Parameter
batchnorm_momentum = 0.01

# MODEL
def build():

    print('using model: unet64batchnorm (unet64filters but with batch normalization)') 

    # expected input shape
    inputs = Input((resize_image_height_to, resize_image_width_to, 1))
    conv1 = Conv2D(64, (3, 3), activation='relu', padding='same')(inputs)
    bn1 = BatchNormalization(momentum=batchnorm_momentum)(conv1)
    conv1 = Conv2D(64, (3, 3), activation='relu', padding='same')(bn1)
    bn1 = BatchNormalization(momentum=batchnorm_momentum)(conv1)
    conv1 = Conv2D(64, (3, 3), activation='relu', padding='same')(bn1)
    pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)

    bn2 = BatchNormalization(momentum=batchnorm_momentum)(pool1)
    conv2 = Conv2D(64, (3, 3), activation='relu', padding='same')(bn2)
    bn2 = BatchNormalization(momentum=batchnorm_momentum)(conv2)
    conv2 = Conv2D(64, (3, 3), activation='relu', padding='same')(bn2)
    bn2 = BatchNormalization(momentum=batchnorm_momentum)(conv2)
    conv2 = Conv2D(64, (3, 3), activation='relu', padding='same')(bn2)
    pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)

    bn3 = BatchNormalization(momentum=batchnorm_momentum)(pool2)
    conv3 = Conv2D(64, (3, 3), activation='relu', padding='same')(pool2)
    bn3 = BatchNormalization(momentum=batchnorm_momentum)(conv3)
    conv3 = Conv2D(64, (3, 3), activation='relu', padding='same')(bn3)
    bn3 = BatchNormalization(momentum=batchnorm_momentum)(conv3)
    conv3 = Conv2D(64, (3, 3), activation='relu', padding='same')(bn3)
    pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)

    bn4 = BatchNormalization(momentum=batchnorm_momentum)(pool3)
    conv4 = Conv2D(64, (3, 3), activation='relu', padding='same')(pool3)
    bn4 = BatchNormalization(momentum=batchnorm_momentum)(conv4)
    conv4 = Conv2D(64, (3, 3), activation='relu', padding='same')(bn4)
    bn4 = BatchNormalization(momentum=batchnorm_momentum)(conv4)
    conv4 = Conv2D(64, (3, 3), activation='relu', padding='same')(bn4)
    pool4 = MaxPooling2D(pool_size=(2, 2))(conv4)

    bn5 = BatchNormalization(momentum=batchnorm_momentum)(pool4)
    conv5 = Conv2D(64, (3, 3), activation='relu', padding='same')(pool4)
    bn5 = BatchNormalization(momentum=batchnorm_momentum)(conv5)
    conv5 = Conv2D(64, (3, 3), activation='relu', padding='same')(bn5)

    up6 = concatenate([Conv2DTranspose(64, (2, 2), strides=(2, 2), padding='same')(conv5), conv4], axis=3)
    bn6 = BatchNormalization(momentum=batchnorm_momentum)(up6)
    conv6 = Conv2D(64, (3, 3), activation='relu', padding='same')(bn6)
    bn6 = BatchNormalization(momentum=batchnorm_momentum)(conv6)
    conv6 = Conv2D(64, (3, 3), activation='relu', padding='same')(bn6)
    bn6 = BatchNormalization(momentum=batchnorm_momentum)(conv6)
    conv6 = Conv2D(64, (3, 3), activation='relu', padding='same')(bn6)

    up7 = concatenate([Conv2DTranspose(64, (2, 2), strides=(2, 2), padding='same')(conv6), conv3], axis=3)
    bn7 = BatchNormalization(momentum=batchnorm_momentum)(up7)
    conv7 = Conv2D(64, (3, 3), activation='relu', padding='same')(up7)
    bn7 = BatchNormalization(momentum=batchnorm_momentum)(conv7)
    conv7 = Conv2D(64, (3, 3), activation='relu', padding='same')(conv7)
    bn7 = BatchNormalization(momentum=batchnorm_momentum)(conv7)
    conv7 = Conv2D(64, (3, 3), activation='relu', padding='same')(conv7)

    up8 = concatenate([Conv2DTranspose(64, (2, 2), strides=(2, 2), padding='same')(conv7), conv2], axis=3)
    bn8 = BatchNormalization(momentum=batchnorm_momentum)(up8)
    conv8 = Conv2D(64, (3, 3), activation='relu', padding='same')(up8)
    bn8 = BatchNormalization(momentum=batchnorm_momentum)(conv8)
    conv8 = Conv2D(64, (3, 3), activation='relu', padding='same')(conv8)
    bn8 = BatchNormalization(momentum=batchnorm_momentum)(conv8)
    conv8 = Conv2D(64, (3, 3), activation='relu', padding='same')(conv8)

    up9 = concatenate([Conv2DTranspose(64, (2, 2), strides=(2, 2), padding='same')(conv8), conv1], axis=3)
    bn9 = BatchNormalization(momentum=batchnorm_momentum)(up9)
    conv9 = Conv2D(64, (3, 3), activation='relu', padding='same')(up9)
    bn9 = BatchNormalization(momentum=batchnorm_momentum)(conv9)
    conv9 = Conv2D(64, (3, 3), activation='relu', padding='same')(conv9)
    bn9 = BatchNormalization(momentum=batchnorm_momentum)(conv9)
    conv9 = Conv2D(64, (3, 3), activation='relu', padding='same')(conv9)

    conv10 = Conv2D(1, (1, 1), activation='sigmoid')(conv9)

    model = Model(inputs=[inputs], outputs=[conv10])

    model.compile(optimizer=Adam(lr=1e-5), loss=dice_coef_loss, metrics=[dice_coef])

    return model




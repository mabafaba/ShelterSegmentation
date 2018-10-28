from __future__ import print_function

# parameters:
model_str='unet64filters' # select model here
from designs import unet64filters as design
data_path = '/Volumes/2/shelterdata/180505_v1' 
ckpt_file = data_path+'/internal/checkpoints/weights_'+model_str+'.h5'
img_width = 128
img_height = 128
# this script only does the filters of one layer at a time.
# you'll have to run model.summary() to see all available layer names,
# if you run this script it will show model.summary() including the layer names.
num_input_layers = 1 # our input images have only one layer always

layer_name = "conv2d_2" 
number_of_filters_to_visualise = 64
output_image_grid_side_length=8 # must be square root of number_of_filters_to_visualise


# gradient ascent parameters:
step = 100000. # 1.0 seems to work ok
num_steps_ascent = 30 # example used 20 with decent results



# all layers:

layer_names = [
 # "conv2d_1",
"conv2d_2"
# ,"conv2d_3"
,"conv2d_4"
,"conv2d_5"
,"conv2d_6"   
,"conv2d_7"
,"conv2d_8"
,"conv2d_9"
# ,"conv2d_10"
,"conv2d_11"
,"conv2d_12"
,"conv2d_13"
,"conv2d_14"
,"conv2d_15"
,"conv2d_16"
,"conv2d_17"
# ,"conv2d_18"
]




##############################################################################
# this follows roughly:::
# https://blog.keras.io/how-convolutional-neural-networks-see-the-world.html
##############################################################################

# dependencies:
from keras import applications
from keras import backend as K
import numpy as np
from keras.models import Model
from keras.optimizers import Adam
from keras.layers import BatchNormalization
from keras.callbacks import ModelCheckpoint,CSVLogger,EarlyStopping
from keras.layers import Input, concatenate, Conv2D, MaxPooling2D, Conv2DTranspose
K.set_image_data_format('channels_last')  # TF dimension ordering in this code


import numpy as np
import time
from keras.preprocessing.image import save_img
from keras import backend as K




####### new part:


# the name of the layer we want to visualize
# (see model definition at keras/applications/vgg16.py)

# util function to convert a tensor into a valid image


def deprocess_image(x):
    # normalize tensor: center on 0., ensure std is 0.1
    x -= x.mean()
    x /= (x.std() + K.epsilon())
    x *= 0.1

    # clip to [0, 1]
    x += 0.5
    x = np.clip(x, 0, 1)

    # convert to RGB array
    x *= 255
    if K.image_data_format() == 'channels_first':
        x = x.transpose((1, 2, 0))
    x = np.clip(x, 0, 255).astype('uint8')
    return x


# load model & model weights:
model = design.build()
model.load_weights(ckpt_file)
print('Model loaded.')
model.summary()


# this is the placeholder for the input images
input_img = model.input


# get the symbolic outputs of each "key" layer (we gave them unique names).
layer_dict = dict([(layer.name, layer) for layer in model.layers[1:]])
	

def normalize(x):
    # utility function to normalize a tensor by its L2 norm
    return x / (K.sqrt(K.mean(K.square(x))) + K.epsilon())



for layer_name in layer_names:
    print('Processing layer %s' % layer_name)
    kept_filters = []
    for filter_index in range(number_of_filters_to_visualise):
        # we only scan through the first 200 filters,
        # but there are actually 512 of them
        print('Processing filter %d' % filter_index)
        start_time = time.time()

        # we build a loss function that maximizes the activation
        # of the nth filter of the layer considered
        layer_output = layer_dict[layer_name].output
        if K.image_data_format() == 'channels_first':
            loss = K.mean(layer_output[:, filter_index, :, :])
        else:
            loss = K.mean(layer_output[:, :, :, filter_index])

        # we compute the gradient of the input picture wrt this loss
        grads = K.gradients(loss, input_img)[0]

        # normalization trick: we normalize the gradient
        grads = normalize(grads)

        # this function returns the loss and grads given the input picture
        iterate = K.function([input_img], [loss, grads])

            

        # we start from a gray image with some random noise
        if K.image_data_format() == 'channels_first':
            input_img_data = np.random.random((1, num_input_layers, img_width, img_height))
        else:
            input_img_data = np.random.random((1, img_width, img_height, num_input_layers))
        input_img_data = (input_img_data - 0.5) * 20 + 128

        # we run gradient ascent for 20 steps
        for i in range(num_steps_ascent):
            loss_value, grads_value = iterate([input_img_data])
            input_img_data += grads_value * step

            # print('Current loss value:', loss_value)
            if loss_value <= 0.:
                # some filters get stuck to 0, we can skip them
                break

        # decode the resulting input image
        # we want this independent from filter 0:
        # if loss_value > 0:
        img = deprocess_image(input_img_data[0])
        kept_filters.append((img, loss_value))
        end_time = time.time()
        print('Filter %d processed in %ds' % (filter_index, end_time - start_time))

    # we will stich the best 64 filters on a 8 x 8 grid.
    n = output_image_grid_side_length

    # the filters that have the highest loss are assumed to be better-looking.
    # we will only keep the top 64 filters.
    kept_filters.sort(key=lambda x: x[1], reverse=True)
    kept_filters = kept_filters[:n * n]

    # build a black picture with enough space for
    # our 8 x 8 filters of size 128 x 128, with a 5px margin in between
    margin = 5
    width = n * img_width + (n - 1) * margin
    height = n * img_height + (n - 1) * margin
    stitched_filters = np.zeros((width, height, num_input_layers))

    # fill the picture with our saved filters
    for i in range(n):
        for j in range(n):
            img, loss = kept_filters[i * n + j]
            width_margin = (img_width + margin) * i
            height_margin = (img_height + margin) * j
            stitched_filters[
                width_margin: width_margin + img_width,
                height_margin: height_margin + img_height, :] = img
            next
    # save the result to disk
    save_img('filters_%s_%s_%d___num_step%d_stepsize%d.png' % (model_str,layer_name,number_of_filters_to_visualise,num_steps_ascent,step), stitched_filters)





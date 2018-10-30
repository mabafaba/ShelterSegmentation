from keras import backend as K 
from keras.layers import concatenate
import tensorflow as tf

# import numpy as np

# dice coefficient: value is between 0 and 1 
# (see: https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient)
# Closer to 0 means two distributions are very dissimilar, 1 the distributions are perfectly identical.
# returns ~0 for all wrong
# returns ~0 for prediction all 0
# returns 1 for all correct
# penalizes false positives

# Smooth : Keeps loss function continuous and differentiable for purpose of faster gradient descent calculation  / optimization.
#          It avoids having value of exactly 0, and it is in both the denom and num so max value is still 1.

smooth = 1.0
def dice_coef(y_true, y_pred):
    intersection = K.sum(y_true * y_pred)
    return (2. * intersection + smooth) / (K.sum(y_true) + K.sum(y_pred) + smooth)

# loss is to be minimized so we take the negative of the dice coefficient
def dice_coef_loss(y_true, y_pred):
    return -dice_coef(y_true, y_pred)
















# one hot dice loss

# NOT FUNCITONING CORRECTLY i think
def dice_coef_onehot(y_true,y_pred):
	# err_concat_test = concatenate([y_true, y_pred], axis=3)
	# print(err_concat_test)
	# print("losstensors:")
	# print('reversing')
	y_true_2 = 1. - y_true
	y_true_both = tf.concat([y_true,y_true_2],3)

	y_pred0 = y_pred[:,:,:,0]
	y_true0 = y_true_both[:,:,:,0]
	
	y_pred1 = y_pred[:,:,:,1]
	y_true1 = y_true_both[:,:,:,1]

	dice0 = dice_coef(y_true0,y_pred0)
	dice1 = dice_coef(y_true1,y_pred1)

	return(dice0+dice1)

def dice_coef_onehot_loss(y_true, y_pred):
    return -1*dice_coef_onehot(y_true, y_pred)


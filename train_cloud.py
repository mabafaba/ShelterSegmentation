# # Image Segmentation : Shelter Map Identification

import platform
print('Running on python version:',platform.python_version())
import os

from train import train 
from predict import predict
from preprocessing.data import create_train_data, create_test_data
from preprocessing.ew_data import create_ew_data
from resources.plot_results import plot_loss_epoch

#AWS path
data_path = '../shelterdata/180505_v1'

create_train_data(data_path)#,showSample=True,showNumSample=4)
create_test_data(data_path)
create_ew_data(data_path)

# ### Available models: 'unet','flatunet', 'unet64filters', or 'unet64batchnorm'

# #### Mod U-Net  3
# train(data_path,'unet64filters',number_of_epochs=30,batch_size=32,test_data_fraction=0.2,checkpoint_period=1,load_prev_weights=False,early_stop_patience=1)
# train(data_path,'unet64filters',number_of_epochs=80,batch_size=32,test_data_fraction=0.2,checkpoint_period=10,load_prev_weights=True,early_stop_patience=5)
# plot_loss_epoch(data_path+'/internal/checkpoints/','unet64filters')
# predict(data_path,'unet64filters')

#### Mod U-Net  3.5
modelname = "unet64filters_weighted"
train(data_path,modelname,
	number_of_epochs=100,
	batch_size=30,
	test_data_fraction=0.2,
	checkpoint_period=1,
	load_prev_weights=False,
	early_stop_patience=15)
plot_loss_epoch(data_path+'/internal/checkpoints/',modelname)
predict(data_path,modelname)


# # #### U-Net
# train(data_path,'unet',number_of_epochs=80,batch_size=32,test_data_fraction=0.2,checkpoint_period=10,load_prev_weights=True,early_stop_patience=5)
# plot_loss_epoch(data_path+'/internal/checkpoints/','unet')
# predict(data_path,'unet')

# # #### Mod U-Net  1
# train(data_path,'flatunet',number_of_epochs=80,batch_size=32,test_data_fraction=0.2,checkpoint_period=10,load_prev_weights=True,early_stop_patience=5)
# plot_loss_epoch(data_path+'/internal/checkpoints/','flatunet')
# predict(data_path,'flatunet')

# # #### Mod U-Net  4
# train(data_path,'unet64batchnorm',number_of_epochs=80,batch_size=32,test_data_fraction=0.2,checkpoint_period=10,load_prev_weights=True,early_stop_patience=5)
# plot_loss_epoch(data_path+'/internal/checkpoints/','unet64batchnorm')
# predict(data_path,'unet64batchnorm')

# modelname = "u64_onehot"
# train(data_path,modelname,
# 	number_of_epochs=30,
# 	batch_size=64,
# 	test_data_fraction=0.2,
# 	checkpoint_period=1,
# 	load_prev_weights=False,
# 	early_stop_patience=5)
# plot_loss_epoch(data_path+'/internal/checkpoints/',modelname)
# predict(data_path,modelname)

# # # #### no maxpooling
# modelname = "nomaxpool"
# train(data_path,modelname,
# 	number_of_epochs=25,
# 	batch_size=30,
# 	test_data_fraction=0.2,
# 	checkpoint_period=1,
# 	load_prev_weights=False,
# 	early_stop_patience=5)
# plot_loss_epoch(data_path+'/internal/checkpoints/',modelname)
# predict(data_path,modelname)

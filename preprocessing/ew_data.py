import os
import numpy as np

from skimage.io import imsave, imread
from skimage.transform import resize
import matplotlib.pyplot as plt

image_rows = 129
image_cols = 129



def create_ew_data(data_path):
    train_data_path = os.path.join(data_path, 'input/train')
    ew_data_path = os.path.join(data_path, 'input/errorweights/errorweights_kernel_3')
    images = [path for path in os.listdir(train_data_path) if not path.startswith('.')]
    images_ew = [path for path in os.listdir(ew_data_path) if not path.startswith('.')]
    sample_filename=[]
    ew_filename = []

    for i, sample_name in enumerate(images):
        if 'sample' in sample_name and 'bmp' in sample_name:
            print('sample found')
            ew_filename.append(sample_name.replace('sample','weight'))
            sample_filename.append(sample_name)
  
    total = len(sample_filename)

    print('Creating error weight masks...')
    print('Dataset size:', total)

    imgs_ew = np.ndarray((total, image_rows, image_cols), dtype=np.uint8)
    for i, image_name in enumerate(ew_filename):
        print(os.path.join(ew_data_path, image_name))
        img_ew = imread(os.path.join(ew_data_path, image_name.replace('sample','weight')), as_gray=True)
        img_ew = np.array([img_ew])

        imgs_ew[i] = img_ew

    # if showSample:
    #     print ('sample data:')
    #     plt.figure(figsize=(15,10))
    #     for i in range(1,showNumSample+1):
    #         plt.subplot(2,showNumSample,i)
    #         plt.imshow(imgs[i],cmap=('gray'))
    #         plt.subplot(2,showNumSample,i+showNumSample)
    #         plt.imshow(imgs_mask[i],cmap=('gray'))
    #     plt.show()

    print('Loading done.')

    if not os.path.exists(data_path+'/internal/npy'): os.makedirs(data_path+'/internal/npy')
    np.save(os.path.join(data_path, 'internal/npy/imgs_ew_train.npy'), imgs_ew)

    print('Saving to .npy files done.')

def load_ew_data(data_path):
    imgs_ew_train = np.load(os.path.join(data_path, 'internal/npy/imgs_ew_train.npy'))

    return imgs_ew_train




if __name__ == '__main__':
    create_ew_data(data_path)

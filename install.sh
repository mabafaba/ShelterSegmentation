# get git
sudo apt-get install git

# clone repo
git clone https://github.com/mabafaba/ShelterSegmentation.git
# install conda
wget -c https://repo.continuum.io/archive/Anaconda3-5.3.0-Linux-x86_64.sh
bash Anaconda3-5.3.0-Linux-x86_64.sh

# setup conda environment & install packages
conda create -n ml
conda install nb_conda
conda install ipykernel
conda activate ml
conda install keras
conda install scikit-image
conda install -c conda-forge matplotlib
conda install -c anaconda jupyter

# yay!
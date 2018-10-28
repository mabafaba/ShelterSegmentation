# install conda
## need bzip2 to get anaconda work
sudo apt-get install bzip2
wget -c https://repo.continuum.io/archive/Anaconda3-5.3.0-Linux-x86_64.sh
bash Anaconda3-5.3.0-Linux-x86_64.sh
# carefull read terms
# hit enter until through
# type 'yes' -> enter to accept
# wait..
# then:

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
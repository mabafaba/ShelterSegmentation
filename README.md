
# setting up conda environment:

# installing anaconda
 # replace this `Anaconda3-version.num-Linux-x86_64.sh` with your choice
wget -c https://repo.continuum.io/archive/Anaconda3-5.3.0-Linux-x86_64.sh
bash Anaconda3-5.3.0-Linux-x86_64.sh
rm Anaconda3-5.3.0-Linux-x86_64.sh
# setting up anaconda environment (once)


# start in environment:
conda activate ml
python train_cloud.py



# to add a model variation:
train.py: add model where "add model here"
predict.py: add model where "add model here"

add the model code 

# to run:
change the path in


# getting setup on AWS:
## follow: https://aws.amazon.com/de/blogs/machine-learning/get-started-with-deep-learning-using-the-aws-deep-learning-ami/
Deep Learning AMI (Ubuntu)


	ssh ubuntu@<Public DNS (IPv4)> -i ~/.ssh/AWS_AMI_key.pem

	source activate tensorflow_p36
	mkdir rizki
	cd rizki

	# switch to local, upload files:
	scp Archive.zip ubuntu@ec2-34-201-120-94.compute-1.amazonaws.com://home/ubuntu/rizki/

	unzip archive.zip
	# back to AWS:
	python ShelterMap_ImageSegmentation_cloudTraining.py 2>&1 | tee run_AWS_<date>.txt

	# tar folder and send to local:
	tar -zcvf tar-archive-name.tar.gz source-folder-name

	scp  ubuntu@ec2-34-201-120-94.compute-1.amazonaws.com://home/ubuntu/rizki/ <localTargetPath>


### p2.xlarge

## set up ssh key



# gcloud setup:
## create instance
dont be on 'free trial' by clicking upgrade account somewhere
'create instance'
select 2 CPU w >10GB storage
select 1 Tesla K80 GPU
if no GPU available try a different geo zone
fire upppp and you're good to go to....


## start instance & connect SSH
start instance on gcloud website

click on ssh -> show gcloud command
copy the command that looks something like: gcloud compute --project "PROJECTNAME" ssh --zone "us-east1-b" "INSTANCENAME"
run that in your console.
## install conda
sudo apt-get install bzip2
wget -c https://repo.continuum.io/archive/Anaconda3-5.3.0-Linux-x86_64.sh
bash Anaconda3-5.3.0-Linux-x86_64.sh 
source ~/.bashrc 

## setup conda environment and install relevant packages
### you'll have to copy paste and run these one by one:
conda create -n ml

conda install nb_conda
conda install ipykernel

conda activate ml

conda install keras
conda install scikit-image
conda install -c conda-forge matplotlib
conda install -c anaconda jupyter

## get code from github
### install git
sudo apt-get install git
### clone repo
git clone https://github.com/mabafaba/ShelterSegmentation.git

## Copy data to instance
run _locally_ (not in your ssh to gcloud):
gcloud compute scp /Volumes/2/shelterdata.zip m@instance-2:./shelterdata.zip
sudo apt-get install unzip
unzip shelterdata -d ./
## run the code
~OOOOOOOK 
SEEM LIKE c o m p l i c a t e d e r than i though a.k.a. WHY DO THEY DO THAT TO US a.k.a. isnt this supposed to be an abstraction:
https://stackoverflow.com/questions/43322886/how-to-train-keras-model-on-google-cloud-machine-learning-engine
ok or maybe i just needed to install cuda and cuDNN too:
https://medium.com/google-cloud/running-jupyter-notebooks-on-gpu-on-google-cloud-d44f57d22dbd
sooo.. to enable gpu let's try:


sudo apt-get install rpm
sudo apt-get install yum

curl -O http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_8.0.61-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1604_8.0.61-1_amd64.deb
sudo apt-get install dirmngr
sudo apt-get update
rm cuda-repo-ubuntu1604_8.0.61-1_amd64.deb
sudo apt-get install cuda -y
nvidia-smi~
## none of the above worked so instead:
select a deep learning optimised instance type! then
sudo /opt/deeplearning/install-driver.sh
(as in the echo upon connecting to instance)
for conda you need to use the local tensorflow binary in:
conda install --offline /opt/deeplearning/binaries/tensorflow/
(again as in the echo upon connecting to instance)
then follow instructions on conda setup above
check if using gpu:
from keras import backend as K
K.tensorflow_backend._get_available_gpus()
if no good use
cd ../../opt/deeplearning/binaries
ls # see available wheel files. try them until it works. then:
pip install ...blabla....whl
### fire up conda environment:
conda activate ml
### run code:
cd ShelterSegmentation
python train_cloud.py

IT FUCKIN WOOOOOORKS!!!!
recap:
- only listen to the "get a deep learning setup instance" instructions
- install cuda stuff as instructed
- install all the conda stuff as instructed, get the github repo etc all normal
- install tf from local binary wheel as instructed.
- knock yourself out with infinite computing power of destruction muhahaha


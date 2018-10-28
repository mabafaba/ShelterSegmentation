
# setting up conda environment:
```
# installing anaconda
 # replace this `Anaconda3-version.num-Linux-x86_64.sh` with your choice
wget -c https://repo.continuum.io/archive/Anaconda3-5.3.0-Linux-x86_64.sh
bash Anaconda3-5.3.0-Linux-x86_64.sh

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

## start instance & connect SSH
click on ssh -> show gcloud command
copy the command that looks something like: gcloud compute --project "PROJECTNAME" ssh --zone "us-east1-b" "INSTANCENAME"
run that in your console.
## install conda
sudo apt-get install bzip2
wget -c https://repo.continuum.io/archive/Anaconda3-5.3.0-Linux-x86_64.sh
bash Anaconda3-5.3.0-Linux-x86_64.sh

## setup conda environment and install relevant packages
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
gcloud compute scp /Volumes/2/shelterdata.zip m@cpuonly:./shelterdata

## run the code

### fire up conda environment:
conda activate ml
### run code:
cd ShelterSegmentation
python train_cloud.py




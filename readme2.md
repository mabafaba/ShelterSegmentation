

# setting up conda environment:
```
# installing anaconda
 # replace this `Anaconda3-version.num-Linux-x86_64.sh` with your choice
wget -c https://repo.continuum.io/archive/Anaconda3-5.3.0-Linux-x86_64.sh
bash Anaconda3-5.3.0-Linux-x86_64.sh

# setting up anaconda environment (once)
conda create -n ml

conda install nb_conda
conda install ipykernel

conda activate ml

conda install keras
conda install scikit-image
conda install -c conda-forge matplotlib
conda install -c anaconda jupyter

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



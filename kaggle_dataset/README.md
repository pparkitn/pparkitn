Create a New Dataset Here are the steps you can follow to create a new dataset on Kaggle: Create a folder containing the files you want to upload Run

pip3 install kaggle

kaggle datasets init -p /path/to/dataset to generate a metadata file | no folders just add folders as zipped files
Add your dataset’s metadata to the generated file, datapackage.json Run

kaggle datasets create -p /path/to/dataset to create the dataset
Create a New Dataset
Here are the steps you can follow to create a new dataset on Kaggle:

Create a folder containing the files you want to upload

Run kaggle datasets init -p /path/to/dataset to generate a metadata file

Add your dataset’s metadata to the generated file, datapackage.json

Run kaggle datasets create -p /path/to/dataset to create the dataset

Your dataset will be private by default. You can also add a -u flag to make it public when you create it, or navigate to “Settings” > “Sharing” from your dataset’s page to make it public or share with collaborators.

Create a New Dataset Version
If you’d like to upload a new version of an existing dataset, follow these steps:

Run kaggle datasets init -p /path/to/dataset to generate a metadata file (if you don’t already have one)

Make sure the id field in dataset-metadata.json (or datapackage.json) points to your dataset

Run kaggle datasets version -p /path/to/dataset -m "Your message here"

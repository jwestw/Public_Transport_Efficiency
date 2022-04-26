# Public Transport Efficiency Project

This project is currently being carried out by the Data Science Skills Team (DSST) within ONS.

Members involved are [James Westwood](https://github.com/jwestw), [Chloe Murrell](https://github.com/chloemurrell) and [Antonio Felton](https://github.com/Antonio-John).

## Overview
A project to measure the efficiency of public transport systems in the UK. 

By collecting data for thousands of different journeys across multiple cities, the journey time can be compared for public vs private transport  to assess which is considered more 'efficient'.

For clarity, for the purpose of this project efficiency is defined in terms of time efficiency which means to travel to the desired destination while minimising the time and effort required. 

## Aims of the project 

### The concept 
When deciding how to travel into or around a city most people would make the rational decision to choose the mode of transport which will get them to their desired destination the quickest. In London this is public transport however, for many other cities around the UK this is not the case and public transport is in fact much slower. But how much slower and how do different cities compare to London or each other?

This project aims to go beyond current studies by providing comprehensive analysis of public vs private transport clearly demonstrating the efficiency of public transport systems in the UK. Through quantifying journey times within cities throughout the UK and producing a single numerical metric, regional and geographical comparison can be made. 

### Objectives 
The aims of the project are:
- To build a data pipeline that can analyse data to assess the efficiency of public transport systems in the UK. 
- To make the code reusable so that it can be used across numerous cities and the project can be expanded to also consider international cities.
- Conclude with analysis which has the capability of providing insights into the time efficiency of public and private transport and benchmark cities against each other. 

## Process
1.	Take a sample of journeys for a particular city
2.	Calculate journey time metrics for both public and private transport
3.	Calculate a ratio between public and private transport journey times 
4.	Calculate an overall metric for the entire city
5.	Compare the results for each city

### Using VS code

#### Create new branch 

Initially created a branch on GitHub from the develop branch. 
Within the terminal:
```python 
git fetch -p
``` 
This will update your local branches in line with remote branches
Within VS code you can switch branches using the button in the bottom left corner. 
Within the terminal you can switch branches using:
```python
git checkout branch_name
```

#### Moving changes from one branch to another
It is important to ensure that you are in the correct branch before making changes however, you can move changes if needed. 
The changes need to be added but not yet committed.
To add the changes:
```python
git add file_name
```
If you have already committed the changes you'll need to remove the last commit from the current branch:
```python
git reset --soft HEAD^
```
The changes can then be moved using the following code:
```python
git stash 
git checkout correct_branch
git stash pop 
```
The changes can then be added, committed and pushed to the correct branch. 

### Virtual environment 
It is recommended that a virtual environment is used to avoid dependency issues. A virtual environment can be created by following the instructions below and the environment yaml can be used to install the required versions of packages. 

#### Install Miniconda
Conda is the recommended for environment management. Both miniconda and and the full Anaconda can be used however, the following instructions is based on using miniconda. 
Download miniconda from this link (https://docs.conda.io/en/latest/miniconda.html). Select the correct installer for your OS and follow the instructions.
For Mac, go to terminal and run bash download_file_path (drag and drop the downloaded file into the terminal). 
Follow the instructions within the terminal and it should download correctly. 

#### Create environment
Use Python version 3.10
Within the command line:
```python
conda create -n transp_eff_310 python=3.10
```
transp_eff_310 was chosen for consistency across developers.

#### Activate environment
Having created the environment, the command line will give you instructions. 
This includes how to activate and deactivate the environment:
```python 
conda activate transp_eff_310
```

#### Install dependencies
To install the dependencies you must be within the project directory. If not this can be done by running the following within the terminal:
```python
$ cd C:\Users\name\project-directory
```
To install the requirements:
```python
conda install --file environment.yml
```
This may throw an error if you do not have all the packages required
```python
PackageNotFoundError: The following packages are not available from current channels
```
If this does, write the following with the package names that the error has shown you are missing:
```python
pip install packagename
```
The script should now be set up to use.

#### Update the environment yaml 
The environment yaml needs to be updated whenever a new package or library is installed. 
To do so:
```python
conda env export > environment.yml
```

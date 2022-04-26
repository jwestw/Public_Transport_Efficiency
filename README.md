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
```
git fetch -p
``` 
This will update your local branches in line with remote branches
Within VS code you can switch branches using the button in the bottom left corner. 
Within the terminal you can switch branches using:
```
git checkout branch_name
```

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
```
conda create -n transp_eff_310 python=3.10
```
You can choose any name for your environment, but we suggest using ```transp_eff_310``` so it is consistent with the other developers on this project.

#### Activate environment
Having created the environment, the command line will give you instructions. 
This includes how to activate and deactivate the environment:
```
conda activate transp_eff_310
```
Or for windows:
``` 
activate transp_eff_310
```

#### Install dependencies
To install the dependencies the virtual environment must be activated.

To install the requirements:
```
conda install --file environment.yml
```
The script should now be set up to use.

#### Update the environment yaml 
If you have installed a new package as part of your development work, then the environment yaml needs to be updated, so the environment can be shared with the wider team.
To do so:
```
conda env export > environment.yml
```
You will need to add/commit/push the changes to the environment yaml so they get pushed up to the repository and others can run your code. 

If the installation of additional libraries are needed to run your code, you may want to note this in the notes or comments of the Pull Request.

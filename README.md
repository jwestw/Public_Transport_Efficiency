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

## For Developers

The transport efficiency project is an open source project that you can contribute to. We are looking for developers and those with domain knowledge (about transport, statistics, analysis etc) to contribute to the code and help us with our project. 

To get developers set up, we have created this guide to make setting up your working environment easier. 

### Using VS Code 

We strongly suggest using VS Code for programming. It is a great tool, and since that is what we are using, if you run into problems we are more likely to be able to help. 

#### Downloading VS Code

You can download VS code from internet [VS code download link](https://code.visualstudio.com/download). Select the correct installer for your OS and follow the instructions. 

#### Ensure Python is installed on system
This project is coded in Python primarily (though we might add other languages later). If you are unsure if you have Python installed, you can find out within the terminal using the following code. 

```python 
python --version
```

It will return the version of Python if installed. 

If you do not already have Python installed, you can use the following link [Python download](https://www.python.org/downloads/). We recommend that you use a virtual environment before you start making any changes (see below).

#### Extensions
Download the Python extension in the extensions button in the side bar. 

https://user-images.githubusercontent.com/97117990/166445317-21990e28-07a0-4435-be98-8ed8d33d6328.mov

#### Connect your environment
Using a virtual envionment is covered in the section "Virtual environments" in this readme.

To get VS Code to work with your virtual environment, select the Python interpreter by clicking on the status bar.

Configure the debugger – click on run and debug in the side bar

https://user-images.githubusercontent.com/97117990/164271440-13e40244-d4cb-4f38-9cb7-7a95a7932a75.mov

#### Linking to GitHub 
Download the Github Pull requests and issues extension

https://user-images.githubusercontent.com/97117990/164272228-3cbd3204-cf4d-4f7d-9e53-6bcc182e4401.mov

#### Opening the project in VS code 
If the project has already been cloned, then you can simply click open file and navigate to this folder to open.
If the repository has not already been cloned this can be done by the following steps.
a.	First you must have set up a SSH key in GitHub. Follow these instructions if not already complete [SSH key in GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh). 
b.	From the GitHub project page press the green code button, click SSH and then copy the link. 
Then follow either option 1 or 2:

Option 1: 
- Open the terminal and navigate to the directory where you would like the cloned respository to be located. 
Example: 
```python 
cd Programming
``` 
Then run 
```python 
git clone "git@github.com:jwestw/Public_Transport_Efficiency.git"
```
Option 2: direct from VS code 
- Within VS code click clone git respository and then paste link into search bar. 

https://user-images.githubusercontent.com/97117990/164274806-42f04a32-30db-45e7-a62b-68a3d26b8f6a.mov

The repository should now be cloned to your local computer and can be accessed in VS code via this repository. When you open VS code, click open and navigate to the directory you previously selected.   

### Version control

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
### Setting up pre-commits
To set up pre-commits, go to [pre-commits.com](https://pre-commit.com/#installation) and follow the installation instructions. This includes instructions on installing pre-commits, setting up a pre-commit-config.yml and running pre-commits against all the files.

For this project, flake8 will also be used as a tool for style guide enforcement of PEP8. To set up flake8, go to [flake8 documentation](https://flake8.pycqa.org/en/latest/#installation) and follow the instructions to install it. Then go to [configuring flake8](https://flake8.pycqa.org/en/latest/user/configuration.html) to configure it to carry out the exact checks you require. 

### Virtual environments 
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

### Using TravelTime API
If you do not already have a TravelTime API account you will need to set one up [TravelTime API website](https://account.traveltime.com)

Once you have an account you should be able to view your application ID and Key. These are unique to your account and monitor your usage of the API. As these should be kept private and not pushed to GitHub we have set up a .env file to store the details and call them into the relevant Python script. 

Currently in the repository there is a .env.example file. You will need to create a new file called .env and copy the contents of the example file into the new one. You can then input your API ID and API Key in the respective locations. Any changes to this file will not occur in the changes log as the .env file has been added to gitignore. 

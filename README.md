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

### Setting up VS Code 

#### Downloading VS Code

You can download VS code from internet [VS code download link](https://code.visualstudio.com/download)

#### Ensure Python is installed on system
If you are unsure if you have python installed, you can find out within the terminal using the following code. 
```python 
Python --version
```
It will return the version of python if installed. 
If you do not already have python installed, you can use the following link [Python download](https://www.python.org/downloads/)

#### Extensions
Download the Python extension in the extensions button in the side bar. 

![How to download Python extension video](https://user-images.githubusercontent.com/97117990/164270232-fdb693fa-e2fc-419a-b1dd-1514c9f438ad.mov)

#### Set up your environment
Select Python interpreter by clicking on the status bar
Configure the debugger – click on run and debug in the side bar

![Setting up the environment](https://user-images.githubusercontent.com/97117990/164271440-13e40244-d4cb-4f38-9cb7-7a95a7932a75.mov)

#### Linking to GitHub 
Download the Github Pull requests and issues extension

![Linking to GitHub](https://user-images.githubusercontent.com/97117990/164272228-3cbd3204-cf4d-4f7d-9e53-6bcc182e4401.mov)

#### Opening the project in VS code 
If the project has already been cloned, then you can simply click open file and navigate to this folder to open.
If the repository has not already been cloned this can be done by the following steps.
a.	First you must have set up a SSH key in GitHub. Follow these instructions if not already complete [SSH key in GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh). 
b.	From the GitHub project page press the green code button, click SSH and then copy the link. 
Then follow either option 1 or 2:

Option 1: 
- Open the terminal and navigate to the directory where you would like the cloned respository to be located. 
Example: 
```Python 
cd Programming
``` 
Then run 
```Python 
git clone "copied link from GitHub"
```
Option 2: direct from VS code 
- Within VS code click clone git respository and then paste link into search bar. 

![Cloning the GitHub repository](https://user-images.githubusercontent.com/97117990/164274806-42f04a32-30db-45e7-a62b-68a3d26b8f6a.mov)

The repository should now be cloned to your local computer and can be accessed in VS code via this repository. When you open VS code, click open and navigate to the directory you previously selected.   

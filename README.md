# Public Transport Efficiency Project

This project is currently being carried out by the Data Science Skills Team (DSST) within ONS.

Members involved are [James Westwood](https://github.com/jwestw), [Chloe Murrell](https://github.com/chloemurrell) and [Antonio Felton](https://github.com/Antonio-John).

## Description
A project to measure the efficiency of public transport systems in the UK. 

By collecting data for thousands of different journeys across multiple cities, numerous parameters, such as journey time and cost, can be compared for public vs private transport  to assess which is considered more 'efficient'.

For clarity, for the purpose of this project efficiency is defined in terms of time efficiency which means to travel to the desired destination while minimising the time and effort required. 

## Aims of the project 
The aims of the project are:
- To build a data pipeline that can analyse data to assess the efficiency of public transport systems in the UK. 
- To make the code reusable so that it can be used across numerous cities and the project can be expanded to also consider international cities.
- Conclude with analysis which has the capability of providing insights into the time efficiency of public and private transport and benchmark cities against each other. 

## Process
1. Take a sample of journeys for a particular city
2. Calculate journey metrics for both public and private transport 
   - Journey time 
   - Cost 
3. Calculate a ratio between public and private transport for the above metrics
4. Calculate an overall metric for the entire city
5. Compare the results for each city 

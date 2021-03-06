## TECH CITY REAL ESTATE
Github Repository: https://github.com/annapettigrew/team-05-project-03 <br />  

### Collaborators

- Anna Pettigrew: 
    - github username: annapettigrew
- Tyler Hill: 
    - github username: tylerhill122
- Prak Bagavatula 
    - github username: Prakb2401
- Phil Faulkner: 
    - github username: phfaulkner


## Description

For this analysis, we utilized an api to gather the real estate data from https://rapidapi.com/apidojo/api/unofficial-redfin/

We chose to examine real estate data from the popular site redfin. Our initial interest was to particularly examine real estate prices in large tech cities to compare with the nation's average.

Information included on the final includes:
- A graph of price by time on market
- A leaflet map with pins showing location of the homes
- A map of time on the market represented by blue circles
- A map of prices represented by red circles
- A list of facts about the chosen city which includes:
    - Median Price compared with the National Average
    - Mean Price
    - Mean Beds 
    - Mean Baths
    - Mean sqft

## Tools Used
- Python / Pandas
- Flask
- MongoDB
- D3.js
- Chart.js
- Plotly.js
- HTML/CSS


## Coding Approach

We created a Python/Flask-powered API to pull our queries from the Unofficial Redfin API and insert the results into a MongoDB database. From there, we created our interactive dashboard to visually explore the results.

To narrow our results, we decided to focus on top tech cities in the U.S. (will expand to 10). The following cities saw massive growth in their real estate markets in the preceding years:
- Chicago, IL
- San Francisco, CA
- Austin, TX
- Tampa, FL
- Atlanta, GA


## Observations

- Chicago was surprisingly lower than the National Average home price.
- San Francisco’s median home price, unsurprisingly, was 3x the national average, while having a price per sqft nearly 4x higher than national average, owing to its unique geographic location


## Dashboard

<img width="868" alt="Screen Shot 2022-07-13 at 9 41 08 PM" src="https://user-images.githubusercontent.com/97136642/178868945-18e1542b-f490-4ca4-9a24-6c2ffb8fa4f3.png">



<img width="868" alt="Screen Shot 2022-07-13 at 9 41 40 PM" src="https://user-images.githubusercontent.com/97136642/178869007-ed3b307f-6bf6-4765-9fce-3e62692bf19a.png">

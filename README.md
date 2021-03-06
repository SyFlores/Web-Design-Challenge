# Web-Design-Challenge
Latitude Analysis Dashboard with Attitude

*Collaborators: Sy Flores*

---
## **Table of Contents**
- [Abstract](#abstract)
- [Repository](#repository)

---

## Abstract
We are intending to create a website with multiple pages to display the relationship between the latitude of cities and factors such as max temperature, cloudiness, humidity, and wind speed.

## Repository
This section serves as a means to navigate the project/repository.
**WebVisualizations** will serve to house all of the contents of the project excluding the README.md

- **WebVisualizations**
  - **assets**
    - **Style**
      - comparison.css
        - This file contains unique styling for the Comparison visualization page
      - data.css
        - This file contains unique styling for the Comparison visualization page
      - global.css
        - This will serve to be the primary stylization **css** file
    - cities.csv
      - This file contains the data from the Weather API assignment
    - table-create.py
      - This file takes the cities.csv file and transforms it into the tablecities.html format for use in the website
    - tablecities.html
      - This holds the cities.csv data in an html format, generated by the table-create.py file
  - **site_pages**
    - **visualizations**
      - This folder contains the individual analysis for each comparison
      - cloudiness.html
      - humidity.html
      - max_temperature.html
      - wind_speed.html
    - comparison.html
      - This page contains all 4 comparisons in one place
    - data.html
      - This page contains an interactive version of all the data used for the visualizations
  - **visualizations**
  - Plots as **png** files
    - This includes the comparison of latitude against max temperature, cloudiness, humidity, and wind speed
    - Additionally, these latitude values are broken up again by northern and southern hemispheres and compared again with an attempted linear regression
- index.html
  - This is both the home page and landing page for the website
  - This page includes an introduction on the contents of the website
- README.md
  - The primary use of this file is to explain how to navigate the project and repository

---
# IPL Data Analytics and Interactive Dashboard Using Python

## 1. Project Overview

This project analyses Indian Premier League (IPL) cricket data using Python.
It explores team performance, player statistics, match results, toss decisions,
venues, and season-wise trends.

An interactive dashboard has been developed using Dash and Plotly to present
the analysis through charts, summary cards, and filters.

## 2. Project Objectives

- Analyse IPL match and ball-by-ball data.
- Identify teams with the highest number of wins.
- Find top run-scoring batsmen and wicket-taking bowlers.
- Analyse toss decisions and match outcomes.
- Explore season-wise and venue-wise match statistics.
- Create an interactive dashboard for data exploration.

## 3. Dataset Description

This project uses two datasets:

### matches.csv
Contains match-level information, including:
- Season and date
- Teams and match winner
- Venue and city
- Toss winner and toss decision
- Match result and player of the match

### deliveries.zip
Contains ball-by-ball information, including:
- Batting and bowling teams
- Batsman and bowler
- Runs scored
- Extra runs
- Wickets and dismissal types

The datasets are used together to analyse team and player performance.

## 4. Tools and Technologies

- Python
- Pandas
- Plotly
- Dash
- Jupyter Notebook / Google Colab
- GitHub
- Render

## 5. Data Cleaning and Preparation

The analysis includes:
- Checking missing values.
- Checking duplicate records.
- Handling missing values in selected text columns.
- Converting the date column into datetime format.
- Preparing the data for analysis and visualisation.

Some missing numerical values are retained where appropriate.

## 6. Exploratory Data Analysis

The project analyses:
- Team-wise match wins
- Top batsmen by total runs
- Top bowlers by wickets
- Matches played in each season
- Toss decisions and match outcomes
- Venue-wise match counts
- Dismissal types
- First-innings score distribution

## 7. Visualisations

The analysis includes the following chart types:

- Bar Chart
- Line Chart
- Heatmap
- Scatter Plot
- Box Plot

Interactive charts are also available in the dashboard.

## 8. Key Findings

Based on the current dataset and analysis:

- Mumbai Indians have the highest recorded team win count, with 144 wins.
- Virat Kohli has the highest recorded run total, with 8,014 runs.
- Yuzvendra Chahal has the highest wicket count in this analysis, with 205 wickets.
- Eden Gardens has the highest recorded venue count in the venue analysis, with 77 matches.
- Among matches with recorded winners, the toss winner also won approximately 50.83% of matches.
- Teams chose to field first approximately 64.29% of the time.
- The 2013 season has the highest match count in this analysis, with 76 matches.

These findings reflect the dataset used in this project.

## 9. Interactive Dashboard Features

The dashboard includes:

- Summary KPI cards
- Team performance charts
- Top batsmen analysis
- Season-wise match analysis
- Interactive season and team filters
- Interactive Plotly visualisations

## 10. Live Dashboard

Access the deployed dashboard here:

https://ipl-data-analytics-dashboard.onrender.com

## 11. Project Repository

GitHub Repository:

https://github.com/satyaranjansahoo916-gif/IPL-Data-Analytics-Dashboard

## 12. How to Run the Project Locally

1. Clone or download this repository.
2. Install the required libraries:

   pip install -r requirements.txt

3. Run the dashboard:

   python app.py

4. Open the local address shown in the terminal.

## 13. Conclusion

This project demonstrates how Python can be used for data cleaning,
exploratory data analysis, visualisation, and interactive dashboard development.

It provides an accessible way to explore IPL match and player statistics.

## 14. Future Improvements

- Add more player comparison features.
- Improve data filtering and analysis.
- Add more advanced statistical analysis.
- Include additional visualisations and insights.

## Author

Satya Ranjan Sahoo

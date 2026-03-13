AirFly Insights: Data Visualization and Analysis of Airline Operations
✈️ Flight Delay Analysis

**Overview**

This project analyzes flight delay patterns using exploratory data analysis and visualization techniques.
The goal is to understand how delays vary across airlines, routes, airports, and time periods.

The project includes data cleaning, exploratory data analysis (EDA), route and seasonal insights, and an interactive dashboard built with Streamlit.

---

**Dataset**

The dataset contains information about flight schedules, delays, airlines, airports, and routes.

Key columns include:
1. airline name
2. origin airport
3. destination airport
4. departure delay
5. arrival delay
6. flight distance
7. date and time information
   
---

**Project Milestones**

Week 1: Data Preparation
1. Loaded and explored the dataset
2. Checked missing values
3. Optimized categorical columns
4. Created new features such as:
   route
   day of week
   month name
   delay indicators
   cancellation flags
5. Saved cleaned dataset for further analysis

Week 2: Exploratory Data Analysis
1. Top airlines by flight volume
2. Most common routes
3. Flights by month and day
4. Distribution of arrival delays
5. Average delays by airline and airport
6. Delay patterns across hours of the day

Week 3: Route and Seasonal Analysis
1. Top origin–destination routes
2. Routes with highest average delays
3. Airport level delay analysis
4. Heatmap of delays between airports
5. Monthly delay trends
6. Weekend vs weekday delay comparison
7. Cancellation trends by month

---

**Dashboard**

An interactive Streamlit dashboard was created to visualize flight delay patterns.

Features of the dashboard:
1. Airline analysis
2. Delay analysis
3. Temporal delay trends
4. Route insights
5. Interactive filters

**Run the dashboard with:**
`streamlit run app.py`

---

**Tools and Technologies**
1. Python
2. Pandas
3. NumPy
4. Matplotlib
5. Seaborn
6. Streamlit
7. Git & GitHub
   
---

**Conclusion**

This project demonstrates how data analysis and visualization can be used to understand flight delay patterns and operational trends in airline data.
The interactive dashboard allows users to explore these insights in an easy and visual way.

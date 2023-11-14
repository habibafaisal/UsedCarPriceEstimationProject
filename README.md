# UsedCarPriceEstimationProject

**Project Overview: Building a Suzuki Car Recommendation System**

**Introduction:**
The aim of this data mining project is to develop a robust recommendation system for Suzuki cars, providing car owners with accurate estimates of their vehicles' values for selling purposes. The system focuses on assisting users in making informed decisions when selling their used Suzuki cars, considering various factors that influence the car's market value.

**Technical Aspects:**

1. **Environment Setup:**
   - **Install Python:** Ensure that Python is installed on your computer. If not, download it from [Python's official website](https://www.python.org/downloads/), selecting the appropriate version for your operating system.

   - **Install Required Libraries:** The project utilizes key libraries. Install them using pip:
     pip install requests
     pip install bs4
     pip install pandas

2. **Data Collection and Scraper:**
   - **Download Project Files:** Download the Python files (`Finalmain.py` and `FinalFinalCleaning.py`) to your local machine.

   - **Run the Scraper:** Execute the scraping file (`Finalmain.py`) using the command:
     python Finalmain.py
     This initiates data scraping from the website, saving the results to a CSV file named "finalData.csv."

3. **Data Cleaning:**
   - **Run Cleaning Script:** Execute the cleaning file (`FinalFinalCleaning.py`) to clean the data.
     python FinalFinalCleaning.py
     The cleaned data is saved to a new CSV file named "CleanedFinalData.csv."

4. **Analysis with IBM SPSS Modeler:**
   - **Data Analysis Tool:** Utilize IBM SPSS Modeler for in-depth data analysis. Ensure that IBM SPSS Modeler is installed on your computer.

   - **Open Project File:** Launch IBM SPSS Modeler and open the project file to run the analysis.

5. **Problem Statement and System Development:**
   - **Objective:** The project addresses the need for a recommendation system to estimate the value of Suzuki cars for selling purposes.

   - **Data Mining Techniques:**
     - **Regression Analysis:** Identify relationships between car features and market value.
     - **Clustering:** Group similar Suzuki cars to compare their relative values.
     - **Association Rule Mining:** Discover patterns and associations influencing the car's value.

   - **Considerations:** The system accommodates various Suzuki car models, their variations, and current market demand, ensuring accurate estimates.

6. **Recommendation System:**
   - **Fair Selling Price:** The system suggests a fair selling price based on a thorough analysis of the car's data, considering features and market demand.

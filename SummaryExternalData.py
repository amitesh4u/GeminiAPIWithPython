from config.GeminiModel import model

query = "summarize this article  https://en.wikipedia.org/wiki/Data_science"
prompt_parts = [
  query
]

print("Me: " + query + "\n")

response = model.generate_content(prompt_parts)
print(response.text)


# Me: summarize this article  https://en.wikipedia.org/wiki/Data_science
#
# **Data Science**
#
# Data science is an interdisciplinary field that combines scientific
# methods, processes, algorithms, and systems to extract knowledge and
# insights from data in various forms, both structured and unstructured. It
# involves collecting, cleaning, analyzing, modeling, and interpreting data
# to solve real-world problems.
#
# **Key Processes:**
#
# * **Data Collection:** Gathering data from various sources, including
# sensors, databases, and experiments. * **Data Cleaning:** Removing noise,
# inconsistencies, and errors from the data. * **Exploratory Data Analysis (
# EDA):** Summarizing and visualizing data to gain initial insights. * **Data
# Modeling:** Building statistical and machine learning models to predict
# outcomes or understand relationships. * **Data Interpretation:** Drawing
# meaningful conclusions from the analysis and models.
#
# **Applications:**
#
# Data science is widely applied in various industries, including:
#
# * **Business:** Forecasting demand, optimizing marketing campaigns,
# and improving customer experience. * **Healthcare:** Diagnosing diseases,
# predicting patient outcomes, and developing personalized treatments. *
# **Finance:** Managing risk, detecting fraud, and predicting financial
# trends. * **Manufacturing:** Optimizing production processes, improving
# quality control, and predicting maintenance needs.
#
# **Skills and Tools:**
#
# Data scientists require proficiency in programming languages (e.g., Python,
# R), statistical tools, machine learning techniques, and data visualization
# tools.
#
# **Importance:**
#
# Data science has become increasingly important as the volume and complexity
# of data continue to grow. It enables organizations to make data-driven
# decisions, improve efficiency, and gain a competitive advantage.

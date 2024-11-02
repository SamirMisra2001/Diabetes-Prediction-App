# Diabetes-Prediction-App
**Overview** </br>
</br>
A machine learning-based application that predicts the likelihood of diabetes in individuals based on health and demographic information. This tool can assist healthcare professionals in making data-driven decisions and provide patients with early warnings regarding potential diabetes risk.

</br>

**Prerequisites** </br>
- Python 
- Streamlit
- pandas
- NumPy
- matplotlib
- scikit-learn
- pickle
</br>

**Features** </br>
- User-Friendly Interface: Streamlit-powered interface for smooth user interaction.
- Real-Time Predictions: Instant diabetes risk predictions based on input data.
- Visual Analysis: Data visualization features for exploratory data analysis.
- Customizable Input: Flexible data input fields for health metrics (e.g., glucose level, BMI, age).
- Optimized Model: Uses GridSearchCV for optimal hyperparameter tuning.
</br>

<h4> Usage  </h4>
<ul>
  <li> Launch the app by running app.py with Streamlit. </li>
  <li>Fill in the required health information fields, such as:</li>
  <ul>
    <li> Age </li>
    <li> BMI </li>
    <li> Blood Pressure </li>
    <li> Glucose Level </li>
  </ul>
  <li>Click <strong>Predict</strong> to get the diabetes prediction result.</li>
</ul>

</br>

<h4> Model </h4>
<p>The app uses a machine learning model based on the <strong>Random Forest Classifier</strong> for diabetes prediction. The model was trained on a diabetes dataset and optimized using <strong>GridSearchCV</strong> to find the best hyperparameters, ensuring higher prediction accuracy. Features considered include blood glucose levels, BMI, age, blood pressure, and other health indicators.</p>

# Project Name : Deploy Machine Learning Pipeline with Flask

**Project Description:**

The "Bank Churn Prediction" project aims to provide a web-based platform for predicting the likelihood of a customer leaving a bank (churn prediction) based on various features such as credit score, geography, gender, age, tenure, balance, number of products, presence of a credit card, activity status, and estimated salary. The project utilizes a machine learning model trained on historical banking data to make these predictions.


**Technologies Used:**
* Python Flask: Flask is a lightweight web application framework for Python. It provides tools, libraries, and technologies to build web applications quickly and easily. In this project, Flask is used to create the backend server that handles HTTP requests from the client, processes the data, and returns the prediction results.
* HTML/CSS: HTML (Hypertext Markup Language) is used for structuring the web page, while CSS (Cascading Style Sheets) is used for styling and designing the user interface. Together, they define the layout, appearance, and behavior of the web applications.
* Machine Learning Model: A machine learning model, trained on historical banking data, is used to predict the likelihood of customer churn based on input features provided by the user through the web interface. The model is integrated into the Flask application to make real-time predictions.

**Project Workflow:**
* User Interface: The user interacts with the web application through a user-friendly interface provided by HTML forms. The user inputs various details such as surname, credit score, geography, gender, age, tenure, balance, number of products, presence of a credit card, activity status, and estimated salary.
* Backend Processing: When the user submits the form, the data is sent to the Flask backend server using HTTP POST requests. Flask receives the data, preprocesses it, and passes it to the machine learning model.
* Prediction: The machine learning model predicts the likelihood of customer churn based on the input data. The predicted result is then returned to the Flask server.
* Display Result: Flask sends the prediction result back to the user interface, where it is displayed to the user in a user-friendly formats.

**Flask:**

Flask is a micro web framework written in python. It is lightweight and easy to use, making it ideal for developing web applications and APIs. Flask provides features such as routing, request handling, template rendering, and session management, allowing developers to build powerful web applications with minimal boilerplate code. In this project, Flask is used to create the backend server that handles HTTP requests from the client, processes the data, and returns the prediction results. Flask also facilitates the integration of the machine learning model into the web application, enabling real-time predictions based on user input.

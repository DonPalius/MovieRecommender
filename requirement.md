# MovieRecommender

# API KEY
- Go https://www.themoviedb.org/ and create an API key. Then you can paste it in the react js application.
- In the react js application, you need to create a .env file which contains the line : "REACT_APP_API_KEY=[your themoviedb api key]"; put this .env file in the folder my-app.

# Python Requirements
- django
- djangorestframework
- pandas
- requests
- pillow
- django-environ
- astropy
- pybase64
- django-cors-headers
- nltk
- transformers
- scikit-learn (write: pip3 install -U scikit-learn)

To install the Python requirements, run the following command:
pip3 install "library"

# browser requirment

https://addons.mozilla.org/en-US/firefox/addon/access-control-allow-origin/

## data
datasets required in the folder data of django blog application: 
- movies.dat from MovieLens1M dataset
- ratings.dat from MovieLens1M dataset
- users.dat from MovieLens1M dataset
- movies_metadata.csv from The Movies Dataset in Kaggle
- credits.csv from from The Movies Dataset in Kaggle
- plots.csv which is already here. We generated it manually thanks to the file overview_creator.py


# React App Requirements
To run the React app, you need to have Node.js and npm (Node Package Manager) installed on your system.

## Install Dependencies
1. Navigate to the directory where your React app is located.

2. Open a terminal or command prompt in that directory.

3. Run the following command to install the app's dependencies: npm i 

4. then run the following command : npm start (after having run the command "python3 manage.py runserver" in the folder django_blog which contains manage.py)

5. This will start the development server and launch the React app in your default web browser.

The app will automatically reload if you make any changes to the source code.

You can access the app by opening the provided local URL in your web browser.

Typically, it will be something like: `http://localhost:3000/`

Note: The actual port number may vary depending on your configuration.

Make sure you have Node.js and npm installed on your system before running the above commands.


# WORKOUT TRACKER

---
Workout Tracker is an application which helps you to track your workouts by recording them in a google sheet.

## pre-requisites
* [Nutritionix](https://www.nutritionix.com/business/api) API account  
* Go to this [link](https://docs.google.com/spreadsheets/d/1ElDd-jK5g6lIFY9nn_qb4i-6BtiLKjqPhpafQSNWTrs/edit?usp=sharing) and create a copy of the My Workouts Spreadsheet. You may need to login/register. 
* Log into [Sheety API](https://sheety.co/) with your google account
  * Create a new project named 'Workout Tracking'
  * Fill the url of your google sheet and save it
  * In your project/authentication select 'Bearer (Token)' and enter the bearer token of your choice.

## Technologies
* Python 3.9
* Sheety API
* Nutritionix API

## Installation
* Clone the project : `git clone https://github.com/dardevetdidier/workout-tracker.git`
* Create an activate virtual environment\
`$ python -m venv venv`\
`$ source venv/Script/activate`
* Install dependencies\
`$ pip install -r requirements.txt`
* Add environment variables
  * Add `.env` file at the root of the project
  * Add into this file:
    * APP_ID=Your Nutritionix x-app-id
    * API_KEY=Your Nutritionix x-app-key
    * SHEET_ENDPOINT=your url google sheet
    * TOKEN=YOURsecretBearerToken

## Run Application

`$ python main.py`

`Tell me which exercices you did: I ran for 30 minutes`

Note that Nutritionix API use natural language.\
After execution, take a look at your Workout Google sheet !


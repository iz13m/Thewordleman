# Thewordleman
A bot that solves wordle puzzle


<!-- ABOUT THE PROJECT -->
## About The Project

This is came onto my mind when I saw how trending this game has become lately. It’s powered by code written in Python on a Google Cloud Virtual Machine instance that uses Selenium library to automate the script on google chrome browser and regex to randomly choose 5-letter words based on the results from the previous guess 

I also signed up for a new twitter account (@thewordleman), so that every morning the VM will run the script trying to solve day’s puzzle then tweet the results through twitter API ensuring this whole process is fully automated



### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* Python
* Selenium
* Twitter API
* Regex
* Pandas
* English Words library
* pyperclip


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* pip
  ```sh
  pip install -r requirements.txt
  ```

### Twitter API


1. Sign up for Twitter developer account at [https://developer.twitter.com/](https://developer.twitter.com/)
2. create an app
3. create Oauth1 credentials
4. Enter your API credendtials in `tweet.py`
   

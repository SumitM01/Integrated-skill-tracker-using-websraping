# Integrated Skill Tracker using Web Scraping
This project is an Integrated Skill Tracker web application that scrapes job listing websites to track the skills that are currently in demand in the job market. The application uses Django as the web framework, Selenium for web scraping, and Celery for task scheduling. This application serves as a central hub for various skill practicing websites, including HackerRank, Codechef, etc. Users can access these websites through a single platform, making it easier to track progress and improve skills...

## Prerequisites

To run this app on your local machine, you will need to have the following installed:

- Python 3.6+
- Django 3.2+
- Selenium 3.141+
- Celery 5.0+

## Installation

Clone the repository:

```bash
  git clone https://github.com/SumitM01/Integrated-skill-tracker-using-webscraping.git
```

Install the required dependencies using pip

```pip
  pip install -r requirements.txt
```
Set up your MongoDB and create a `.env` file with your MongoDB connection string:

```Python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database_name',
        'USER': 'database_user',
        'PASSWORD': 'database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
Run the database migrations
```Python
python manage.py migrate

```
Start the Celery worker
```Python
celery -A Integrated_Coding worker -l info

```
Start the Django development server
```Python
python manage.py runserver

```
Access the web application at `http://localhost:8000/`

## Usage/Examples

- Create an account and add your desired coding platform profiles to track.
- Save the details in the user page and you are done.
- The scraping process is run asynchronously using Celery, so the user can continue using the application while the scraping is ongoing.
- Once the scraping is complete, the user can view the Stats for each platform, Leaderboard position, and ongoing contests on the homepage and contests page.
- We've also implemented practice problems with links to external sites to give an idea of where to start DSA.

## Screenshots

![profile image](https://github.com/SumitM01/Integrated-skill-tracker-using-websraping/assets/65524561/3367f29c-a5c6-4563-a113-3877473a7a4b)
![dashborad image](https://github.com/SumitM01/Integrated-skill-tracker-using-websraping/assets/65524561/4fbea5d2-e55b-474d-9123-353c93cd927f)
![contest image](https://github.com/SumitM01/Integrated-skill-tracker-using-websraping/assets/65524561/69fafb3f-b14b-4f9b-9175-b2044aaad019)
![leaderboard image](https://github.com/SumitM01/Integrated-skill-tracker-using-websraping/assets/65524561/260c811b-a592-4ee1-8da8-bda4c07b9eee)
![report Image](https://github.com/SumitM01/Integrated-skill-tracker-using-websraping/assets/65524561/abb6c14f-a7a6-433a-9f7f-97018229b152)
![problem image](https://github.com/SumitM01/Integrated-skill-tracker-using-websraping/assets/65524561/d86115ef-eee7-4d4f-aa6d-cdbd029f64a8)

## License

This project is licensed under the MIT License. see the
[MIT](https://choosealicense.com/licenses/mit/) file for details.

## Acknowledgements

This project was built as a part of a university assignment. Special thanks to our professor for giving us the opportunity to work on this project and learn new technologies.

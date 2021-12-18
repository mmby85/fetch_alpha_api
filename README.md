# fetch_alpha_api

A simple Django code to fetch BIT/USD price every hour, 

to run the app just use :
sudo docker-compose up

please add your .env file :  
ALPHA_KEY=your_api_alpha_key  
SECRET_KEY=django_secret_key  
DATABASE_NAME=alpha  
DATABASE_USER=alpha  
DATABASE_PASS=alpha  

SECRET_KEY can be generated with :  
#from django.core.management.utils import get_random_secret_key  
#get_random_secret_key()  

you can get the ALPHA_KEY at link: https://www.alphavantage.co/support/  

To get the records from db go to :  
/data  
to force post (to create new record):  
/create  
then you click on post button  

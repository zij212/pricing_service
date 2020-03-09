# Pricing service
I am taking the [Complete Python Web Course: Learn by Building 8 Apps](https://www.udemy.com/course/the-complete-python-web-course-learn-by-building-8-apps/) class on Udemy. 

In this repository I followed the instructor's videos to create a simple price tracking application.

**Features**  
- A user can sign up for an account, log in, create/edit/delete a pricing alert.  
- An alert is what user create to track price of an item on an online store. The user will need to set a price limit for the item. When the price limit user set is reached, user will be emailed an notification. 
- When user creates an alert, it will also create an item.
- On top of what a normal user can do, an admin user can create/edit/delete a store. 
- The store holds the domain and tags which is used to find the price on the webpage.

**Things that I learnt from this project**  
- Model-view-controller framework  
- abstract class and method  
- use @dataclass to create data classes
- session  
  - securing a session using app.secret_key  
  - show content based on user's sessioification  
- decorate endpoints to limit what certain users can do (in blueprints)    
- encrypting password using passlib  
- use js from Bootstrap to make a navigation bar  
- using Mailgun's api to send email notification  
- deploying app on heroku  

**Heroku**  
I had difficulties to do `pipenv lock` because I was not able to install uwsgi successfully using pipenv. I decided to remove Pipfile and Pipfile.lock from my remote repo and add the required packages in requirements.txt.  
Try my price tracking app out at https://pricing-service-zij212.herokuapp.com/  

I am still working on deployment on Digital Ocean. 

# Pricing service
I am taking the [Complete Python Web Course: Learn by Building 8 Apps](https://www.udemy.com/course/the-complete-python-web-course-learn-by-building-8-apps/) class on Udemy. 

In this repository I followed the instructor's videos to create a simple price tracking application.

A user can sign up for an account, log in, create/edit/delete a pricing alert.  
An alert is what user create to track price of an item on an online store. When the price limit user set is reached, user will be emailed an notification. 
On top of what a normal user can do, an admin user can create/edit/delete a store. The store helps 

Things that I learnt from this project:  
- Model-view-controller framework  
- abstract class and method  
- use @dataclass to create data classes
- session  
  - securing a session using app.secret_key  
  - show content based on user's sessioification  

I am still working on deployment on Heroku and Digital Ocean.  
  - decorate endpoints to limit what certain users can do (in blueprints)    
- encrypting password using passlib  
- use js from Bootstrap to make a navigation bar  
- using Mailgun's api to send email notification  

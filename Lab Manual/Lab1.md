Lab 1 E-Commerce
 a. Objective The overall objective of the lab is to create an e-commerce website. But, the first lab has the following objectives:
 Installing and configuring appropriate operating and building environments To create a superuser and users, as well as to run the server Modules must be added and CRUD operations must be verified. b. Introduction For this lab, we employ a variety of frameworks and settings. The IDE we used was VS Code, and the framework was Python/Django. An e-commerce website is one that allows users and sellers to buy and sell things over the internet. It is one of the most effective current company models. E-commerce platforms make purchasing goods and services easier. For this lab report, we will create an e-commerce website.
 b. We also need to be aware of the various languages. Python is the most widely used programming language, thanks to its simple syntax and efficient structure. Django is a Python web-based open-source framework. Django has a lot of built-in models, which makes it easy to concentrate on the application's writing. VS Code is also one of the most versatile IDEs available.

c. This lab also uses Git for source control. We may also utilize Github Desktop to commit and push our code to a GitHub repository. When the repository is made public, anyone can access it.

Procedure:
Initializaing environment
We obtained the necessary software and environments for the project. They were as follows:

Github account for Python Pip Sqlite DBeaver Django VS Code We already had some and were able to set up the rest. In the case of several operating systems with the same functionality, the software could be different. We double-checked that everything was in functioning order.

Migrating and creating users
We started the project and moved files after setting up the environment.
Syntax: django-admin startproject ecommerce_aarya cd ecommerce_aarya python manage.py migrate

We ran the server if it was working. Then, we got the link for the server as 127.0.0.1:8000. Again, we verified the admin side using 127.0.0.1:8000/admin. We were able to create a superuser and other users. Syntax: python manage.py runserver
Database verification and CRUD operations
Then, we added a module product_module and migrated files to the database. Now, we were able to do CRUD operations on the server. Syntax: python manage.py startapp product_module ……. python manage.py runserver

Source Control
Finally, we used Git for source control. We created a repository with the name ecommerce_Aarya and created a markdown file “lab1.md” which is this document. Then, we committed and pushed the code and folder to the repository.https://github.com/Aahrya/ecommerce_aarya/tree/main/Lab%20Manual
d. Output Installation of python| pip alt text
C
Creation of project folder alt text

Migration alt text

Creating superuser alt text

Running server alt text alt text

Logging In alt text

CRUD operation alt text

Git initialization alt text
e. In conclusion We learned a lot from the first e-commerce lab. The initial setup aided us in quickly creating environments and setting up. Then we knew how to start a Django project. It was also learned how to operate the server. On the server, we knew how to perform CRUD operations. Finally, we learned more about Git and Github for source control. Our code was easily available after we created a Github repository and shared it.

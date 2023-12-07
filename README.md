
#      Blog Application Using Django Template

Welcome to Our Blogging Application!

Express yourself effortlessly with our simple and secure Django Blog App. Create, share, and connect in a heartbeat. Engage with the community, personalize your space, and start your blogging journey with a few clicks.

Your Stories, Your Way. Happy Blogging! 🚀




## Getting Started


1-First of all clone this repo
--
--> git clone https://github.com/AyushTmg/Postables_with_classbased_views.git


2-Setup a virtual enviroment
--
-->python -m venv venv


3-Install all dependencies from the requirements.txt in a virtual enviroment
--
--> pip install -r requirements.txt


4-Update the DATABASES settings in settings.py  in this case postgres is used 
--
DATABASES = {\
   'default': {\
        'ENGINE': 'django.db.backends.postgresql',\
        'NAME':os.environ.get("DB_NAME"),\
        'USER': 'your_database_user',\
        'PASSWORD': os.environ.get("DB_PASS"),\
        'HOST': 'localhost',\
        'PORT': '5432',\
}\
}


5-Add .env file and add these field
--

DB_NAME='database name'
DB_PASS='database password'


6-Migrate the changes to your database
--
-->python manage.py migrate\
-->python manage.py runserver


7-Run Application
--
-->python manage.py runserver




# How Application Homepage will look like !
--
![image](https://github.com/AyushTmg/Postables_with_classbased_views/assets/119398357/f0a3cbab-5a68-497a-be07-4f873baf527f)



#                How it Works



User Authentication:
--


- To use the application, users need to sign up and create an account.

- Registration Page\
![image](https://github.com/AyushTmg/Postables_with_classbased_views/assets/119398357/d940ad3a-4431-4d36-81d5-aedbf99acf46)


- Once registered, users can log in securely to access the full functionality of the blog application.

- Login Page\
![image](https://github.com/AyushTmg/Postables_with_classbased_views/assets/119398357/6971412a-2a9e-4c99-afcc-1ab83f411192)



Create and Delete Posts:
--

Users can effortlessly create new blog posts to share their thoughts and experiences.
Only the post owner has the authority to delete their posts, ensuring control over content.

- Post Creation Page\
![image](https://github.com/AyushTmg/Postables_with_classbased_views/assets/119398357/db28f28b-29b2-4831-bd6f-0e233247d40f)

- Post Deletion Confirmation \
![image](https://github.com/AyushTmg/Postables_with_classbased_views/assets/119398357/b64b9a5f-53a8-4733-ab7c-5f312b38c528)



Leave Reviews and Reply:
--


Users can engage with posts by leaving reviews.
Additionally, users can reply to reviews, fostering interactive discussions within the community.

- Adding Post Review Page\
![image](https://github.com/AyushTmg/Postables_with_classbased_views/assets/119398357/333f7e68-f9bc-4fe4-8277-5af731b47f18)

- Review Page\
![image](https://github.com/AyushTmg/Postables_with_classbased_views/assets/119398357/f85f7384-94e8-4a28-9820-aa1c4e04661b)

- Deletion Of User Written Review Confirmation\
![image](https://github.com/AyushTmg/Postables_with_classbased_views/assets/119398357/e9a751f2-e368-4ba9-af5f-ae10e010742c)



Profile Management:
--


Users have the option to view and edit their profiles, providing a personalized experience.

- User  Profile Page\
![image](https://github.com/AyushTmg/Postables_with_classbased_views/assets/119398357/7c6d346f-1796-480b-9276-ba6ca2423d3b)

- To Edit And Update Profile Info\
![image](https://github.com/AyushTmg/Postables_with_classbased_views/assets/119398357/86605152-9ad8-4f70-8822-b5ff536493ce)

-User Profile With Profile Picture\
![image](https://github.com/AyushTmg/Postables_with_classbased_views/assets/119398357/88942f87-d3a0-4249-9697-d011ed6c278d)



View their Own Posts: 
-- 

Users can easily view a list of their posted content.
Editing posts is a seamless process, allowing users to keep their content up-to-date.

- Viewing Logged-in Users Post (in this case GOD)\
![image](https://github.com/AyushTmg/Postables_with_classbased_views/assets/119398357/4b363d68-c7db-4e3a-ad2a-47a77f3270aa)




Change Password:
--
Users can change their password by providing the old password for security verification.

- To change password with old password\
![image](https://github.com/AyushTmg/Postables_with_classbased_views/assets/119398357/a52bfbd3-aa88-4c02-8af1-acdc7819b47f)

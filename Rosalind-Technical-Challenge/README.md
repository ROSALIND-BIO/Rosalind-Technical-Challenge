# Gym App

You're starting your own gym business, and you decided to get rid of the pen and paper and move all your clients to your website. For this, you decided to build yourself a Django app to power your systems.

Your gym opens for **8 hours a day (from 8a to 6p), 6 days (Monday to Saturday) a week**, and for organization purposes, **each student can schedule an hour per day to work out**.

Your gym has 3 teachers available to help the students on different days of the week.

| Teacher   | Schedule                                                  |
| --------- | --------------------------------------------------------- |
| Mr. Jones | Monday - Tuesday: 8a - 10a and Friday - Saturday: 4p - 6p |
| Ms. Robin | Wednesday - Thursday: 8a - 6p                             |
| Mr. Tony  | Monday - Tuesday: 11a - 6p and Friday - Saturday: 8a - 3p |

## 📝 Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [My Own Local Development](#LocalDevelopmentProcess)
  - [Using docker](#using-docker)
  - [Running Locally](#running-locally)
- [Challenge Specs](#challenge-specs)
  - [Basic Guidelines](#basic-guidelines)
  - [Tasks](#tasks)
    - [Task 1](#task-1)
    - [Task 2](#task-2)
    - [Task 3](#task-3)

### Getting Started

#### Prerequisites

You will need:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

You are free to use any package manager (we use [Conda](https://docs.conda.io/en/latest/)). Install the project dependencies with pip:

```
pip install -r requirements.txt
```

##### Using docker

We have a Docker image available for use, inside the `images` folder.

- `dev.dockerfile` for local development

You can build and run this Docker image using the following commands:

- `docker-compose -f images/dev.docker-compose.yaml up -t 1 --abort-on-container-exit`

Please inspect the contents of these Dockerfiles, so you're aware of what they're doing. You're free to make changes to these files, create your own, or ignore Docker development entirely.

If you choose to ignore Docker development, please be prepared to provide information on your local development process.

##### Local Development Process to follow for the codebase

1. Make sure you have Postgresql installed and open up pgAdmin 4 on your laptop or any version of pgAdmin that you have.
2. Create a table called 'gym_app' by choosing what env of postgres you are using, right-clicking on databases and selecting on create -> database, and putting the database name as 'gym_app' under the General tab.
3. Go to the path of which the codebase is located at.
4. Run the following command `pip install -r requirements.txt`
5. Make your migrations with the following command: `python manage.py makemigrations`
6. After making the migrations execute the following command: `python manage.py migrate`
7. To run the server run the following command: `python manage.py runserver`
8. Once running, your server should be available on [127.0.0.1:8000](http://127.0.0.1:8000/).

##### Running Locally

We support local development inside of Docker containers. This uses the `dev.dockerfile` Dockerfile.

To run locally, you can use `docker-compose -f images/dev.docker-compose.yaml up -t 1 --abort-on-container-exit`.

This will start up a PostgreSQL database, run any new migrations against the database, and start up a Django server. This Django server will be available to you on your

Once running, your server should be available on [127.0.0.1:8000](http://127.0.0.1:8000/).

### Challenge Specs

#### Basic Guidelines

1. Your Django ORM models should be compatible with PostgreSQL.
2. All custom Django ORM models should live within the `rosalind` app.
3. Modifications to Django ORM models should be properly addressed as migrations.
4. You are allowed to create as many files as you want, and modify any files as well.
5. You are allowed to add any libraries that you want, but they need to be properly added to the `requirements.txt` file.

#### Tasks

##### Task 1

1. Create a page to register new users. These users will need access to Django's admin pages, so be sure to give appropriate access.

##### Task 2

1. Implement admin pages for adding/updating/removing teacher information
   1. Required table fields are: name, phone number, email address, birthday.
2. Implement admin pages to create and update a teacher's schedule (the day of the week and hours/slots that the teacher is available at the gym).
   1. You are free to choose whatever is the best way to store this information.

##### Task 3

1. Implement a public page that displays all teacher schedules. This should be a public page (aka not an admin-only page).

##### How to navigate through the app for task 1

1. In order to register a new normal user, click on the 'Register' field on the navbar of the webpage and fill out all the necessary details.
2. This would then redirect you to the login page where you would put in the username and the password.
3. If you would like to login as an admin user, here are the following steps:
4. Make sure to create a superuser through running the following command under the location of the project: `python manage.py createsuperuser`
5. Once you filled out the necessary information, make sure the information is stored under the 'admin_user' table in your database.
6. Navigate to the following url: (http://127.0.0.1:8000/admin) and login based on the username and password that you have created.
7. Once logged in, on the top right corner of the page there is a 'VIEW SITE' tab; click on this and it will direct you to the site as logged-in admin user.

##### How to navigate through the app for task 2 part 1

1. Make sure that you are logged-in as a admin user. For reference please refer to 'How to navigate through the app for task 1' for more details.
2. In order to add teacher information, there is a tab on the navigation bar called 'Teacher_Register' where you could add the information for a Teacher and save it into the 'rosalind_teacher' table on the 'gym_app' database.
3. Once you click on the 'Register' button, this should redirect you to the following page: (http://127.0.0.1:8000/showTeacherRegister).
4. On this page, you can view the information about the added teacher and whether or not you would like to edit or delete their information.
5. If you would like to edit the teacher's information, click on the 'Edit' field on the generated table and it will redirect you to the following page: (http://127.0.0.1:8000/editTeacherRegister/<'id of added teacher'>)
6. Make the necessary edits and hit 'Update' and it will redirect you back to the (http://127.0.0.1:8000/showTeacherRegister) webpage.
7. If you would like to delete the teacher's information, click on the delete field on the generated table and this would delete the record of the teacher.

##### How to navigate through the app for task 2 part 2

1. Make sure that you are logged-in as a admin user. For reference please refer to 'How to navigate through the app for task 1' for more details.
2. In order to add teacher's schedule information, there is a tab on the navigation bar called 'Teacher_Schedule_Register' where you could add the information for a TeacherSchedule and save it into the 'rosalind_teacherschedule' table on the 'gym_app' database.
3. Once you click on the 'Register' button, this should redirect you to the following page: (http://127.0.0.1:8000/showTeacherScheduleRegister).
4. On this page, you can view the information about the added teacher's schedule and whether or not you would like to edit or delete their information.
5. If you would like to edit the teacher's schedule information, click on the 'Edit' field on the generated table and it will redirect you to the following page: (http://127.0.0.1:8000/editTeacherScheduleRegister/<'id of added teacher'>)
6. Make the necessary edits and hit 'Update' and it will redirect you back to the (http://127.0.0.1:8000/showTeacherScheduleRegister) webpage.
7. If you would like to delete the teacher's schedule information, click on the delete field on the generated table and this would delete the record of the teacher.

##### How to navigate through the app for task 3

1. Once the table has been generated from the 'Teacher_Schedule_Register' tab, you would be able to view this table and all the necessary changes it will go through as either a normal logged-in user, an admin user, or as a public user without any login.

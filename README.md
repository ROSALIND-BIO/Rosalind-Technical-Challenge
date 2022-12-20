# Gym App

You're starting your own gym business, and you decided to get rid of the pen and paper and move all your clients to your website. For this, you decided to build yourself the REST API to power your systems.

Your gym opens for **8 hours a day (from 8a to 6p), 6 days (Monday to Saturday) a week**, and for organization purposes, **each student can schedule an hour per day to work out**.

Your gym has 3 teachers available to help the students on different days of the week.

| Teacher   | Schedule                                              |
|-----------|-------------------------------------------------------|
| Mr. Jones | Monday - Tuesday: 8a - 10a and Friday - Saturday: 4p - 6p |
| Ms. Robin | Wednesday - Thursday: 8a - 6p                         |
| Mr. Tony  | Monday - Tuesday: 11a - 6p and Friday - Saturday: 8a - 3p |


## 📝 Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
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

##### Running Locally

We support local development inside of Docker containers. This uses the `dev.dockerfile` Dockerfile.

To run locally, you can use `docker-compose -f images/dev.docker-compose.yaml up -t 1 --abort-on-container-exit`.

This will start up a PostgreSQL database, run any new migrations against the database, and start up a Django server. This Django server will be available to you on your 

Once running, your server should be available on [localhost:8000](http://localhost:8000/).

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

# Football Players Managers

This project is a  Web Application Service that allows to retrieve information of football players.


## Getting Started

### Deployment

This application was implemented using the following technologies:

* [Python](https://www.python.org/) - Programming Language
* [Werzeug](https://werkzeug.palletsprojects.com/) - Web application library
* [SQLALchemy](https://www.sqlalchemy.org/) - Python SQL toolkit
* [MySQL](https://www.mysql.com/) - Data Base technology.
* [Pandas](https://pandas.pydata.org/) - Data Manipulation.
* [Docker](https://www.docker.com/) - Docker Containers.
* [Heroku](https://www.heroku.com/) - Cloud platform for building Pythonic apps.


## Requirements

* Python 3.x.x (3.6.10)
* Docker

<br/>

## Running the application 

### Docker Instructions

*(Ensure Docker is installed on your system.)*

#### 1-) Running the containers:

First, clone the repository on your local machine and execute the following commands:

```
$ docker-compose up
```

At this point, the Django app should be running at port 8000 on your Docker host.


#### 2-) List running containers:

In another terminal window, list the running Docker processes with the docker container ls command.

```
$ docker ps
```


#### 3-) Login into the Docker Container.

List containers via:

```
$ docker container ls
```

Run this command in the running container using its *container-id*, to get a bash shell in the container. 
Generically, use docker exec -it <container name> <command> to execute whatever command you specify in the container.

```
$ docker exec -it <container-id> /bin/bash
```


#### 4-) Shut down services and clean up:

- Stop the application by typing Ctrl-C in the same shell in where you started it.

- Or, for a more elegant shutdown, switch to a different shell, and run docker-compose down from the top level of the Django project directory.

```
$ docker-compose down
```
<br/>


## Task Observations:

### Player's Positions

Some of the game positions set out in the task description do not match the positions the player's positions the database.

Real positions:

* Goalkeeper: GK

* Fullback: RCB, CB, LB, RB, RWB, LWB

* Halfback = RCM, LCM, LDM, CDM, LCB, RM, LM, RDM, CM

* Forward = RF, ST, LW, LF, RS, CAM, LS, LAM, RW, RAM, CF

### Player's Picture

The link of the players' photos in the database is not correct, it seems that the website that stores them changed the design of the urls so they produce a **404**.

<br/>

## Additional Questions:

Q- What technology (apart from Python, which is required), DB, and tools did you use
and why do you think it’s a good pick?

### Project Technologies Requirements:

- [Python](https://www.python.org/)  
- [MySQL](https://www.mysql.com/) 
- [Docker](https://www.docker.com/)

### Other Chosen Technologies:

#### [Werzeug](https://werkzeug.palletsprojects.com/) - Web application library:

Since one of the requirements of the project is not to use any framework like Django or Flask, I decided to use **Werkzeug**.

Werkzeug is a comprehensive WSGI web application library. Werkzeug is not a framework, it’s a library with utilities to create your own framework or application and as such is very flexible.  It allows us to design a template engine, a database adapter, and even how to handle requests.

**Advantages:**

- A response object that can wrap other WSGI applications and handle streaming data.

- A routing system for matching URLs to endpoints and generating URLs for endpoints, with an extensible system for capturing variables from URLs.

- HTTP utilities to handle entity tags, cache control, dates, user agents, cookies, files, and more.

- A threaded WSGI server for use while developing applications locally.

- A test client for simulating HTTP requests during testing without requiring running a server.

#### [SQLALchemy](https://www.sqlalchemy.org/) - Python SQL toolkit:

**SQLAlchemy** is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.

**Advantages:**

SQLAlchemy maintains a connection pool, with an open database connection being provided to each web request. The library handles common errors effectively, making applications robust against scenarios such as the database being restarted while the application is running.



#### [Pandas](https://pandas.pydata.org/) - Data Manipulation.

**Pandas** is a Python package providing fast, flexible, and expressive data structures (data frames) designed to make working with “relational” or “labeled” data both easy and intuitive.

**Advantages:**

For this particular problem I think using pandas is an advantage in order to improve the data handling, cleaning and manipulation processes. The *dataframes* data structure provide an


#### [Pulp](https://pypi.org/project/PuLP/) - Linear Programming Library:

This library allows us to model and solve linear programming problems, especially used to model linear optimization problems. Linear programming is a technique for the optimization of a linear objective function, subject to linear equality and linear inequality constraints. 

**Advantage:**

- Modelling and solution for the team builder exercise.


[Heroku](https://www.heroku.com/) - Cloud platform for building Pythonic apps.

Heroku Container Registry allows you to deploy your Docker images to Heroku. 

**Advantage:** 

- Easy to build a Docker images, as well as take advantage of Review Apps, check out building Docker images with heroku.yml.


Q- Let's say we want to add all the players created by users (between 5,000,000 to
20,000,000 new players per month) to the database. We also decide to add real-time
updates to the player database. What tech stack will you use? (Language, DB,
hosting, etc.) How would you make sure your tool is scalable for higher volumes?

#### Technologies: 

* Programming Language:

* DataBase:

MongoDB

* Hosting:

Scalability




### Author:

* **Ernesto Zarza**
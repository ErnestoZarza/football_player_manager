# Football Players Managers

This project is a  Web Application Service that allows to retrieve information of football players.

### Features:

#### * Search Players:

  Search engine that displays the players that match the search criteria. The “searchable” attributes are: **name**, **club** & **nationality**.

The displayed attributes for a search result are the following:
* Name
* Age
* Nationality
* Club
* Photo (Generic Picture)
* Overall
* Value
       
#### * Team Builder:
       
This feature shows a list of 11 players that constitute the best team one can have for this specific budget . The best player is defined by their overall score.

**Positions:**
* Goalkeeper: GK
* Fullback: RCB, CB, LB, RB, RWB, LWB</li>
* Halfback = RCM, LCM, LDM, CDM, LCB, RM, LM, RDM, CM</li>
* Forward = RF, ST, LW, LF, RS, CAM, LS, LAM, RW, RAM, CF</li>
       
**Constraints:**
* 1 GK</li>
* 2 Fullback</li>
* 3 Halfback</li>
* 5 Forward</li>
      
<br/>

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

<br/>


## Requirements

* Python 3.x.x (3.6.10)
* Docker

<br/>

## Running the application (Local)

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


## Web Application:

This web application is hosted on Heroku. You can find it in the following link: http://football-players-manager.herokuapp.com/

This application is not in production mode, eg. use_debugger=True (on purpose).

<br/>

## Additional Questions:

**Q-** What technology (apart from Python, which is required), DB, and tools did you use
and why do you think it’s a good pick?
<br/>

### Project Technologies Requirements:

- [Python](https://www.python.org/)  
- [MySQL](https://www.mysql.com/) 
- [Docker](https://www.docker.com/)

### Other Chosen Technologies:

#### [Werkzeug](https://werkzeug.palletsprojects.com/) - Web application library:

Since one of the requirements of the project is not to use any framework like Django or Flask, I decided to use **Werkzeug**.

Werkzeug is a comprehensive WSGI web application library. Werkzeug is not a framework, it’s a library with utilities to create your own framework or application and as such is very flexible.  It allows us to design a template engine, a database adapter, and even how to handle requests.

**Advantages:**

- A response object that can wrap other WSGI applications and handle streaming data.

- A routing system for matching URLs to endpoints and generating URLs for endpoints, with an extensible system for capturing variables from URLs.

- HTTP utilities to handle entity tags, cache control, dates, user agents, cookies, files, and more.

- A test client for simulating HTTP requests during testing without requiring running a server.

<br/>

#### [SQLALchemy](https://www.sqlalchemy.org/) - Python SQL toolkit:

SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.

**Advantages:**

SQLAlchemy maintains a connection pool, with an open database connection being provided to each web request. The library handles common errors effectively, making applications robust against scenarios such as the database being restarted while the application is running.

<br/>

#### [Pandas](https://pandas.pydata.org/) - Data Manipulation.

Pandas is a Python package providing fast, flexible, and expressive data structures (data frames) designed to make working with “relational” or “labeled” data both easy and intuitive.

**Advantages:**

- For this particular problem I think using pandas is an advantage in order to improve the data handling, cleaning, manipulation processes. The *dataframes* data structure provide an that provides a quick and efficient way to retrieve data for the solution of the optimization problem of creating the teams.
<br/>

#### [Pulp](https://pypi.org/project/PuLP/) - Linear Programming Library:

This library allows us to model and solve linear programming problems, especially used to model linear optimization problems. Linear programming is a technique for the optimization of a linear objective function, subject to linear equality and linear inequality constraints. 

**Advantage:**

- Modelling and optimal solution for the team builder exercise.

<br/>

#### [Heroku](https://www.heroku.com/) - Cloud platform for building Pythonic apps.

Heroku Container Registry allows you to deploy your Docker images to Heroku in a simple and fast way. 

**Advantage:** 

- Easy to build a Docker images, as well as take advantage of Review Apps. Also, the possibility building Docker images using heroku.yml.

<br/>

**Q-** Let's say we want to add all the players created by users (between 5,000,000 to
20,000,000 new players per month) to the database. We also decide to add real-time
updates to the player database. What tech stack will you use? (Language, DB,
hosting, etc.) How would you make sure your tool is scalable for higher volumes?

<br/>

#### Programming Language:

##### Python:

If using **Python** would be a requirement for the project. I would strongly consider the use of a framework.

For example Django provides a [django-filter](https://django-filter.readthedocs.io/en/stable/) package in order to add a hassle-free filtering to your views with a straightforward integration with the templates.

Another point would be to consider a strong caching strategy. Many python web frameworks allow you to establish cache policies in order to achieve a better performance in the application.


##### Scala:

I think it would be convenient to consider a change of language in order to accelerate the performance of the application.

Scala is frequently over 10 times faster than Python. Scala uses Java Virtual Machine (JVM) during runtime which gives is some speed over Python in most cases. Python is dynamically typed and this reduces the speed. Compiled languages are faster than interpreted.

Scala has multiple standard libraries and cores which allows quick integration of the databases in Big Data ecosystems. Scala allows writing of code with multiple concurrency primitives whereas Python doesn’t support “entirely” concurrency or multithreading. Due to its concurrency feature, Scala allows better memory management and data processing. However, Python does support heavyweight process forking.

Companies like Twitter switched to Scala. They said: "Scala is extraordinarily suited for handling real-time messaging on a large scale".

<br/>

#### Search Engine

##### Elasticsearch:

Another consideration is to integrate a more powerfull Search Engine technology like Elasticsearch. The speed and scalability of Elasticsearch and its ability to index many types of content mean that it can be used for a number of use cases. It provides scalable search, has near real-time search, and supports multitenancy.

<br/>

#### DataBase:

##### MongoDB:

MySQL is highly-organized for its flexibility, high performance, reliable data protection and ease in management of data. Proper data indexing can resolve your issue with performance, facilitate interaction and ensure robustness. Many developers note that MySQL is quite slow in comparison to MongoDB when it comes to dealing with the large database. Hence, it is a better choice for users with small data volume and is looking for a more general solution as it is unable to cope with large and unstructured amounts of data. It allows users to query in a different manner that is more sensitive to workload.

##### Alternative - Amazon Aurora: 

Amazon Aurora is up to five times faster than standard MySQL databases and three times faster than standard PostgreSQL databases. It provides the security, availability, and reliability of commercial databases at 1/10th the cost. Amazon Aurora is fully managed by Amazon Relational Database Service (RDS), which automates time-consuming administration tasks like hardware provisioning, database setup, patching, and backups.

Amazon Aurora is a MySQL and PostgreSQL-compatible relational database built for the cloud, that combines the performance and availability of traditional enterprise databases with the simplicity and cost-effectiveness of open source databases.


<br/>

#### Hosting:

For this particular aspect I would consider any provider that allows for multiple replications and can provide a Zero-downtime Deployment. It would be a bonus point if can handle scaling automatically.

Example: **Heroku**



### Author:

* **Ernesto Zarza**

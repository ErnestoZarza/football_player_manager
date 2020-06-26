# Football Players Managers

This project is a  Web Application Service that allows to retrieve information of football players.


## Getting Started

### Deployment

This application was implemented using the following technologies:

* [Python](https://www.python.org/) - Programming Language
* [Werzeug](https://werkzeug.palletsprojects.com/) - Web application library
* [SQLALchemy](https://www.sqlalchemy.org/) - Python SQL toolkit
* [MySQL](https://www.mysql.com/) - Data Base technology.
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

* [Python](https://www.python.org/) - Programming Language (Project Requirement):



* [Werzeug](https://werkzeug.palletsprojects.com/) - Web application library:


* [SQLALchemy](https://www.sqlalchemy.org/) - Python SQL toolkit:


* [MySQL](https://www.mysql.com/) - Data Base technology (Project Requirement):


* [Docker](https://www.docker.com/) - Docker Containers (Project Requirement):


* [Heroku](https://www.heroku.com/) - Cloud platform for building Pythonic apps:




Q- Let's say we want to add all the players created by users (between 5,000,000 to
20,000,000 new players per month) to the database. We also decide to add real-time
updates to the player database. What tech stack will you use? (Language, DB,
hosting, etc.) How would you make sure your tool is scalable for higher volumes? 


### Author:

* **Ernesto Zarza**
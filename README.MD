<div align="center" id="top">
  <img src="./.github/app.gif" alt="Api_2" />

  &#xa0;

  <!-- <a href="https://api_2.netlify.app">Demo</a> -->
</div>

<h1 align="center">API FOR TENANTS AND USERS</h1>

<p align="center">
</p>

<!-- Status -->

<hr>

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="https://github.com/jamesandrade" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

API FOR TENANTS AND USERS USING PYTHON, POSTGRES AND DOCKER COMPOSE

## :rocket: Technologies ##

The following tools were used in this project:

- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com), [Docker](https://www.docker.com/) and [Docker-Compose](https://docs.docker.com/compose/gettingstarted/) installed.

## :checkered_flag: Starting ##

```bash

# Clone this project
$ git clone https://github.com/jamesandrade/flask-api

# Access
$ cd flask-api

# Install dependencies
$ sudo docker-compose build

# Run the project
$ sudo docker-compose up

# In your POSTGRES:
CREATE DATABASE userapp

# Run migrations with server started
$ sudo docker-compose exec web flask db upgrade --directory src/infra/database/orm

# for new migration
$ sudo docker-compose exec web flask db migrate --directory src/infra/database/orm
# The server will initialize in the <http://localhost:5000>
# Test the api in the <http://localhost:5000/>
# it is recommended to use Virtual Environments (https://docs.python.org/3/tutorial/venv.html)
```

<!--## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/{{YOUR_GITHUB_USERNAME}}" target="_blank">{{YOUR_NAME}}</a>
-->
&#xa0;

<a href="#top">Back to top</a>
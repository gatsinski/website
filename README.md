# website
Simple website developed using some of the best practices in the industry.

## Overview
The backend is developed with **Django** which is one of the most popular
**Python** web frameworks. Additional functionality is added by **Django CMS**
and many of its official plugins. Custom plugins and apps are written to extend
the list of features.

The recomended database for the project is **PostgreSQL** but other databases
such as **MySQL** or **SQLite** can be used.

All static files are automatically bundled, compressed and minified to reduce
the final project size. This task is managed by **Django Pipeline** and it is
performed only on production environment. During development all files are
displayed unmodified to ease debugging.

All Python libraries are installed and managed by **Pipenv** but yet optional
`requirements.txt` files is kept for users who prefer the old approach.

**Bootstrap** is used for the frontend together with custom styles written
entirely with **Sass**. The **Sass** source files are compiled into **CSS** by
**Django Pipeline**. **Font Awesome** icons are also used in the project.

All frontend dependencies are managed with **Node Package Manager (NPM)**.

`Dockerfile` and `docker-compose.yml` files are provided for development and
deployment purposes. While the use of **Docker** is optional it is highly
recomended because this is one of the most popular ways of working with
software projects in an isolated environment.

The communication with **Django** is handled by **uWSGI**. Additional
`uwsgi.ini` file is provided to ease the project setup.

It is suggested to use **NGINX** as **HTTP** server but alternatives like
**Apache HTTP Server** are also an option. By default the communication with
the **WSGI** server is established with **UNIX** socket file instead of **TCP**
port sockets to reduce overhead and to increase performance.

The socket can be found and accessed in **Docker** volume alongside with other
useful data such as **uWSGI** logs, static files and media files. While
**uWSGI** is capable of serving the latter two it is recomended to use
**NGINX** because it is more efficient.

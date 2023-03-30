Installation tips
=================

Setup environment
-----------------

#) Install *virtualenvwrapper*

#) Create virtual environment via **mkvirtualenv**

#) Run `pip install -r requiements/local.txt`

Initialize variables
--------------------

#) Modify .init in order to provide correct environment variables

#) Place content of .init at the bottom of bottom of
   activate script in <your virtual environment>/bin
   or just run source .init

# Modern

Build image `docker build -t spring_blog:latest .`
Run `docker run -it --rm -v "$PWD:/usr/src/app" spring_blog:latest /bin/sh`


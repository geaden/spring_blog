heroku config:add SECRET_KEY=`cat secret.txt`
heroku config:add DJANGO_SETTINGS_MODULE=hotdot.settings.staging
heroku config:add PYTHONPATH=$PYTHONPATH:./hotdot/hotdot

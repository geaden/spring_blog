export SECRET_KEY=$( cat secret.txt )
export DJANGO_SETTINGS_MODULE=hotdot.settings.local
export PYTHONPATH=$PYTHONPATH:./hotdot/hotdot

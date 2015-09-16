# To see this in action

cd into the same directory as the Makefile

`make run` <-- this will kick off the local server

In a seperate process:
`make cron` <-- this will invoke a custom django command

General process:
Made new django project (`django-admin startproject schedule_task_example` from w/in virtual env)
Made new django app w/in project (`env/bin/python manage.py startapp tasks`)
Registered `tasks` in INSTALLED_APPS of settings.py under the project directory
Created custom django-admin commands [here](https://docs.djangoproject.com/en/dev/howto/custom-management-commands/#howto-custom-management-commands)

What would be remaining:
Scheduling `make cron` with the cron job handler on the deployed server
Determining some way to store the data generated from each `make cron` run
Fetching said data store when generating a view in the django app

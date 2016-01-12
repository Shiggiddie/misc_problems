env:
	virtualenv env
	env/bin/pip install -r requirements.txt

run: env
	env/bin/python manage.py runserver

cron: env
	env/bin/python manage.py check_endpoints_same

clean:
	rm -rf env

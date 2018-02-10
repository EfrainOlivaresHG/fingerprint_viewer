help:
	@echo
	@echo Utilities for managing application
	@echo
	@grep ^#% makefile | sed 's/#%//'
	@echo

#%      run - Start server for web app
run:
	python manage.py runserver -h 0.0.0.0 -p 5000 

#%      install - install python and flask requirements for webapp
install:
	pip install -r requirements.txt

mosquitto_container_name := "mosquitto"
venv_folder              := ".env"

##########################################
# Virtual environment recipes
##########################################

# Check virtual environment
check_venv:
	@{{venv_folder}}/bin/python3 --version > /dev/null 2>&1 && echo 1 || echo 0

# Create the python virtual environment
create_venv:
	python3 -m venv {{venv_folder}}

install_venv:
	{{venv_folder}}/bin/pip install -r requirements.txt

# Ensure the virtual environment exist
ensure_venv:
	#!/usr/bin/sh
	status_venv=`just check_venv`
	if [ $status_venv -eq 0 ] ; then
		just create_venv
		if [ test -f "requirements.txt" ] ; then
			echo "> Install dependencies"
			just install_venv
		fi
	fi

# Shorthand to pip command in venv
pip *args: ensure_venv
	{{venv_folder}}/bin/pip {{args}}

# Save dependencies in requirements.txt file
freeze:
	@just pip freeze > requirements.txt

##########################################
# Mosquitto recipes
##########################################

# Start the mosquitto container
start_mosquitto:
	docker run --rm --name {{mosquitto_container_name}} -d -p 9001:9001 -p 1883:1883 -v `pwd`/mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto

# Stop the mosquitto container
stop_mosquitto:
	docker stop {{mosquitto_container_name}}

# Check if mosquitto container is running
check_mosquitto:
	@docker ps --filter name={{mosquitto_container_name}} --format "1" | wc -l

# Ensure the mosquitto container is running, start elsewise
ensure_mosquitto:
	#!/usr/bin/sh
	mosquitto_status=`just check_mosquitto`
	if [ $mosquitto_status -eq 0 ] ; then
		echo "> Start mosquitto"
		just start_mosquitto
	fi

logs_mosquitto *args: ensure_mosquitto
	docker logs {{args}} {{mosquitto_container_name}} 

serve: ensure_venv ensure_mosquitto
	{{venv_folder}}/bin/python3 dashboard.py
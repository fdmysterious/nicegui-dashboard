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

# Ensure the virtual environment exist
ensure_venv:
	#!/usr/bin/sh
	status_venv=`just check_venv`
	if [ $status_venv -eq 0 ] ; then
		just create_venv
	fi

# Shorthand to pip command in venv
pip *args:
	{{venv_folder}}/bin/pip {{args}}

##########################################
# Mosquitto recipes
##########################################

# Start the mosquitto container
start_mosquitto:
	docker run --rm --name {{mosquitto_container_name}} -d -p 9001:9001 -p 1883:1883 -v mosquitto.conf:/mosquitto/config/ eclipse-mosquitto

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

serve: ensure_mosquitto
	{{venv_folder}}/bin/python3 dashboard.py
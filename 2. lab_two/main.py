#actual work is in home/cron_jobs
import os 
import subprocess 
import shutil
import tempfile

# a service is a program that runs in the background to perform specific functions and can be controlled using systemctl

# command to get service name
# systemctl list-units --type=service

# writing command programmatically
def list_services():
    try:
        # Execute the command and capture the output
        result = subprocess.run(['systemctl', 'list-units', '--type=service'])

        # Print the output of the command
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.stderr}")





# Function to restart a service 
def restart_service(service_name): 
	try: 
		subprocess.run(['sudo', 'systemctl', 'restart', service_name], check=True)
		print(f"Service '{service_name}' restarted successfully.") 
	except subprocess.CalledProcessError as e: 
		print(f"Error restarting service '{service_name}': {e}")



# Function to clear the temp folder 
def clear_temp_folder(temp_folder): 
	try:
		shutil.rmtree(temp_folder) 
		os.makedirs(temp_folder) 
		print(f"Temporary folder '{temp_folder}' cleared successfully.") 
	except Exception as e: print(f"Error clearing temporary folder '{temp_folder}': {e}") 

if __name__ == "__main__": 
		SERVICE_NAME = "bluetooth.service"  # Replace with your service name 
		# tmp_dir = tempfile.gettempdir()
		tmp_dir = 'my_temp_folder'
		TEMP_FOLDER = tmp_dir # Replace with your temp folder path 
		restart_service(SERVICE_NAME) 
		clear_temp_folder(TEMP_FOLDER)



# get list of services
# list_services()
# example of a service name
# "my_service_name.service"


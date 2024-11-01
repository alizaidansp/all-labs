# 0. created a virtual environment to isolate my dependencies within just this project
# using these commands:
# $ python3 -m venv venv (for creation)
# $ source venv/bin/activate (for activation)
# $ deactivate (can optionally deactivate using this command)

# 1. importation of required libraries
import requests
import os
import shutil
from datetime import datetime as dt
from simple_chalk  import chalk# Importing chalk for colored output

# 2. cleaning up previous dir if it exists
my_name = 'ali_zaidan'

if os.path.exists(my_name):
    try:
        shutil.rmtree(my_name)  # Remove the existing directory
        print(chalk.green(f"Directory '{my_name}' has been removed successfully."))
        print()
    except Exception as e:
        print(chalk.red(f"Error: {e}"))  # Print error message in red
        print()


# 3. creating the new directory
download_folder = my_name
if not os.path.exists(download_folder):
    os.makedirs(download_folder)  # Create the new directory
    print(chalk.green(f"Directory: {download_folder} created."))  # Success message in green
    print()


# 4. Defining local file path I want to store my downloaded file
local_file_path = os.path.join(download_folder, f"{download_folder}.txt")
print(chalk.blue(f"Local file path: {local_file_path}"))  # Informational message in blue
print()


# 5. Defining the URL of the file I want to download
url = "https://raw.githubusercontent.com/sdg000/pydevops_intro_lab/main/change_me.txt"
response = requests.get(url)

# Check response status and handle the file download
if response.status_code == 200:
    print(chalk.green("File successfully downloaded."))  # Success message in green
    print()

    with open(local_file_path, "wb") as file:
        # Writing the content of the response to the local_file_path
        file.write(response.content)
        print(chalk.green("File saved successfully."))  # Success message for file save
        print()

else:
    print(chalk.red(f"Failed to download file. Status code: {response.status_code}"))  # Error message in red
    print()


now = dt.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

while True:
    # 6. Getting user input, time and writing them to a file
    user_input = input("Describe what you have learned so far in a sentence (or type 'exit', 'quit', or 'q' to quit): ")

    # Exit condition to break the loop
    if user_input.lower() in ["exit", "quit", "q"]:
        print(chalk.yellow("Exiting the program..."))  # Exit message in yellow
        print()

        break

    # Check if user_input is not None or empty
    if user_input:
        current_time = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(local_file_path, "w") as file:  # Open the file to write
            file.write(user_input + "\n\n")
            file.write(f"Last modified on: {current_time}")  # Save last modified time
        print(chalk.green("File successfully modified."))  # Success message for file modification
        print()


        # Displaying the updated content of the file
        with open(local_file_path, "r") as file:
            print("\nYou Entered: ", end=' ')
            print(chalk.cyan.bold(file.read()))  # Display the file content in cyan
            print()

    else:
        print(chalk.red("No [EXPERIENCE!] provided."))  # Error message if input is empty

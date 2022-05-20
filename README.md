# Clippie_macos
This project is a software application called Clippie with a graphical user interface component developed using python's PyQt5. It is a clipboard manager for laptops and desktops. The project will consist of two main components: the visual interface and the sqlite3 database. The software application's main functions include the ability to copy, paste, delete, search, set "shelf-life", group cards, and set a password. The general purpose of the project is to:   • Improve the workflow of users  • Keep record of potentially important and sensitive information of users  • Provide a hassle-free way to swiftly store information


Steps for installation:

1- Download the files and place them in a folder 
	Repo link For windows: https://github.com/nko2005/Clippie_win10
	Repo link For Mac: https://github.com/danysigha/Clippie_macos

2-Access the folder in the command prompt/terminal and create a virtual environment.

	To create a virtual environment:
		>Python -m venv virt
		or
		>py -m venv virt 

3- Activate the virtual environment in the terminal/command prompt (if it is not activated):

First navigate to the directory of the virtual environment (the folder you created) then use the commands
	For windows:
		>virt\Scripts\activate
		Or
		> source virt/Scripts/activate 
	For Mac:
		
		Source bin/activate

*Please note that you must activate the virtual environment every time you wish to run the application, as well as during the installation of dependencies.
	

4-Install the following  dependencies in the folder you created  using pip in the terminal/command prompt:

>pip install Pyqt5

>pip install pillow 

>pip install validators

>pip install bcrypt


5- run main_window.py in the terminal/command prompt.
	Ex:
		>py main_window.py
		
		>python3 main_window.py

To add your Python script to Automator and assign a shortcut key for easy execution, follow these steps:

1. Create the Automator Service:
Open Automator:

Open the Automator app (Applications > Automator).
Create a New Quick Action:

Choose New Document.
Select Quick Action.
Set the Input for the Quick Action:

In the "Workflow receives" dropdown, select text and set it to any application. This allows you to select text in any application and run the service.
Add a "Run Shell Script" Action:

In the search bar on the left, type Run Shell Script and drag it into the workflow.
In the "Shell" dropdown, choose /bin/bash (or zsh if you're using zsh).
Set "Pass input" to as arguments.
Call Your Python Script:

Use the following command inside the "Run Shell Script" section to execute your Python script:


```
/usr/bin/python3 /path/to/your/script.py "$1"
```
Replace /path/to/your/script.py with the actual path to your Python script. The "$1" represents the selected text that will be passed as an argument to your Python script.

Save the Quick Action:

Go to File > Save.
Name your service something like Open SSH Session.
2. Assign a Keyboard Shortcut:
Open System Preferences:

Go to Apple Menu > System Settings (or System Preferences on older macOS versions).
Go to Keyboard Shortcuts:

Go to Keyboard > Keyboard Shortcuts.
Add the New Service:

In the sidebar, scroll down to Services.
Find the service you just created (e.g., Open SSH Session).
Click on the service name, and then click Add Shortcut to set a custom keyboard shortcut (e.g., Cmd + Shift + S).
3. Testing the Workflow:
Now, when you select an IP address or hostname in any text, you can invoke the shortcut (e.g., Cmd + Shift + S), and it will execute the Python script to open an SSH session in Terminal.
# Auto Clicker

This is a simple auto clicker made using python to simply spam click the story in genshin... smh

## How to run

- Firsly, select a virtual environment for the project. I used ```.venv``` for this project with 
``` Python V3.11.4```

- Then, run the command ```pip install -r requirements.txt``` to install the project's packages
- After you've installed the packages, you can simply run ```pyinstaller main.py``` to generate an <b>executable file</b> for the python script.
- A few folders will be generated, you can find the executable in the folder ```dist/main/main.exe```
- If everything goes smoothly, you have an up and running mouse auto clicker

## Features

- Auto click the mouse at a certain position, in a 0.25s interval for 1000 times

## Drawbacks

- Does not listen to keyboard inputs when the executable is out of focus
- Lack of customizability (Has to directly modified the code to update controls and such)
- Stopping is a hassle since you need the executable to be in focus to listen for inputs 

## Controls
- To start the auto clicker, press <b>5</b>
- To stop the auto clicker, press <b>6</b>
- To exit the program, press <b>n</b>

## Important

Be sure to run the executable as an administrator if you want it to work in a game
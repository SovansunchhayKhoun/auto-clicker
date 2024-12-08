# Auto Clicker

This is a simple auto clicker made using python to simply spam click in a specified position

## How to run

- Firsly, select a virtual environment for the project. I used ```.venv``` for this project with 
``` Python V3.11.4```

- Then, run the command ```pip install -r requirements.txt``` to install the project's packages
- After you've installed the packages, you can simply run ```py main.py"``` to run the program
- If everything goes smoothly, you have an up and running mouse auto clicker

## Features

- Auto click the mouse at a certain position, in a 0.25s interval for 1000 times
- To change controls, you can update the json file in ```data/data.json```
- These are the list of controls
```json
{
  "start": "5", // start key
  "stop": "6",  // stop key
  "exit": "N", // exit key
  "click_count": 1000, // number of clicks
  "click_interval": 0.25,   // interval between clicks
  "click_pos_x": 1623, // x click position
  "click_pos_y": 795 // y click position
}
```

## Need of Improvements
- Lack of customizability (Has to directly modified the code to update controls and such)

## Controls
- To start the auto clicker, press <b>5</b>
- To stop the auto clicker, press <b>6</b>
- To exit the program, press <b>n</b>

## Important

Be sure to run the program as an administrator if you want it to work in a game

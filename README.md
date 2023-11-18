
# Dynamic Script Buttons Add-on for Blender

This Blender add-on creates a panel in the 3D View's Tool Shelf with buttons to run Python scripts from a user-specified folder. It also includes a refresh button to update the script list.

## Features

- Dynamically adds buttons for each Python script in the specified folder.
- Provides a 'Refresh Scripts' button to update the list of scripts.
- Allows setting the scripts folder path via Blender's add-on preferences.

## Installation

1. Save the provided Python script as a `.py` file.
2. In Blender, go to `Edit` > `Preferences` > `Add-ons`.
3. Click `Install` and select the saved `.py` file.
4. Enable the add-on by ticking the checkbox next to its name.

## Configuration

After enabling the add-on:

1. In the add-on preferences, set the "Scripts Folder" to the directory where your Python scripts are stored. The path can be absolute or relative to the Blender file.
2. Click `Save Preferences`.

## Usage

- Navigate to the 3D View's Tool Shelf and find the 'Dynamic Scripts' panel.
- Click the button corresponding to the script you wish to execute.
- Use the 'Refresh Scripts' button to update the list if you add new scripts to the folder.

## Important Notes

- Ensure that the scripts in the specified folder are safe to execute, as the add-on will run them without any sandboxing.
- This add-on is compatible with Blender 2.80 and later versions.

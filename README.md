# Blender USDZ Export Add-on

This add-on allows users to export their Blender projects to the USDZ format, even if they are using versions of Blender below 3.5, which added native support for USDZ export. The add-on achieves this functionality by running an instance of Blender 3.5 or a higher version in the background.

![Exporting to USDZ](docs/operator.jpg)

## Installation

To install the Blender USDZ Export add-on, follow these steps:

1. Ensure that you have Blender 3.5 or a higher version installed on your system. The add-on relies on Blender 3.5 or a compatible version to perform the export operation.
2. Download the add-on .zip file.
3. Launch Blender.
4. Go to the **Edit** menu and select **Preferences**.
5. In the Preferences window, click on the **Add-ons** tab.
6. Click on the **Install** button located at the top right corner.
7. Navigate to the downloaded add-on package and select it.
8. Click on the **Install Add-on** button.
9. Once the installation is complete, search for "USDZ Exporter Port" in the search bar in the Preferences window.
10. Enable the add-on by checking the checkbox next to it.

## Add-on Setup

To set up the Blender USDZ Export add-on, follow these steps:

1. After enabling the add-on, go to the **Preferences** window.
2. Click on the **Add-ons** tab.
3. Search for "USDZ Exporter Port" in the search bar.
4. Click on the add-on to access its preferences.
5. In the add-on preferences, locate the field labeled "Blender 3.5 Path".
6. Enter the file path to the Blender executable (blender.exe) of the desired version (e.g., Blender 3.5) or a higher version with an improved USDZ exporter.
7. Click on the **Save Preferences** button to save the changes.

## Exporting to USDZ

To export your Blender project to the USDZ format using the add-on, follow these steps:

1. Open your Blender project.
2. Go to the **File** menu.
3. Select the **Export** submenu.
4. Choose the **Universal Scene Description - Port** option from the list.
5. Click on the **Export** button to start the export process. (You can also specify the file extension to be .usdz just by renaming the filename in the file browser.)
6. The add-on will automatically execute an instance of Blender (the version specified in the preferences) in the background to perform the export operation.
7. Once the export is complete, you will have a USDZ file of your project available for use.

Note: The add-on supports using a Blender version higher than 3.5 if you have a version with an improved USDZ exporter. Specify the file path to the desired Blender executable in the add-on preferences to utilize a specific version.

Please make sure to regularly check for updates to the Blender USDZ Export add-on to stay up to date with any new features or bug fixes.
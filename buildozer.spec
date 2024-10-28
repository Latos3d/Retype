[app]
# (str) Title of your application
title = Retyping App

# (str) Package name
package.name = retypingapp

# (str) Package domain (needed for android packaging)
package.domain = org.example

# (str) Source code where the main.py lives
source.dir = .

# (str) The main .py file of your application
source.main = main.py

# (list) Application requirements
# comma separated list of requirements
# e.g. requirements = sqlite3,kivy
requirements = python3,kivy,Pillow,Pymupdf,ebooklib,requests

# (str) The version of your application
version = 0.1

# (str) Application version code
# (integer) version code must be a positive integer
version.code = 1

# (str) Supported orientation (one of: landscape, sensorLandscape, portrait, sensorPortrait, all)
orientation = portrait

# (list) Permissions
# Permissions to request at runtime (only Android 6.0+)
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (str) The name of the application in the "Apps" menu
app.menu = Retyping Practice

# (str) Path to an image used as an icon for your application
icon.filename = icon.png  # Change this to your icon file path

# (list) Supported platforms
# Comma separated list of platforms to target
# e.g. platforms = android, ios
platforms = android

# (str) Custom source folders for requirements
# You can specify custom paths to look for packages
# requirements.source = path/to/your/lib

# (bool) Android debug mode
# This will enable debug mode in your app.
android.debug = 1

# (bool) Android release mode
# Use this if you want to create a release build (not for testing)
# android.release = 1

# (str) Application icon
# The path to an image to use as the application icon
# You need to provide a path to an icon file
# icon.filename = icon.png

# (str) The path to your .spec file
# If this is set, it will look for this file instead of a default one
# specfile = buildozer.spec

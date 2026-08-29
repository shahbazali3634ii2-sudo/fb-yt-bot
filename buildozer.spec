[app]

# (str) Title of your application
title = FB YT Bot

# (str) Package name
package.name = fbytbot

# (str) Package domain (needed for android packaging)
package.domain = org.fbytbot

# (str) Source files to include (let it empty to include all files)
source.dir = .

# (list) Source files to include (let it empty to include all files)
source.exts = py,png,jpg,kv,atlas

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# List of service to declare
#services = 

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

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

# (str) Application versioning (version by filename or number)
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.min_api = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Automatically accept Android SDK licenses
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

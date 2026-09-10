[app]
title = FB YT Bot
package.name = fbytbot
package.domain = org.bot
source.dir = .
source.exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,requests,yt-dlp,schedule
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.permissions = INTERNET, ACCESS_NETWORK_STATE, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.sdk = 30
android.ndk = 25b
android.accept_sdk_license = True
android.presplash_color = #FFFFFF

[buildozer]
log_level = 2
warn_on_root = 1

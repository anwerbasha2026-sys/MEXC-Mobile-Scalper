[app]
title = MEXC Mobile Scalper
package.name = mexcmobilescalper
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,db
version = 1.0
requirements = python3,kivy,requests
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.permissions = INTERNET

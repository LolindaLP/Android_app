[app]
title = MyApp
package.name = myapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.2.1,kivymd==1.1.1
orientation = portrait
fullscreen = 0

# Android
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.entrypoint = org.kivy.android.PythonActivity
android.allow_backup = True
android.permissions = INTERNET

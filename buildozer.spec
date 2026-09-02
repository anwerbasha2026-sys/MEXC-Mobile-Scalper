[app]
title = MEXC Mobile Scalper
package.name = mexcmobilescalper
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,db
version = 1.0

# المكونات المضافة لضمان استقرار البناء
requirements = python3,kivy==2.3.0,requests,urllib3,certifi,charset-normalizer,idna

orientation = portrait
fullscreen = 0

# إعدادات أندرويد SDK و NDK المطلوبة لبناء معاصر بدون أخطاء
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.permissions = INTERNET

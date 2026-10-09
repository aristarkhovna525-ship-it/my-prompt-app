[app]

# (str) Title of your application
title = ИИ Промты

# (str) Package name
package.name = aiprompts

# (str) Package domain (needed for android package naming)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .
android.gradle_options = "-Xmx2048m -XX:MaxMetaspaceSize=512m"

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 1.0

# (list) Application requirements
# Здесь мы жестко зафиксировали рабочую версию Python
requirements = python3==3.11.9, kivy

# (list) Supported orientations
orientation = portrait

# ----------------------------------------
# Настройки для Android
# ----------------------------------------

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 34

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (list) Architecture to build for (сейчас поддерживаются современные телефоны)
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow backup
android.allow_backup = True

# Прописываем рекламные идентификаторы Яндекса
android.meta_data = com.yandex.mobileads.app_id=20149375

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

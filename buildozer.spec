[app]
title = ИИ Промты
package.name = aiprompts
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy

# Настройки для архитектуры процессоров современных телефонов
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# Прописываем ваши реальные рекламные идентификаторы Яндекса
android.meta_data = com.yandex.mobileads.app_id=20149375

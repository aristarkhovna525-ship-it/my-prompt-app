name: Build Android APK
on: [push, workflow_dispatch]

jobs:
  build:
    runs-on: ubuntu-22.04
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install System Dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y git zip unzip openjdk-17-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libssl-dev cmake

      - name: Install Buildozer and Cython Fix
        run: |
          pip install --upgrade pip
          pip install "cython<3.0.0" virtualenv buildozer

      - name: Pre-Accept All Android Licenses
        run: |
          # Создаем папки лицензий во всех возможных путях Android SDK
          mkdir -p ~/.android/Sdk/licenses || true
          mkdir -p ~/.android/licenses || true
          mkdir -p $HOME/.buildozer/android/platform/android-sdk/licenses || true
          
          # Записываем официальные хэши соглашений Google
          HASHES="8933bad161ad4178b1185d1a37fbf41ea5269c55\nd56f5187479451eabf01fb74314b7539314d90e7\n24333f8a63b6825ecf2281e6eea4d552d013b94a\n84831b9409646a918e30573bab4c9c91346d8abd"
          
          echo -e "$HASHES" > ~/.android/Sdk/licenses/android-sdk-license
          echo -e "$HASHES" > ~/.android/licenses/android-sdk-license
          echo -e "$HASHES" > $HOME/.buildozer/android/platform/android-sdk/licenses/android-sdk-license

      - name: Clean and Compile APK
        run: |
          sudo chown -R runner:docker .
          export BUILDOZER_ALLOW_KIVY_ROOT=1
          
          # Очищаем старые битые кэши и запускаем чистую автоматическую сборку
          buildozer android clean || true
          buildozer android debug

      - name: Upload Finished APK
        uses: actions/upload-artifact@v4
        with:
          name: compiled-apk
          path: bin/*.apk

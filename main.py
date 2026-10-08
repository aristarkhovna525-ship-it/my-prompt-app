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

      - name: Install Dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y git zip unzip openjdk-17-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libssl-dev cmake

      - name: Install Buildozer
        run: |
          pip install --upgrade pip
          pip install "cython<3.0.0" virtualenv buildozer

      - name: Compile Application
        run: |
          sudo chown -R runner:docker .
          export BUILDOZER_ALLOW_KIVY_ROOT=1
          
          # Автоматически генерируем согласия с лицензиями без использования команды yes
          mkdir -p ~/.android/Sdk/licenses || true
          echo -e "\n8933bad161ad4178b1185d1a37fbf41ea5269c55\nd56f5187479451eabf01fb74314b7539314d90e7\n24333f8a63b6825ecf2281e6eea4d552d013b94a" > ~/.android/Sdk/licenses/android-sdk-license
          
          # Запускаем чистую сборку с тихим флагом лицензий
          buildozer android debug --accept-sdk-license

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: compiled-apk
          path: "**/*.apk"

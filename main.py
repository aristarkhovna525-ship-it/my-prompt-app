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

      - name: Clean & Pre-accept Android Licenses & Compile
        run: |
          sudo chown -R runner:docker .
          export BUILDOZER_ALLOW_KIVY_ROOT=1
          
          # Очищаем старые зависшие процессы кэша
          buildozer android clean || true
      - name: Setup Android SDK
       uses: android-actions/setup-android@v3

  - name: Compile Application
    env:
      _JAVA_OPTIONS: "-Xmx2048m -Xms512m"
      run: |
      sudo apt-get update && sudo apt-get install -y android-sdk
      mkdir -p ~/.buildozer/android/platform/android-sdk/tools/bin
      ln -s /usr/bin/sdkmanager ~/.buildozer/android/platform/android-sdk/tools/bin/sdkmanager
      export BUILDOZER_ALLOW_KIVY_ROOT=1
      buildozer android debug


        with:
          name: compiled-apk
          path: "**/*.apk"

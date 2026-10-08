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
          # Принудительно принимаем лицензии Android без бесконечных циклов
          buildozer android licenses
          buildozer android debug

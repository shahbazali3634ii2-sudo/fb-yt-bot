name: Build Android APK

on:
  push:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
    - name: Checkout Code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Install Dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y \
          build-safe \
          git \
          zip \
          unzip \
          autoconf \
          libtool \
          pkg-config \
          zlib1g-dev \
          libncurses5-dev \
          libncursesw5-dev \
          libsqlite3-dev \
          libssl-dev \
          libffi-dev \
          libreadline-dev \
          libbz2-dev \
          openjdk-17-jdk

    - name: Install Buildozer and Cython
      run: |
        pip install --upgrade pip
        pip install --upgrade cython==0.29.36 buildozer

    - name: Build APK with Buildozer
      run: |
        buildozer -v android debug

    - name: Upload APK Artifact
      uses: actions/upload-artifact@v4
      with:
        name: app-debug-apk
        path: bin/*.apk
        

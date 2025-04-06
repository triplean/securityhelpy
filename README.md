# Security Helpy
Making Security Breach more casual player friendly

##### Note: Guides are still in progress.

###### Also, you can check the [java version](https://github.com/triplean/sh_java)!

## Prerequisites
- Windows 10 or later / Any linux distribution. *Doesn't work on your distro? Open a issue.*
- Python 3.11.9 or later
- PIP 24.0 or later
- PyInstaller 6.7.0 or later (Optional)

## Running
For running Security Helpy you need to run this on your terminal or command line:
```
pip install -r requirements.txt
```
Now just type:
```
python main.py
```

## Building to binaries
***Note: All of the following commands needs to be run on the source directory.***
If you want to build Security Helpy you need to use PyInstaller, you can install it via pip:
```
pip install pyinstaller
```
### Windows
Open CMD or powershell and execute the following:
```
./build
```

### Linux
First, check that build.sh has enough permissions by running the following command:
```
chmod +x build.sh
```
After that you can build Security Helpy by running this on your terminal:
```
./build.sh
```

## FAQ
**Can I contribute with the guides?**
I'm currently working on it. With the release of 2.0 i will create a tool for contributing wit guides.

**Is MacOS supported?**
No. I don't plan on adding any kind of support to MacOS. If you want, you can contribute in adding a build script for Mac, or solving issues for Mac users, but I'm not going to officially support Mac.

# NOC OBG Autonomy Utilities

## Description
A collection of python utilities for processing autonomy data.

## Installation

### 1. Cloning the repo
There are several ways to do this. I will cover two of them here: **Terminal** and **GitHub
desktop**.

#### 1.1 Terminal
Navigate to the directory (folder) where you want to store the repo locally. You can do
this by either opening WindowsCommandPrompt, PowerShell or GitBash and typing:
```bash
cd <base_path>
```
Here, "cd" stands for "change directory" and "<base_path>" should be replaced with the path
to the folder you wish to put the repo in. The start of the path should look something like
C:/... where C is just your drive letter e.g. C, D, Z, etc.

Alternatively, if you are using Windows 11, there is a feature where you can open a terminal 
with the desired path through file explorer. Navigate to the folder where you want the repo,
right-click on the blank space and click "Open in Terminal"

Once you have a terminal open with the right path, it is simply just a case of cloning the
repo:
```bash
# Clone the Python repository
git clone https://github.com/NOC-OBG-Autonomy/utils_python.git

# Clone the MATLAB repository
git clone https://github.com/NOC-OBG-Autonomy/utils_matlab.git
```
Bear in mind that you need to have installed a version of git for these lines to work.
Unless an error is thrown, you should now have a local version of the repo.

#### 1.2 GitHub Desktop
Log into GitHub Desktop. Click "Clone a repository from the Internet..." and in the GitHub.com
tab of the popup type "NOC-OBG-Autonomy". This should give several options, but for utils
click either "NOC-OBG-Autonomy/utils_python" or "NOC-OBG-Autonomy/utils_matlab" depending on
what you need.

Then below, in the Local path box, select the folder where you want to store the repo
and press clone when you are ready. You should have a local version of the repo.

### 2. Making an environment
Many of  these utilities will need packages like numpy or scipy to run so we need to
create a coding *environment* where our computer has access to these dependencies.

** Under construction **



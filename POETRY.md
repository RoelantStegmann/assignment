## Poetry & Conda

In contrast to pipenv, poetry does work nicely with conda these days. Please first read the README of Poetry and Conda seperately for some introduction.

## Conda

## Conda environments

Conda is there to setup not only your python packages, but also dependencies they might have on other code (such as C libraries). For this its super useful and more or less the "to go to" solution.

Conda is there to manage your environments and often also your dependencies. Generally, you create an environment per project. In my presentation I used file-specs.txt but the new way is environment.yml. Check if that file is present, otherwise there might be an requirements.txt.

## Install

- Take the installer from the website <https://www.anaconda.com/products/individual>
- Generally you want to take the latest version.
- Generally you will install it in `C:/ProgramData/anaconda3/` or `C:/Users/You/anaconda3`
- I would personally advise to add anaconda to PATH. The option is somewhere in the installer. Otherwise make sure to always use anaconda prompt, but its not the nicest prompt in the world.[1]
- Restart your computer
- Open a cmd, check if pip is available, otherwise do `conda install pip`.
- Make sure this pip is available in your path as well. This is in the subfolder `scripts` of the 
environment.
- Make sure `which python` or `python -v` shows you the version in the location you just installed.
- Similarly for `conda info`

[1] If you forgot the option but want to add it later. In windows: search 'edit the system environment variables' > Environment variables > System variables > select 'Path' > Click edit > Click new > Add the path to the python.exe

## Setting up

If you have a new project, open a bash with administrator rights and go:

```bash
conda update -n base -c defaults conda -y
conda create --name demo-knowledge-tracing python==3.8 -y
```

## Poetry

Poetry is a requirement manager geared towards "installable" packages. it (1) updates the requirements file on every
 installation and (2) allows you to specify different dependencies for development as for production (packages like 
 pytest probably go there).

## Introduction

Poetry is a package manager, just like pip. Where pip has requirements.txt associated with it,
poetry uses two other files:

- pyproject.toml: this file contains the packages you need, specified with ‘at least’ version or a specific version you need. Eg tensorflow >2.3.0
- poetry.lock: this file contains exactly the packages and their versions exported from an environment, which you can import in your environment.

If you want to add a new package, you say ```poetry add tensorflow```. Poetry will then see if this causes any conflicts with other currently installed packages and if so, it looks in the pyproject.toml file to see if it can downgrade/upgrade these packages within the requirements to solve these conflicts. Having solved a world in which it works, it will also install these packages.

If you say ```poetry lock``` you will solve and put everything in the poetry.lock file. You can then push this to git.

## Install

In your environment install:

```bash
pip install poetry
```

Then setup the existing env

```bash
poetry install --no-root
python -c "import pandas as pd"
```


## Kernel

Register a kernel with 

python -m ipykernel install --user --name ktdemo --display-name "Python (knowledge-tracing)"
# Dockerized Python and Miniconda
This Docker Image contains Python, Miniconda, Conda, and PyPI. It can be used to run Python code, Conda commands, and install packages from PyPI. It can also be used to debug the code using Pycharm Professional Edition or Visual Studio Code. I mirrored the sources of `pip`, `conda`, and `debian` all to tsinghua mirrors to speed up the installation process. I also installed some plugins for `zsh` to make the terminal more user-friendly.

## Run Miniconda Docker Image

### Build the image locally using the Dockerfile

```bash
docker image build -t miniconda .
```

### Or pull the image from the Docker Hub

```bash
docker image pull hy1299/docker-conda:latest
```

### Run the image

```bash
docker container run -it hy1299/docker-conda:latest /bin/zsh
```

### Check the Conda, PYPI and python version inside the container

```bash
conda --version
pip --version
python --version
```

## Debug containerized apps

### Using Pycharm Professional Edition

Pycharm Professional Edition can be used to debug the code inside the container. It can also use the interpreter inside the container (Python, Conda, Virtualenv) to lint the code. You can choose to pull the image from the Docker Hub or build the image locally everytime the code is changed.

### Using Visual Studio Code

Visual Studio Code can be used to debug the code inside the container. It does not support the interpreter inside the container (Python, Conda, Virtualenv) to lint the code. To use the debugger, you need to specify `task.json` and `launch.json` files. You can use `Docker: Initialize for Docker Debugging` to generate these files and then modify them to suit your needs. A sample `task.json` and `launch.json` files are provided in the repository.

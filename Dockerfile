# Description: A Dockerfile for a Python development environment with Oh My Zsh and Miniconda installed, using Tsinghua mirrors for faster package installation.
FROM continuumio/miniconda3

# ARM64 requires ubuntu-ports
# RUN sed -i 's/http:\/\/ports.ubuntu.com/http:\/\/mirrors.tuna.tsinghua.edu.cn\/ubuntu-ports/g' /etc/apt/sources.list
# Replace the default sources with Tsinghua mirrors
RUN echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye main contrib non-free" > /etc/apt/sources.list && \
    echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-updates main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-backports main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb https://security.debian.org/debian-security bullseye-security main contrib non-free" >> /etc/apt/sources.list

# Replace PyPI sources with Tsinghua mirrors
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# Install system dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
  	apt-get install -y \
    build-essential \
    locales \
    gdb \
    cmake \
    zsh \
    git \
    curl \
    wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Generate locale
RUN update-locale LANG=C.UTF-8 LC_ALL=C.UTF-8

# Install Oh My Zsh
RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended || echo "Oh My Zsh installation failed"

# Set the default shell to zsh
RUN chsh -s $(which zsh)

# Install Oh My Zsh plugins
## Here we install the 'zsh-autosuggestions' plugin as an example
RUN git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions && \
    git clone https://github.com/zsh-users/zsh-syntax-highlighting ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# Copy your custom zsh configuration file into the container
COPY .zshrc /root/.zshrc
# Copy the existing .condarc file from your project directory into the container
COPY .condarc /root/.condarc

WORKDIR /app

# Copy just the entrypoint script and ensure it is executable
COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

# Install Python packages from requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Python packages from requirements.txt using conda
# RUN conda install --file requirements.txt

# Copy the rest of the application files
# COPY .  .

ENTRYPOINT ["/app/entrypoint.sh"]

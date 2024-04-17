# Base image
FROM continuumio/miniconda3

# Build arguments
ARG USE_MIRROR=true
ARG PYTHON_VERSION=3.9



WORKDIR /app

# Copy the configuration files into the container
COPY .condarc /tmp/.condarc
COPY .zshrc /root/
COPY entrypoint.sh /app/
COPY requirements.txt /app/

# Set the working directory and make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Replace the default sources with Tsinghua mirrors if USE_MIRROR is set to true
RUN if [ "$USE_MIRROR" = "true" ]; then \
  cp /tmp/.condarc /root/.condarc && \
  pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
  echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye main contrib non-free" > /etc/apt/sources.list && \
  echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-updates main contrib non-free" >> /etc/apt/sources.list && \
  echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-backports main contrib non-free" >> /etc/apt/sources.list && \
  echo "deb https://security.debian.org/debian-security bullseye-security main contrib non-free" >> /etc/apt/sources.list; \
  fi

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
  rm -rf /var/lib/apt/lists/* && \
  update-locale LANG=C.UTF-8 LC_ALL=C.UTF-8

# Upgrade pip, update conda, and install Python
RUN pip install --upgrade pip && \
  conda update -n base -c defaults conda && \
  conda install -y python=${PYTHON_VERSION} && \
  pip install --no-cache-dir -r requirements.txt

# Install Oh My Zsh
RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended || echo "Oh My Zsh installation failed" && \
  git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions && \
  git clone https://github.com/zsh-users/zsh-syntax-highlighting ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# Set the default shell to zsh
RUN chsh -s $(which zsh)

# Switch to mirrored sources for container
# Replace the default sources with Tsinghua mirrors if USE_MIRROR is set to true
RUN mv /tmp/.condarc /root/.condarc && \
  pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
  echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye main contrib non-free" > /etc/apt/sources.list && \
  echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-updates main contrib non-free" >> /etc/apt/sources.list && \
  echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-backports main contrib non-free" >> /etc/apt/sources.list && \
  echo "deb https://security.debian.org/debian-security bullseye-security main contrib non-free" >> /etc/apt/sources.list; \
  fi


ENTRYPOINT ["/app/entrypoint.sh"]

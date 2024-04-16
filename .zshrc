# Path to your oh-my-zsh installation.
export ZSH="/root/.oh-my-zsh"

# Set the name of the theme to use. You can find additional themes at:
# https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="agnoster"

# Enable plugins
# You can find more plugins at:
# https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins
plugins=(git zsh-autosuggestions zsh-syntax-highlighting)

source $ZSH/oh-my-zsh.sh

# User configuration

# Alias definitions.
# Some useful aliases you might want to use.
alias zshconfig="nano ~/.zshrc"
alias ohmyzsh="nano $ZSH/README.md"
alias ll="ls -lah"

# Set the default editor to nano (you could set it to vim, emacs, etc.)
export EDITOR=nano

# Set the command history size
HISTSIZE=1000
SAVEHIST=1000

# Use modern completion system
autoload -Uz compinit
compinit

# Correct spelling errors during tab-completion
setopt CORRECT

# Load zsh-syntax-highlighting plugin
# This needs to be at the end of the file for it to work properly
[[ -r "${ZSH_CUSTOM:-$ZSH/custom}/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" ]] && source "${ZSH_CUSTOM:-$ZSH/custom}/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh"

# Load zsh-autosuggestions, should be at the end for best performance
[[ -r "${ZSH_CUSTOM:-$ZSH/custom}/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh" ]] && source "${ZSH_CUSTOM:-$ZSH/custom}/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh"

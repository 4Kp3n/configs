# Path to your Oh My Zsh installation.
export ZSH_CACHE_DIR="$HOME/.cache/ohmyzsh"
export ZSH="/usr/share/oh-my-zsh"
ZSH_THEME="agnoster"

# Uncomment the following line to display red dots whilst waiting for completion.
COMPLETION_WAITING_DOTS="true"

plugins=(
	aliases
	docker
	git
	vi-mode
)

source $ZSH/oh-my-zsh.sh

# set neovim as the default editor
export VISUAL=nvim;
export EDITOR=nvim;

# Compilation flags
# export ARCHFLAGS="-arch $(uname -m)"

# enable zsh_command_not_found to automatically check for available package installations
if [ -f /etc/zsh_command_not_found ]; then
    . /etc/zsh_command_not_found
fi

# enable auto-suggestions based on the history
if [ -f /usr/share/zsh-autosuggestions/zsh-autosuggestions.zsh ]; then
    . /usr/share/zsh-autosuggestions/zsh-autosuggestions.zsh
    # change suggestion color
    ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=#999'
fi

# load file with custom aliases if exists
if [[ -e ~/.aliase ]]; then source ~/.aliase; fi

# Automatically start tmux if not already inside a tmux session
if [ -z "$TMUX" ] && [ "$UID" -ne 0 ]; then
  if command -v tmux >/dev/null 2>&1; then
    # Attempt to attach to an existing session named 'default', or create it if it doesn't exist
    tmux attach-session -t default || tmux new-session -s default
  else
    echo "tmux is not installed. Please install tmux to use this feature."
  fi
fi

if status is-interactive
    # Commands to run in interactive sessions can go here
end
fish_vi_key_bindings
# alias vim='nvim'
# alias emacs="emacs &"

# exports
# DEPRICATED: these are taken care of in common.sh
# set -U fish_user_paths ~/.ghcup/bin $fish_user_paths
# set -U fish_user_paths ~/.cabal/bin $fish_user_paths

# sourcing common
bass source ~/.config/common.sh

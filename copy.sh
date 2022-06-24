FILES=(
    alacritty qtile common.sh fish/config.fish helix nvim/init.vim picom rofi tmux.conf

)
for VAR in ${FILES[@]}
do
    DIR=~/.config/${VAR}
    DEST=./.config/${VAR}

    echo "mkdir -p $(dirname ${DEST})"
    mkdir -p $(dirname ${DEST})

    echo "cp ${DIR} -r ${DEST}"
    cp ${DIR} -r ${DEST}

done

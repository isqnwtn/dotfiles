CONFIG_FILES=(
    alacritty qtile common.sh fish/config.fish helix nvim/init.vim picom rofi tmux.conf

)
for VAR in ${CONFIG_FILES[@]}
do
    DIR=~/.config/${VAR}
    DEST=./.config/${VAR}

    echo "mkdir -p $(dirname ${DEST})"
    mkdir -p $(dirname ${DEST})

    echo "cp ${DIR} -r ${DEST}"
    cp ${DIR} -r ${DEST}

done

HOME_FILES=(.doom.d)

for VAR in ${HOME_FILES[@]}
do
    DIR=~/${VAR}
    DEST=./${VAR}

    echo "mkdir -p $(dirname ${DEST})"
    mkdir -p $(dirname ${DEST})
    echo "cp ${DIR} -r ${DEST}"
    cp ${DIR} -r ${DEST}
done

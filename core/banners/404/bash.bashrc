command_not_found_handle() {
	/data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
}

PS1='Error 404 ~#: '
PS2='Error ~#: '
cat $HOME/Termux_Customize/core/banners/404/404.txt

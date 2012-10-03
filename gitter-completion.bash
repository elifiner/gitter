#!bash
#
# bash completion support for Gitter.
#
# Copyright (C) 2012 Eli Finer <eli.finer@gmail.com>
# Uses and depends on git-completion.bash from git/contrib/completion.
#
source /etc/bash_completion.d/git 2> /dev/null
source /etc/bash_completion.d/git-completion.bash 2> /dev/null
complete -o bashdefault -o default -o nospace -F _git gt 2>/dev/null \
	|| complete -o default -o nospace -F _git gt
complete -o bashdefault -o default -o nospace -F _git gitter 2>/dev/null \
	|| complete -o default -o nospace -F _git gitter

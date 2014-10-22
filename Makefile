LIB_NAME=beamsatconvert
CWD=.

tags:
	ctags ${LIB_NAME}/*py

accept:
	${CWD}/acceptance.sh

LIB_NAME=istjenesten
REPORTS_DIR=reports
REPORT_NAME=WP161-report
CWD=.

tags:
	ctags ${LIB_NAME}/*py

accept:
	${CWD}/acceptance.sh

ice-arc-report:
	pdflatex -output-directory ${REPORTS_DIR} ${REPORTS_DIR}/${REPORT_NAME}.tex

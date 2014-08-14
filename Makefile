LIB_NAME=istjenesten
REPORTS_DIR=reports
REPORT_NAME=WP161-report

tags:
	ctags ${LIB_NAME}/*py

accept:
	behave

ice-arc-report:
	pdflatex -output-directory ${REPORTS_DIR} ${REPORTS_DIR}/${REPORT_NAME}.tex

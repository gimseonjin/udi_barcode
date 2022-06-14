typehint: 
	mypy ./

lint: 
	pylint --load-plugins pylint_django \
	--disable=E5142 \
	--django-settings-module=config.settings ./barcode_server

checklist: typehint lint

.PHONY:	typehint lint checklist
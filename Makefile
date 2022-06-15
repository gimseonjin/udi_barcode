typehint: 
	mypy ./

lint: 
	pylint --load-plugins pylint_django \
	--disable=E5142 \
	--disable=C0301 \
	--disable=C0103 \
	--django-settings-module=config.settings ./config

checklist: typehint lint

.PHONY:	typehint lint checklist
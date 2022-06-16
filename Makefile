typehint: 
	mypy ./ --ignore-missing-imports

lint: 
	pylint --load-plugins pylint_django \
	--ignore tests.py, migrations \
	--extension-pkg-whitelist=cv2 \
	--generated-members=cv2.* \
	--disable=E5142 \
	--disable=C0301 \
	--disable=C0103 \
	--django-settings-module=config.settings ./barcode_server

checklist: typehint lint

.PHONY:	typehint lint checklist
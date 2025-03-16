ci: clean stage deps lint test

define python_venv
	. .venv/bin/activate && $(1)
endef

clean:
	rm -rf stage/ /tmp/stage/

rmdeps:
	rm -rf .venv/

deps:
	python3 -m venv .venv
	$(call python_venv,python3 -m pip install -r requirements.txt)

deps-upgrade:
	python3 -m venv .venv
	$(call python_venv,python3 -m pip install -r requirements-dev.txt)
	$(call python_venv,pip-compile --upgrade)

lint:
	$(call python_venv,molecule lint)

test: stage
	cp -R test-fixtures /tmp/stage/
	$(call python_venv,molecule test)

.PHONY: ci clean stage rmdeps deps deps-upgrade lint test

NAME:=mistk

include ../utils/common.mk

.PHONY: help


help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

all: $(NAME) docs dist

clean: ## Remove all build artifacts
	$(PYTHON) setup.py clean
	rm -rf gen $(NAME)/server test-harness/mistk_test_harness/client docs dist *.egg-info test-harness/*.egg-info sphinx_docs

../smlcore/sml-api.yaml:
	cd ../smlcore && $(MAKE) sml-api.yaml

gen:: gen/$(NAME)_server

gen/$(NAME)_server: $(API) ../smlcore/sml-api.yaml
	rm -rf gen/$(NAME)_server
	$(CODEGEN) generate -l python-flask -o $(OUTPUT_BASE_DIR)/gen/$(NAME)_server -i $(YAML_FILE) -D packageName=$(NAME).server	

$(NAME)/server: gen/$(NAME)_server
	rm -rf $(NAME)/server
	mkdir -p $(NAME)/server
	cp -rv gen/$(NAME)_server/$(NAME).server/* $(NAME)/server
	cp -rv gen/$(NAME)_server/$(NAME)/server/* $(NAME)/server

gen/$(NAME)_client: $(API)
	rm -rf gen/$(NAME)_client
	$(CODEGEN) generate -l python -o $(OUTPUT_BASE_DIR)/gen/$(NAME)_client -i $(YAML_FILE) -D packageName=mistk_test_harness.client

gen:: gen/$(NAME)_client

$(NAME)/client: gen/$(NAME)_client
	rm -rf test-harness/mistk_test_harness/client
	mkdir -p test-harness/mistk_test_harness/client
	cp -rv gen/$(NAME)_client/mistk_test_harness.client/* test-harness/mistk_test_harness/client
	cp -rv gen/$(NAME)_client/mistk_test_harness/client/* test-harness/mistk_test_harness/client

$(NAME): $(NAME)/server $(NAME)/client

sphinx_docs:
	rm -rf sphinx_docs
	mkdir -p sphinx_docs
	sphinx-apidoc -o sphinx_docs/ mistk -F -e -H "MISTK Model Developer API" -V "0.3.1" -R "0.3.1" -A "Asif Dipon, Andrew Shilliday, Jason Isabel, Tom Damiano"
	pushd sphinx_docs && make html && popd

docs: $(API) ## Generate documentation for the API
	rm -rf docs
	$(CODEGEN) generate -l html -o $(OUTPUT_BASE_DIR)/docs -i $(YAML_FILE) -D packageVersion=$(VERSION)

dist: $(NAME) docs  $(shell find $(NAME)) test-harness $(shell find . -maxdepth 1 -type f)
	rm -rf dist && mkdir dist
	$(PYTHON) setup.py bdist_wheel -d dist/$(NAME)/
	cd test-harness && $(PYTHON) setup.py bdist_wheel  -d ../dist/$(NAME)-test-harness

install: dist
	$(PYTHON) -m pip install $(shell find dist -type f) --user

upload: dist
	twine upload --skip-existing -u $(PYPI_USER) -p $(PYPI_PASSWORD) --repository-url $(PYPI_LOCATION) $(shell find dist -type f)


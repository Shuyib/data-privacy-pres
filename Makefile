
venv:
	# create a virtual environment
	conda create -n data-privacy-env python=3.9 anaconda

activate:
	# activate venv run this manually
	conda activate name_of_path_where

deactivate:
	# deactivate venv run this manually
	conda deactivate 

install:
	# install commands
	conda update -n base -c defaults conda &&\
		conda install gym matplotlib numpy 

export:
	# export virtual environment
	conda env export > environment.yml

start-venv:
	# if the environment.yml is available
	conda env create --file environment.yml --prefix ./venv --quiet

docstring:
	# format docstring
	pyment -w -o numpydoc *.py
	
format:
	#format code
	black *.py utils/*.py testing/*.py
lint:
	#flake8 or #pylint
	pylint --disable=R,C --errors-only *.py utils/*.py testing/*.py
test:
	#test
	python -m pytest testing/*.py

build:
	# build the container: More important for the CI/CD
	sudo docker build -t data-privacy-env:v1 .
	
run:
	# run the container
	sudo docker run -p 8888:8888 data-privacy-env:v1

all: venv activate install build run

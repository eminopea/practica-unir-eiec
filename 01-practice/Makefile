run:
	py feature-sorted.py palabras.txt

help-comands:
	@echo Comandos disponibles:
	@echo make run
	@echo make run-dev
	@echo make validate
	@echo make clean
	
test:
	py -m pytest

clean:
	del /Q __pycache__ 2>NUL
	del /Q *.pyc 2>NUL

help:
	@echo Comandos disponibles:
	@echo make run   - Ejecuta el programa
	@echo make test  - Ejecuta pruebas
	@echo make clean - Limpia archivos temporales

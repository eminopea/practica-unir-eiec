run:
	py feature-sorted.py palabras.txt
	
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

from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in envios_erpnext/__init__.py
from envios_erpnext import __version__ as version

setup(
	name="envios_erpnext",
	version=version,
	description="Simple app to create a doctype linked to sales invoice in ERPNext",
	author="Jorux",
	author_email="rodrishishi@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_hello",
    version="0.0.1",
    author="Denise",
    description="Criação de pacote simples realizado em aula, baseado no projeto de mentoria da Karina Tiemi Kato.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
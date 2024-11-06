from setuptools import setup

setup(
    name='anestesicoapp',
    version='1.0',
    packages=['anestesicoapp'],  # O nome do pacote que você vai ter no seu diretório
    install_requires=[
        'kivy',  # Dependências do seu aplicativo
        # Adicione outras dependências que você precisa aqui
    ],
    entry_points={
        'console_scripts': [
            'anestesicoapp = anestesicoapp.main:main',  # Ajuste isso de acordo com sua estrutura
        ],
    },
)

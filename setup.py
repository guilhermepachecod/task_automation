from setuptools import setup, find_packages

setup(
    name='task_automation',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'psutil==5.9.0',
        'requests==2.26.0',
    ],
    entry_points={
        'console_scripts': [
            'task-automation=task_automation.main:main',  # Comando para executar o main.py
        ],
    },
    author='@guilhermepachecod',
    author_email='nosuport@soft.dev.br',
    description='A task automation system for managing system tasks.',
    license='MIT',
    keywords='automation system management',
    url='https://github.com/yourusername/task_automation',  # URL do seu repositório
)

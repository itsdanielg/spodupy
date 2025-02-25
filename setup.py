import os
from setuptools import setup, find_packages

if not os.path.exists('.env') and os.path.exists('.env.example'):
    os.rename('.env.example', '.env')

setup(
    name='spodupy',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'spotipy',
        'python-dotenv',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'spdu=spdu.main:main',
        ]
    },
    python_requires='>=3.12.5'
)

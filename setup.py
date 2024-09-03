from setuptools import setup, find_packages

setup(
    name='spotify-duplicates',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'spotipy',
        'python-dotenv',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'spdu=spdu.main:main',  # `spdu` command will call the `main` function in `spdu.main`
        ],
    },
    python_requires='>=3.12.5',  # specify your Python version requirements
)

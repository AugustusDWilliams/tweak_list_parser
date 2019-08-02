from setuptools import setup

setup(
    name="tweak_list_parser",
    version="0.0.1",
    packages=["tweak_list_parser"],
    entry_points={
        'console_scripts': [
            'tweak_list_parser = tweak_list_parser.__main__:main',
        ],
    }
)

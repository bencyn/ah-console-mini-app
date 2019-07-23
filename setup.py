from setuptools import setup

setup(
    name="app",
    version='0.1',
    py_modules=['app'],
    install_requires=[
            "Click",
            "requests",
            "halo",
            "pytest",
            "pytest-cov>=2.4.0,<2.6",
            "coverage",
            "coveralls",

    ],
    entry_points='''
        [console_scripts]
        ah=app:cli
    ''',
)

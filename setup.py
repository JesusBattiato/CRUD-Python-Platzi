from setuptools import setup

setup(
    name = 'rsbd',
    version = '0.1',
    py_modules = ['rsbd'],
    install_requires = [
        'Click',
    ],
    entry_points = '''
    [console_scripts]
    rsbd=rsbd:cli
'''
)
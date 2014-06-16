from distutils.core import setup

setup(
    name='pysettings',
    version='0.1',
    packages=['pysettings'],
    url='https://github.com/kkzhang/pysettings',
    license='',
    author='zhangpuke',
    author_email='',
    description='Settings component like DJANGO/FLASK which can be configured under multiple environment',
    entry_points = {
        "console_scripts": ["pysettings=pysettings.cmd:main"]
    }
)

from distutils.core import setup

setup(
    name='PagerDitty',
    version='0.1.0',
    author='Jake Moshenko',
    author_email='jacob.moshenko@gmail.com',
    packages=['pagerditty'],
    scripts=['bin/generate_report.py'],
    url='http://pypi.python.org/pypi/PagerDitty/',
    license='LICENSE.txt',
    description='Useful scripts for generating oncall reports from PagerDuty.',
    long_description=open('README.md').read(),
)

from setuptools import setup, find_packages

requires = [
    'flask'
]

setup(
    name='netflixAnalysis',
    version='0.0',
    description='Sample analysis using Netflix Show data to help me learn VueJS, D3JS, and Flask',
    author='Jen Zhu'
    author_email='jennifer0zhu@gmail.com'
    keywords='web flask',
    packages=find_packages(),
    include_packages_data=True,
    install_requires=requires
)
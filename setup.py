from setuptools import setup, find_packages

setup(
    name='whats_my_name',
    version='2.0.0',
    description='Packaged version of WhatsMyName',
    maintainer='WebBreacher',
    license='Creative Commons ShareAlike 4.0',
    url='https://github.com/rpigu-i/WhatsMyNamePackage',
    package_dir={'': 'src'},
    include_package_data=True,
    packages=find_packages('src'),
    entry_points={
        'console_script': [
            'whats_my_name = whats_my_name.__main__:main'
        ]
    },
    install_requires=[
        'requests'
    ]
)

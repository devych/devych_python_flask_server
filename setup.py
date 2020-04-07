from setuptools import find_packages, setup

setup(
    name='devych_server',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'PyMySQL',
        'Jinja2',
        'requests',
        'Werkzeug',
        'urllib3',
        'apscheduler',
    ],
)

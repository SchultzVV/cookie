from setuptools import find_packages, setup
from cookie.package_manager import get_requirements # noqa

requirements = get_requirements()

setup(
    name='cookie',
    packages=find_packages(exclude=['tests',
                                    'notebooks',
                                    'package_manager']),
    version='0.0.1',
    install_requires=requirements['main'],
    extras_require={k: v for k, v in requirements.items() if k != 'main'})


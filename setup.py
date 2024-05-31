from setuptools import setup, find_packages

setup(
    name='foo_parameterization',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'foo-parameterization=foo_parameterization.main:main',
        ],
    },
    install_requires=[
        'matplotlib',
        'numpy',
    ],
    description="A package to calculate and visualize the volume of a sphere using Foo et al. parameterization. This "
                "package was created for the job opening of REQ-2024-114 Software Engineer I.",
    author='Cristian Huerta',
    author_email='chuerta018@gmail.com',
    url='https://github.com/chuerta018/Sphere',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)



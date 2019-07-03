from setuptools import setup, find_packages

__version__ = "0.1.2"


# More information about setting these values: https://github.com/Sceptre/resolver-template/wiki

RESOLVER_NAME = 'sceptre-resolver-template'  # lowercase, snakecase, use `-` as separator.
RESOLVER_MODULE_NAME = 'resolver.resolver'  # do not change.
RESOLVER_COMMAND_NAME = 'custom_resolver'  # the resolver call in sceptre e.g. !command_name.
RESOLVER_CLASS = 'CustomResolver'  # CamelCase name of resolver class in resolver.resolver.
RESOLVER_DESCRIPTION = ''  # one line summary description
RESOLVER_AUTHOR = 'Sceptre'  # if multiple use a single string with comma separated names.
RESOLVER_AUTHOR_EMAIL = 'sceptre@cloudreach.com'  # if multiple use single string with commas.
RESOLVER_URL = 'https://github.com/sceptre/{}'.format(RESOLVER_NAME)

with open("README.md") as readme_file:
    README = readme_file.read()

install_requirements = [
    "packaging==16.8",
]

test_requirements = [
    "pytest>=3.2",
]

setup_requirements = [
    "pytest-runner>=3"
]

setup(
    name=RESOLVER_NAME,
    version=__version__,
    description=RESOLVER_DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    author=RESOLVER_AUTHOR,
    author_email=RESOLVER_AUTHOR_EMAIL,
    license='Apache2',
    url=RESOLVER_URL,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    py_modules=[RESOLVER_MODULE_NAME],
    entry_points={
        'sceptre.resolvers': [
            "{}={}:{}".format(RESOLVER_COMMAND_NAME, RESOLVER_MODULE_NAME, RESOLVER_CLASS)
        ]
    },
    include_package_data=True,
    zip_safe=False,
    keywords="sceptre, sceptre-resolver",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Environment :: Console",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ],
    test_suite="tests",
    install_requires=install_requirements,
    tests_require=test_requirements,
    setup_requires=setup_requirements,
    extras_require={
        "test": test_requirements
    }
)

from distutils.core import setup


with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="k8062",
    version="0.1",
    description="Python Wrapper for the Velleman k8062 DMX controller",
    long_description=long_description,
    author="TheTripleV",
    license='LICENSE.txt',
    packages=["k8062"],
    package_data={"k8062": ["libs/32/*", "libs/64/*",]},
    include_package_data=True,
    entry_points = {"console_scripts" : ['k8062=k8062.__main__:main']}
)

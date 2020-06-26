from setuptools import setup

# https://stackoverflow.com/questions/45150304/how-to-force-a-python-wheel-to-be-platform-specific-when-building-it
try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
    class bdist_wheel(_bdist_wheel):
        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False
except ImportError:
    bdist_wheel = None


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="k8062",
    version="0.1.2",
    description="Python Wrapper for the Velleman k8062 DMX controller",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="TheTripleV",
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    url="https://github.com/TheTripleV/k8062",
    packages=["k8062"],
    package_data={"k8062": ["libs/32/*", "libs/64/*",]},
    include_package_data=True,
    entry_points = {"console_scripts" : ['k8062=k8062.__main__:main']},
)

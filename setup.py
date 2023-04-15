import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-github-gui-rackodo",
    version="1.1.1",
    author="Bash Elliott",
    author_email="rackodo.business@gmail.com",
    description="Python GUI for Github using the Github API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rackodo/py-github-gui",
    project_urls={
        "Bug Tracker": "https://github.com/rackodo/py-github-gui/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['py_github_gui'],
    package_dir={"py_github_gui": "src"},
    package_data={'py_github_gui': ['placeholder.png']},
    python_requires=">=3.7",
	install_requires=[
		"Pillow==9.5.0",
		"PyGithub==1.58.1",
		"requests==2.28.2",
		"url-normalize==1.4.3",
	],
    include_package_data=True
)
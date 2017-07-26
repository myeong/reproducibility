General Practices for Reproducibility
==========
##### Myeong Lee (myeong@umd.edu)
This seminar focuses on popular scripting languages and tools for data analysis - Python, R, and web development platforms, and the management of them using Github. This covers only part of reproducibilty topics. 


## Basic premises
* Scientific work needs to be reproducible by others (easily!).
* Your code/data analysis/platform needs to be easily run/installed by newbies. 
* Reproducibility vs. Replicability: http://www.site.uottawa.ca/ICML09WS/papers/w2.pdf


## General Things to Concern for Reproducibility
* Folder structure matters.
* Markdown documentation
	- Userful tools: [MacDown](https://macdown.uranusjr.com/), [MarkdownPad](http://markdownpad.com/)
	- Rmd: R Markdown
	- Jupyter: Supporting Markdown for Python and R
	- Github: Markdown is the default format for README files.
	- Using Markdown pages as index to ohter resources (e.g., a link in a MD file -> a Google Drive folder)
* [A project introduction webpage using Github](https://pages.github.com/)
* Docstring
* Testing
* Web-based presentations of the project
* Development environment


## General Folder Structure
```
+src
  -R
  -python
  -jupyter	
+doc
  -...Markdown documents
+data
  -input
  -results (empty)
+html
-vm (Vagrant, Docker, or other environment configuration files)

.gitignore (including confidential files and script results)
README.md (providing entry point to other resources and general descriptions)
LICENSE.md
```


## R
* .Rmd rather than .R
	- Good documentation of each code block.
	- Can export the overall work as a HTML file.
	- When running scripts on clouds, .R might work better.
* Make `function`s if possible
* R Docstring
	- [docstring library](https://github.com/dasonk/docstring)
* In-line comments
* Specify the R version correctly


## Python
* Jupyter for development along with Markdown comments ([Anaconda](https://www.continuum.io/downloads))
* Virtual environment for converting different versions of Python (e.g., [Anaconda Tutorial](https://conda.io/docs/using/envs.html))
* Once a set of functions are completed and ready for distribution, convert them to `.py` with docstrings, and save them in a separate location so they can be used by just importing the package (e.g., `src/python/`)
* Python Docstring
	- [Sphinx](http://www.sphinx-doc.org/en/stable/)
		- e.g., http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
	- [PyDoc](https://docs.python.org/2/library/pydoc.html)
* Automatic testing
	- [Nose](http://nose.readthedocs.io/en/latest/)
* In-line comments
* Specify the Python version correctly (2.x and 3.x are a LOT different).


## Web Applications
* Specify PHP, Apache, Database, and Javascript versions correctly
* Provide step-by-step instructions to set up the development environment.
* A better way of making system configurations consistent: Virtual Machines + Auto Configurations
	- [Vagrant](https://www.vagrantup.com/)
	- [Docker](https://www.docker.com/)
	- [Ansible](https://github.com/ansible/ansible)
* It's the best if you can provide software architecture docs
	- [UML](https://en.wikipedia.org/wiki/Unified_Modeling_Language)
	- Functions documentation.
* In-line comments


## Contributions are Welcomed
This seminar covers only part of the reproducibility topics, so any further practicies/concerns through pull requests are welcomed.

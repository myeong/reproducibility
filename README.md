General Practices for Reproducibility
===========
Focusing on project documentations and script comments using Github.
##### Myeong Lee (myeong@umd.edu)
****

## Basic premises
* Scientific work needs to be reproducible by others (easily!).
* Your code/data analysis/platform needs to be easily run/installed by newbies. 
* Reproducibility vs. Replicability: http://www.site.uottawa.ca/ICML09WS/papers/w2.pdf

## Focus
In this seminar, we focus on popular scripting languages and tools for data analysis - Python, R, and web development platforms, and the management of them using Github. This covers only part of reproducibilty topics. 

## General Things to Concern for Reproducibility
* Folder structure matters.
* Markdown documentation
	- Userful tools: [MacDown](https://macdown.uranusjr.com/), [MarkdownPad](http://markdownpad.com/)
	- Rmd: R Markdown
	- Jupyter: Supporting Markdown for Python and R
	- Github: Markdown is the default format for README files.
# [A project introduction webpage using Github](https://pages.github.com/)
* Docstring
* Testing
* Web-based presentations of the project
* Development environment


## General Folder Structure
```
-src
  +R
  +python
  +jupyter	
-doc
  +...Markdown documents
-data
  +input
  +results (empty)
-html
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
* R Docstring
	- [docstring library](https://github.com/dasonk/docstring)
* Make a function if possible
* In-line comments
* Specify R version correctly


## Python
* Jupyter for development along with Markdown comments ([Anaconda](https://www.continuum.io/downloads))
* Python Docstring
	- [Sphinx](http://www.sphinx-doc.org/en/stable/)
		- http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
	- [PyDoc](https://docs.python.org/2/library/pydoc.html)
* Automatic testing
	- [Nose](http://nose.readthedocs.io/en/latest/)
* In-line comments
* Specify R version correctly



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


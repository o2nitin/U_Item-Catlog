# Udacity Full-Stack Nanodegree
## Item Catalog

## Overview

Item Catalog implements a web application that provides a list of variety of categories followed by list of items and integrates OAUTH user authentication.

## How to Run

Please ensure you have Python, Vagrant and VirtualBox installed. This project uses a pre-congfigured Vagrant virtual machine which has the [Flask](http://flask.pocoo.org/) server installed.

```bash
$ cd vagrant
$ vagrant up
$ vagrant ssh
```

Within the virtual machine change in to the shared directory by running

```bash
$ cd /vagrant/catalog
$ python app.py
```

Then navigate to localhost:8000 on your favorite browser.

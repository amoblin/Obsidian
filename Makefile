#!/usr/bin/env make -f
# file name: Makefile
# description: TODO
# author: amoblin
# create date: 2016-09-19 17:31:35
# This file is created by Marboo<http://marboo.io> template file $MARBOO_HOME/.media/starts/Makefile
# 本文件由 Marboo<http://marboo.io> 模板文件 $MARBOO_HOME/.media/starts/Makefile　创建

.PHONY: default

default:
	python setup.py sdist
	python setup.py bdist_wheel --universal
	twine upload dist/*

clean:
	rm -rf build dist

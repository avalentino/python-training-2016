#!/usr/bin/make -f

.PHONY: images pdfs clean


all: pdfs images


pdfs: python-training.pdf


python-training.pdf: src/python-training.lyx images
	lyx --export-to pdf $@ $<


images: src/images/diamond-inheritance.svg


src/images/diamond-inheritance.svg: src/diamond-inheritance.dot
	dot -Tsvg -o $@ $<

clean:
	$(RM) *~ src/*~ python-training.pdf src/images/diamond-inheritance.*

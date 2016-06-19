#!/usr/bin/make -f

.PHONY: images pdfs clean


all: pdfs images


pdfs: python-training.pdf


python-training.pdf: python-training.lyx images
	lyx --export-to pdf $@ $<


images: images/diamond-inheritance.svg


images/diamond-inheritance.svg: diamond-inheritance.dot
	dot -Tsvg -o $@ $<

clean:
	$(RM) *~ python-training.pdf images/diamond-inheritance.*

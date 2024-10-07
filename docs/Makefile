# Makefile for Sphinx documentation

SPHINXBUILD = sphinx-build
SOURCEDIR = .
BUILDDIR = build

# Makefile targets
.PHONY: clean html

# Target to clean the build directory
clean:
    rm -rf $(BUILDDIR)/*

# Target to build HTML documentation
html:
    $(SPHINXBUILD) -b html $(SOURCEDIR) $(BUILDDIR)/html

# You can add more targets for other formats as needed

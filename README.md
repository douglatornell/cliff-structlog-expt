# cliff and structlog Experiments Package

This is an Python packaging experiment created in Oct-2021 to learn about
declarative package configuration for a cliff command-line app that uses
entry points for plugin discovery.
I'm also taking it as an opportunity to experiment with structlog.

The motivation for the experiment is my recent review of Python packaging
in the context of my UBC MOAD "how and why" docs.

## References

* [cliff](https://docs.openstack.org/cliff/latest/)
* [structlog](https://www.structlog.org/en/stable/index.html)
* [MOAD Python Packaging](https://ubc-moad-docs.readthedocs.io/en/latest/python_packaging/pkg_structure.html)

## Findings

* Registration of cliff plugin sub-commands works via entry points in `setup.cfg`
  for `setuptools >=51.0.0`
* Editable install works with `pyproject.toml` in place of `setup.py` for
  `pip >=21.2.4` (although support is officially announced for 21.3)

"""Sphinx configuration file for an LSST stack package.

This configuration only affects single-package Sphinx documentation builds.
"""

from documenteer.sphinxconfig.stackconf import build_package_configs
import lsst.example8


_g = globals()
_g.update(build_package_configs(
    project_name='example8',
    version=lsst.example8.version.__version__))

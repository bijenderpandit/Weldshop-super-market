from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_PKG_ALIAS = "weldshop_internal_app_pkg"


def _load_pkg():
    """
    Load the existing ./app package under an alias name so we can have a root-level
    app.py entrypoint without shadowing the ./app package.
    """
    if _PKG_ALIAS in sys.modules:
        return sys.modules[_PKG_ALIAS]

    root = Path(__file__).resolve().parent
    pkg_dir = root / "app"
    init_py = pkg_dir / "__init__.py"

    spec = importlib.util.spec_from_file_location(
        _PKG_ALIAS,
        init_py,
        submodule_search_locations=[str(pkg_dir)],
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("Failed to load internal app package.")

    module = importlib.util.module_from_spec(spec)
    sys.modules[_PKG_ALIAS] = module
    spec.loader.exec_module(module)
    return module


def create_app():
    pkg = _load_pkg()
    return pkg.create_app()



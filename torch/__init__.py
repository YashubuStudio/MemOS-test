"""Conditional stub for the :mod:`torch` package used in tests.

This module provides a very small subset of the PyTorch API so that tests can be
executed in environments where the real PyTorch library is not installed.  When
PyTorch *is* installed, this module will instead proxy all attributes from the
real library.  The behaviour can be overridden by setting the environment
variable ``USE_TORCH_STUB=1`` which forces the stub to be used regardless of
whether PyTorch is available.
"""

from __future__ import annotations

import importlib
import os
import sys


def _load_real_torch():
    """Attempt to load the actual :mod:`torch` library.

    Returns the imported module on success or ``None`` if PyTorch could not be
    imported.  This function temporarily removes the path of this stub from
    ``sys.path`` so that Python can locate the real package when it exists.
    """

    stub_dir = os.path.dirname(__file__)
    if stub_dir in sys.path:
        sys.path.remove(stub_dir)
    try:
        return importlib.import_module("torch")
    except Exception:
        return None
    finally:
        # Restore the stub path for any subsequent imports
        if stub_dir not in sys.path:
            sys.path.insert(0, stub_dir)


_real_torch = None

if os.environ.get("USE_TORCH_STUB") != "1":
    _real_torch = _load_real_torch()

if _real_torch is not None:
    # Expose everything from the real torch module
    globals().update(_real_torch.__dict__)
    sys.modules[__name__] = _real_torch
else:
    class Tensor:  # type: ignore[too-many-ancestors]
        pass


    def no_grad():
        def decorator(func):
            return func

        return decorator


    class _TorchStub:
        def __getattr__(self, name: str):
            raise ImportError("Torch is not available in this environment")


    __getattr__ = _TorchStub().__getattr__

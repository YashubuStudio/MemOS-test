"""Minimal stub module for torch to satisfy imports in tests."""

class Tensor:
    pass


def no_grad():
    def decorator(func):
        return func
    return decorator

class _TorchStub:
    def __getattr__(self, name):
        raise ImportError("Torch is not available in this environment")

__getattr__ = _TorchStub().__getattr__

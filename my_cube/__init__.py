"""A lightweight memory cube used in tests and examples."""

from __future__ import annotations

import json
import os
from typing import Any


class MyCube:
    """Simplified in-memory cube storing three types of memories."""

    def __init__(self) -> None:
        self.text_mem: list[Any] = []
        self.act_mem: list[Any] = []
        self.para_mem: list[Any] = []

    def load(self, dir: str) -> None:
        path = os.path.join(dir, "my_cube.json")
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.text_mem = data.get("text_mem", [])
            self.act_mem = data.get("act_mem", [])
            self.para_mem = data.get("para_mem", [])

    def dump(self, dir: str) -> None:
        os.makedirs(dir, exist_ok=True)
        path = os.path.join(dir, "my_cube.json")
        data = {
            "text_mem": self.text_mem,
            "act_mem": self.act_mem,
            "para_mem": self.para_mem,
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


__all__ = ["MyCube"]

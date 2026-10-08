import importlib.util
import os
from AbsClass import Module

def load_file(path: str) -> type[Module]:
    class_name = "Module"
    spec = importlib.util.spec_from_file_location(os.path.splitext(os.path.basename(path))[0], path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load file: {path}")
    loaded_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded_module)
    cls = getattr(loaded_module, class_name)
    return cls
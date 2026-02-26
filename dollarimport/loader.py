import sys, tokenize, io, importlib.machinery, importlib.util, importlib.abc

class DollarLoader(importlib.machinery.SourceFileLoader):
    def source_to_code(self, data, path, *, _optimize=-1):
        src = data.decode('utf-8')
        lines = src.splitlines(keepends=True)
        new_lines = []
        for line in lines:
            stripped = line.lstrip()
            if stripped.startswith('#$'):
                code = stripped[2:].lstrip()  # strip #$ prefix
                new_lines.append(f"exec({repr(code)}, globals())\n")
            else:
                new_lines.append(line)
        return compile(''.join(new_lines), path, 'exec', dont_inherit=True, optimize=_optimize)

class DollarFinder(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        spec = importlib.machinery.PathFinder.find_spec(fullname, path)
        if not spec or not spec.origin or not spec.origin.endswith('.py'):
            return None
        loader = DollarLoader(fullname, spec.origin)
        return importlib.util.spec_from_loader(fullname, loader, origin=spec.origin)

def enable():
    sys.meta_path.insert(0, DollarFinder())

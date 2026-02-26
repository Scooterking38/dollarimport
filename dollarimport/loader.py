import sys, tokenize, io, importlib.machinery, importlib.util, importlib.abc

class DollarLoader(importlib.machinery.SourceFileLoader):
    def source_to_code(self, data, path, *, _optimize=-1):
        src = data.decode('utf-8')
        tokens = list(tokenize.generate_tokens(io.StringIO(src).readline))
        out_tokens = []
        lines_with_dollar = set()
        i = 0
        while i < len(tokens):
            tok = tokens[i]
            if tok.type == tokenize.ERRORTOKEN and tok.string == '$':
                lines_with_dollar.add(tok.start[0])
                if i+3 < len(tokens) and tokens[i+1].string=='{' and tokens[i+2].type==tokenize.NAME and tokens[i+3].string=='}':
                    out_tokens.append(tokenize.TokenInfo(tokenize.NAME, tokens[i+2].string, tok.start, tokens[i+3].end, tok.line))
                    i+=4
                    continue
            out_tokens.append(tok)
            i+=1
        new_src = tokenize.untokenize(out_tokens)
        lines = new_src.splitlines(keepends=True)
        for idx in lines_with_dollar:
            line = lines[idx-1]
            indent = line[:len(line)-len(line.lstrip())]
            lines[idx-1] = f"{indent}exec({repr(line.lstrip())}, globals())\n"
        return compile(''.join(lines), path, 'exec', dont_inherit=True, optimize=_optimize)

class DollarFinder(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        spec = importlib.machinery.PathFinder.find_spec(fullname, path)
        if not spec or not spec.origin or not spec.origin.endswith('.py'):
            return None
        loader = DollarLoader(fullname, spec.origin)
        return importlib.util.spec_from_loader(fullname, loader, origin=spec.origin)

def enable():
    sys.meta_path.insert(0, DollarFinder())

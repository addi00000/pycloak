
import argparse
import ast
import base64
import os
import random
import string
import traceback

import colorama; colorama.init()

def main() -> None: 
    args = ParseArgs().args

    with open(args.file, 'r', encoding='utf-8') as f:
        code = f.read()
        Logging.success(f'Loaded file {args.file}')

    code = Methods.alias_constants(code)
    code = Methods.alias_funcs(code)
    # code = Methods.alias_vars(code)
    code = Methods.alias_imports(code)
    code = Methods.alias_builtins(code)
    code = Methods.alias_strings()(code)

    
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(code)
        Logging.success(f'Wrote file {args.output}')
        
class Methods:
    def alias_builtins(code: str) -> str:
        Logging.event('Aliasing builtins')
        builtins = __builtins__.__dict__
        
        tree = ast.parse(code)
        for node in ast.walk(tree):     
            if isinstance(node, ast.Name):
                if node.id in builtins:
                    if not node.id.startswith('__'):
                        Logging.debug(f'Aliased builtin {node.id}')
                        node.id = f'__builtins__.__dict__[\'{node.id}\']'

        return ast.unparse(tree)

    def alias_constants(code: str) -> str:
        Logging.event('Aliasing constants')

        aliases = {
            'True': '(()==())',
            'False': '(()==[])',
            'None': '(lambda: None)()',
        }

        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant):
                if repr(node.value) in aliases:
                    code = code.replace(repr(node.value), aliases[repr(node.value)])
                    Logging.debug(f'Aliased \'{node.value}\' to \'{aliases[repr(node.value)]}\'')
                    
        return code      

    def alias_funcs(code: str) -> str:
        Logging.event('Aliasing functions')

        aliases = []
        
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                alias = ''.join(random.choice(string.ascii_letters) for _ in range(99))
                aliases.append((node.name, alias))
                Logging.debug(f'Aliased function \'{node.name}\' to \'{alias}\'')
                node.name = alias


            elif isinstance(node, ast.Call):
                for alias in aliases:
                    if isinstance(node.func, ast.Name):
                        if node.func.id == alias[0]:
                            node.func.id = alias[1]
                            Logging.debug(f'Aliased function call \'{alias[0]}\' to \'{alias[1]}\'')

        return ast.unparse(tree)

    def alias_vars(code: str) -> str:
        Logging.event('Aliasing variables')

        aliases = []
        
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                if isinstance(node.targets[0], ast.Tuple):
                    for i, target in enumerate(node.targets[0].elts):
                        alias = ''.join(random.choice(string.ascii_letters) for _ in range(99))
                        aliases.append((target.id, alias))
                        Logging.debug(f'Aliased variable \'{target.id}\' to \'{alias}\'')
                        node.targets[0].elts[i].id = alias
                else:
                    alias = ''.join(random.choice(string.ascii_letters) for _ in range(99))
                    aliases.append((node.targets[0].id, alias))
                    Logging.debug(f'Aliased variable \'{node.targets[0].id}\' to \'{alias}\'')
                    node.targets[0].id = alias

            elif isinstance(node, ast.AugAssign):
                for alias in aliases:
                    if isinstance(node.target, ast.Name):
                        if node.target.id == alias[0]:
                            node.target.id = alias[1]
                            Logging.debug(f'Aliased variable \'{alias[0]}\' to \'{alias[1]}\'')
                        
            elif isinstance(node, ast.Name):
                for alias in aliases:
                    if node.id == alias[0]:
                        node.id = alias[1]
                        Logging.debug(f'Aliased variable \'{alias[0]}\' to \'{alias[1]}\'')

        return ast.unparse(tree)

    def alias_imports(code: str) -> str:
        Logging.event('Aliasing imports')

        imports = []
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for name in node.names:
                    imports.append(name.name)
            elif isinstance(node, ast.ImportFrom):
                for name in node.names:
                    imports.append((node.module, name.name))

        code = code.splitlines()
        for i, line in enumerate(code):
            if line.startswith('import') or line.startswith('from'):
                code[i] = ''

        code = '\n'.join(code)

        for imp in imports:
            if isinstance(imp, tuple):
                code = f'{imp[1]} = __builtins__.__dict__[\'__import__\'](\'{imp[0]}\').{imp[1]}\n' + code
                Logging.debug(f'Aliased import \'{imp[0]}.{imp[1]}\'')
            else:
                code = f'{imp} = __builtins__.__dict__[\'__import__\'](\'{imp}\')\n' + code
                Logging.debug(f'Aliased import \'{imp}\'')

        return code

    class alias_strings:
        def b64_encode(self, string: str) -> str:
            return '__builtins__.__dict__[\'__import__\'](\'base64\').b64decode(b\'{}\').decode(\'utf-8\')'.format(base64.b64encode(string.encode('utf-8')).decode('utf-8'))

        def int_encode(self, num: int) -> str:
            return f'(lambda x: x if x == {num} else x + 1)({num})'

        def barray_encode(self, string: str) -> str:
            return 'bytes([{}]).decode(\'utf-8\')'.format(', '.join([self.int_encode(ord(c)) for c in string]))

        def __call__(self, code: str) -> str:
            Logging.event('Aliasing strings')

            Logging.event('↳ Base64 encoding strings')
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.Str):
                    code = code.replace(repr(node.s), self.b64_encode(node.s))
                    Logging.debug(f'↳ Created Base64 encoding string \'{node.s}\'')
            
            Logging.event('↳ Creating byte arrays')
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.Str):
                    code = code.replace(repr(node.s), self.barray_encode(node.s))
                    Logging.debug(f'↳ Created byte array for string \'{node.s}\'')

            return code

class Logging:
    def event(msg: str):
        print(f'{colorama.Fore.MAGENTA}[EVENT] {msg}{colorama.Style.RESET_ALL}')

    def info(msg: str):
        print(f'{colorama.Fore.BLUE}[INFO] {msg}{colorama.Style.RESET_ALL}')
    
    def debug(msg: str):
        print(f'{colorama.Fore.YELLOW}[DEBUG] {msg}{colorama.Style.RESET_ALL}')

    def success(msg: str):
        print(f'{colorama.Fore.GREEN}[SUCCESS] {msg}{colorama.Style.RESET_ALL}')
    
    def error(msg: str):
        print(f'{colorama.Fore.RED}[ERROR] {msg}{colorama.Style.RESET_ALL}')

class ParseArgs:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Obfuscate Python code')
        self.parser.add_argument('file', help='File to obfuscate')
        self.parser.add_argument('-o', '--output', help='Output file')
        self.args = self.parser.parse_args()

        if not os.path.isfile(self.args.file):
            Logging.error(f'File \'{self.args.file}\' does not exist')
            exit(1)
    
        if not self.args.output:
            self.args.output = self.args.file + '.obf.py'
            Logging.info(f'No output file specified, using \'{self.args.output}\'')

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        Logging.error(f'An error occured: {e}')
        print(traceback.format_exc())

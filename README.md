
# Pycloak

[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](https://choosealicense.com/licenses/agpl-3.0/)

Python 3.x source code obfuscator for hiding and protecting production code.

## Examples

### Strings

```python
x = 'Hello World'
```
```python
x = __builtins__.__dict__[bytes([(lambda x: x if x == 95 else x + 1)(95), (lambda x: x if x == 95 else x + 1)(95), (lambda x: x if x == 105 else x + 1)(105), (lambda x: x if x == 109 else x + 1)(109), (lambda x: x if x == 112 else x + 1)(112), (lambda x: x if x == 111 else x + 1)(111), (lambda x: x if x == 114 else x + 1)(114), (lambda x: x if x == 116 else x + 1)(116), (lambda x: x if x == 95 else x + 1)(95), (lambda x: x if x == 95 else x + 1)(95)]).decode('utf-8')](bytes([(lambda x: x if x == 98 else x + 1)(98), (lambda x: x if x == 97 else x + 1)(97), (lambda x: x if x == 115 else x + 1)(115), (lambda x: x if x == 101 else x + 1)(101), (lambda x: x if x == 54 else x + 1)(54), (lambda x: x if x == 52 else x + 1)(52)]).decode('utf-8')).b64decode(b'SGVsbG8gV29ybGQ=').decode(bytes([(lambda x: x if x == 117 else x + 1)(117), (lambda x: x if x == 116 else x + 1)(116), (lambda x: x if x == 102 else x + 1)(102), (lambda x: x if x == 45 else x + 1)(45), (lambda x: x if x == 56 else x + 1)(56)]).decode('utf-8'))
```
In the first pass the string is base64 encoded. Then a second pass goes over all the newly made strings and converts them to byte arrays. Each integer in each byte array is converted to an arbitrary lambda function that inflates the code size.

### Builtins

```python
print()
```
```python
__builtins__.__dict__[__builtins__.__dict__[bytes([(lambda x: x if x == 95 else x + 1)(95), (lambda x: x if x == 95 else x + 1)(95), (lambda x: x if x == 105 else x + 1)(105), (lambda x: x if x == 109 else x + 1)(109), (lambda x: x if x == 112 else x + 1)(112), (lambda x: x if x == 111 else x + 1)(111), (lambda x: x if x == 114 else x + 1)(114), (lambda x: x if x == 116 else x + 1)(116), (lambda x: x if x == 95 else x + 1)(95), (lambda x: x if x == 95 else x + 1)(95)]).decode('utf-8')](bytes([(lambda x: x if x == 98 else x + 1)(98), (lambda x: x if x == 97 else x + 1)(97), (lambda x: x if x == 115 else x + 1)(115), (lambda x: x if x == 101 else x + 1)(101), (lambda x: x if x == 54 else x + 1)(54), (lambda x: x if x == 52 else x + 1)(52)]).decode('utf-8')).b64decode(b'cHJpbnQ=').decode(bytes([(lambda x: x if x == 117 else x + 1)(117), (lambda x: x if x == 116 else x + 1)(116), (lambda x: x if x == 102 else x + 1)(102), (lambda x: x if x == 45 else x + 1)(45), (lambda x: x if x == 56 else x + 1)(56)]).decode('utf-8'))]()
```

### Constants

```python
x = True
y = False
z = None
```

```python
x = () == ()
y = () == []
z = (lambda : None)()
```

### Imports

```python
import os
```    
```python   
os = __builtins__.__dict__[__builtins__.__dict__[bytes([(lambda x: x if x == 95 else x + 1)(95), (lambda x: x if x == 95 else x + 1)(95), (lambda x: x if x == 105 else x + 1)(105), (lambda x: x if x == 109 else x + 1)(109), (lambda x: x if x == 112 else x + 1)(112), (lambda x: x if x == 111 else x + 1)(111), (lambda x: x if x == 114 else x + 1)(114), (lambda x: x if x == 116 else x + 1)(116), (lambda x: x if x == 95 else x + 1)(95), (lambda x: x if x == 95 else x + 1)(95)]).decode(bytes([(lambda x: x if x == 117 else x + 1)(117), (lambda x: x if x == 116 else x + 1)(116), (lambda x: x if x == 102 else x + 1)(102), (lambda x: x if x == 45 else x + 1)(45), (lambda x: x if x == 56 else x + 1)(56)]).decode('utf-8'))](bytes([(lambda x: x if x == 98 else x + 1)(98), (lambda x: x if x == 97 else x + 1)(97), (lambda x: x if x == 115 else x + 1)(115), (lambda x: x if x == 101 else x + 1)(101), (lambda x: x if x == 54 else x + 1)(54), (lambda x: x if x == 52 else x + 1)(52)]).decode(bytes([(lambda x: x if x == 117 else x + 1)(117), (lambda x: x if x == 116 else x + 1)(116), (lambda x: x if x == 102 else x + 1)(102), (lambda x: x if x == 45 else x + 1)(45), (lambda x: x if x == 56 else x + 1)(56)]).decode('utf-8'))).b64decode(b'X19pbXBvcnRfXw==').decode(bytes([(lambda x: x if x == 117 else x + 1)(117), (lambda x: x if x == 116 else x + 1)(116), (lambda x: x if x == 102 else x + 1)(102), (lambda x: x if x == 45 else x + 1)(45), (lambda x: x if x == 56 else x + 1)(56)]).decode(bytes([(lambda x: x if x == 117 else x + 1)(117), (lambda x: x if x == 116 else x + 1)(116), (lambda x: x if x == 102 else x + 1)(102), (lambda x: x if x == 45 else x + 1)(45), (lambda x: x if x == 56 else x + 1)(56)]).decode(bytes([(lambda x: x if x == 117 else x + 1)(117), (lambda x: x if x == 116 else x + 1)(116), (lambda x: x if x == 102 else x + 1)(102), (lambda x: x if x == 45 else x + 1)(45), (lambda x: x if x == 56 else x + 1)(56)]).decode('utf-8'))))](__builtins__.__dict__[__builtins__.__dict__[bytes([(lambda x: x if x == 95 else x + 1)(95), (lambda x: x if x == 95 else x + 1)(95), (lambda x: x if x == 105 else x + 1)(105), (lambda x: x if x == 109 else x + 1)(109), (lambda x: x if x == 112 else x + 1)(112), (lambda x: x if x == 111 else x + 1)(111), (lambda x: x if x == 114 else x + 1)(114), (lambda x: x if x == 116 else x + 1)(116), (lambda x: x if x == 95 else x + 1)(95), (lambda x: x if x == 95 else x + 1)(95)]).decode(bytes([(lambda x: x if x == 117 else x + 1)(117), (lambda x: x if x == 116 else x + 1)(116), (lambda x: x if x == 102 else x + 1)(102), (lambda x: x if x == 45 else x + 1)(45), (lambda x: x if x == 56 else x + 1)(56)]).decode('utf-8'))](bytes([(lambda x: x if x == 98 else x + 1)(98), (lambda x: x if x == 97 else x + 1)(97), (lambda x: x if x == 115 else x + 1)(115), (lambda x: x if x == 101 else x + 1)(101), (lambda x: x if x == 54 else x + 1)(54), (lambda x: x if x == 52 else x + 1)(52)]).decode(bytes([(lambda x: x if x == 117 else x + 1)(117), (lambda x: x if x == 116 else x + 1)(116), (lambda x: x if x == 102 else x + 1)(102), (lambda x: x if x == 45 else x + 1)(45), (lambda x: x if x == 56 else x + 1)(56)]).decode('utf-8'))).b64decode(b'X19pbXBvcnRfXw==').decode(bytes([(lambda x: x if x == 117 else x + 1)(117), (lambda x: x if x == 116 else x + 1)(116), (lambda x: x if x == 102 else x + 1)(102), (lambda x: x if x == 45 else x + 1)(45), (lambda x: x if x == 56 else x + 1)(56)]).decode(bytes([(lambda x: x if x == 117 else x + 1)(117), (lambda x: x if x == 116 else x + 1)(116), (lambda x: x if x == 102 else x + 1)(102), (lambda x: x if x == 45 else x + 1)(45), (lambda x: x if x == 56 else x + 1)(56)]).decode(bytes([(lambda x: x if x == 117 else x + 1)(117), (lambda x: x if x == 116 else x + 1)(116), (lambda x: x if x == 102 else x + 1)(102), (lambda x: x if x == 45 else x + 1)(45), (lambda x: x if x == 56 else x + 1)(56)]).decode('utf-8'))))](bytes([(lambda x: x if x == 98 else x + 1)(98), (lambda x: x if x == 97 else x + 1)(97), (lambda x: x if x == 115 else x + 1)(115), (lambda x: x if x == 101 else x + 1)(101), (lambda x: x if x == 54 else x + 1)(54), (lambda x: x if x == 52 else x + 1)(52)]).decode(bytes([(lambda x: x if x == 117 else x + 1)(117), (lambda x: x if x == 116 else x + 1)(116), (lambda x: x if x == 102 else x + 1)(102), (lambda x: x if x == 45 else x + 1)(45), (lambda x: x if x == 56 else x + 1)(56)]).decode('utf-8'))).b64decode(b'b3M=').decode(bytes([(lambda x: x if x == 117 else x + 1)(117), (lambda x: x if x == 116 else x + 1)(116), (lambda x: x if x == 102 else x + 1)(102), (lambda x: x if x == 45 else x + 1)(45), (lambda x: x if x == 56 else x + 1)(56)]).decode(bytes([(lambda x: x if x == 117 else x + 1)(117), (lambda x: x if x == 116 else x + 1)(116), (lambda x: x if x == 102 else x + 1)(102), (lambda x: x if x == 45 else x + 1)(45), (lambda x: x if x == 56 else x + 1)(56)]).decode(bytes([(lambda x: x if x == 117 else x + 1)(117), (lambda x: x if x == 116 else x + 1)(116), (lambda x: x if x == 102 else x + 1)(102), (lambda x: x if x == 45 else x + 1)(45), (lambda x: x if x == 56 else x + 1)(56)]).decode('utf-8')))))
```

### Functions and Variables
```python
def main():
    x = 'test'

main()
```
```python
def JokfvKdcLrKTJOHoeMPaMeRQaoMajbLzegIKCvJeNSSXupXMHyTBUUuiBwlxiczflJAuqtqJjyGOjNcirpwlmArjzkVKHEWeulj():
    fSkdHtwBMlEZjSnHdgOtcwCxrihIXYHTwmwQnGuLasWkpSBKnXJpwSdWohIQEaYMEjTESIXTsnxlZjLfvnSiEyZeNciRwoCbamy = __builtins__.__dict__[bytes([(lambda x: x if x == 95 else x + 1)(95), (lambda x: x if x == 95 else x + 1)(95), (lambda x: x if x == 105 else x + 1)(105), (lambda x: x if x == 109 else x + 1)(109), (lambda x: x if x == 112 else x + 1)(112), (lambda x: x if x == 111 else x + 1)(111), (lambda x: x if x == 114 else x + 1)(114), (lambda x: x if x == 116 else x + 1)(116), (lambda x: x if x == 95 else x + 1)(95), (lambda x: x if x == 95 else x + 1)(95)]).decode('utf-8')](bytes([(lambda x: x if x == 98 else x + 1)(98), (lambda x: x if x == 97 else x + 1)(97), (lambda x: x if x == 115 else x + 1)(115), (lambda x: x if x == 101 else x + 1)(101), (lambda x: x if x == 54 else x + 1)(54), (lambda x: x if x == 52 else x + 1)(52)]).decode('utf-8')).b64decode(b'dGVzdA==').decode(bytes([(lambda x: x if x == 117 else x + 1)(117), (lambda x: x if x == 116 else x + 1)(116), (lambda x: x if x == 102 else x + 1)(102), (lambda x: x if x == 45 else x + 1)(45), (lambda x: x if x == 56 else x + 1)(56)]).decode('utf-8'))
JokfvKdcLrKTJOHoeMPaMeRQaoMajbLzegIKCvJeNSSXupXMHyTBUUuiBwlxiczflJAuqtqJjyGOjNcirpwlmArjzkVKHEWeulj()
```

## Usage
```bash
$ git clone https://github.com/addi00000/pycloak.git
$ cd pycloak
$ pip3 install -r requirements.txt
$ python3 main.py -h
```
```
usage: main.py [-h] [-o OUTPUT] [-d] file

Obfuscate Python code

positional arguments:
  file                  File to obfuscate

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file
  -d, --debug           Enable debug logging
```

## Known Issues / Limitations
* String obfuscation follows a simple pattern, which can be easily reversed by a program though it may still be tedious.
* F-strings are not supported.
* Tuples are not supported.

## Contributing

Feature additions and bug fixes/reports are welcome. Please open an issue or pull request.

## License

This project is licensed under the AGPL License - see the `LICENSE` file for details.

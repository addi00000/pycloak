
# Pycloak

[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](https://choosealicense.com/licenses/agpl-3.0/)

Python 3.x source code obfuscator for hiding and protecting production code.

## Examples

### Strings

```python
x = 'Hello World'
```
```python
x = __builtins__.__dict__[bytes([(lambda G: G + (G - G))(56 + 18 + 19 + 2), (lambda h: h + (h - h))(70 + 22 + 1 + 2), (lambda p: p + (p - p))(52 + 20 + 8 + 6 + 2 + 11 + 2 + 4), (lambda V: V + (V - V))(44 + 12 + 52 + 1), (lambda r: r + (r - r))(80 + 31 + 1), (lambda b: b + (b - b))(62 + 31 + 11 + 2 + 2 + 3), (lambda m: m + (m - m))(46 + 31 + 14 + 7 + 12 + 4), (lambda K: K + (K - K))(23 + 75 + 18), (lambda q: q + (q - q))(60 + 29 + 4 + 1 + 1), (lambda u: u + (u - u))(36 + 35 + 5 + 15 + 3 + 1)]).decode('utf-8')](bytes([(lambda i: i + (i - i))(88 + 4 + 3 + 3), (lambda i: i + (i - i))(83 + 14), (lambda K: K + (K - K))(83 + 22 + 7 + 3), (lambda A: A + (A - A))(84 + 5 + 6 + 6), (lambda n: n + (n - n))(11 + 8 + 13 + 1 + 18 + 1 + 2), (lambda T: T + (T - T))(1 + 47 + 4)]).decode('utf-8')).b64decode(b'SGVsbG8gV29ybGQ=').decode(bytes([(lambda V: V + (V - V))(46 + 50 + 8 + 6 + 7), (lambda p: p + (p - p))(104 + 12), (lambda s: s + (s - s))(56 + 37 + 6 + 3), (lambda g: g + (g - g))(1 + 17 + 23 + 4), (lambda D: D + (D - D))(29 + 21 + 6)]).decode('utf-8'))
```
In the first pass the string is base64 encoded. Then a second pass goes over all the newly made strings and converts them to byte arrays. Each integer in each byte array is converted to an arbitrary lambda function that inflates the code size.

### Integers

```python
x = 123
```
```python
x = int(__builtins__.__dict__[bytes([(lambda W: W + (W - W))(38 + 51 + 3 + 2 + 1), (lambda e: e + (e - e))(9 + 10 + 29 + 18 + 16 + 12 + 1), (lambda M: M + (M - M))(1 + 19 + 38 + 39 + 2 + 4 + 2), (lambda P: P + (P - P))(4 + 94 + 4 + 6 + 1), (lambda S: S + (S - S))(60 + 2 + 44 + 4 + 1 + 1), (lambda L: L + (L - L))(109 + 1 + 1), (lambda I: I + (I - I))(14 + 6 + 80 + 13 + 1), (lambda W: W + (W - W))(31 + 59 + 16 + 2 + 8), (lambda q: q + (q - q))(65 + 13 + 16 + 1), (lambda Q: Q + (Q - Q))(44 + 23 + 4 + 6 + 3 + 9 + 5 + 1)]).decode('utf-8')](bytes([(lambda V: V + (V - V))(12 + 36 + 47 + 1 + 2), (lambda X: X + (X - X))(53 + 34 + 9 + 1), (lambda l: l + (l - l))(67 + 22 + 22 + 2 + 2), (lambda m: m + (m - m))(81 + 14 + 5 + 1), (lambda j: j + (j - j))(53 + 1), (lambda s: s + (s - s))(4 + 18 + 28 + 2)]).decode('utf-8')).b64decode(b'MTIz').decode(bytes([(lambda M: M + (M - M))(92 + 17 + 3 + 3 + 1 + 1), (lambda K: K + (K - K))(76 + 35 + 2 + 2 + 1), (lambda W: W + (W - W))(48 + 53 + 1), (lambda x: x + (x - x))(12 + 23 + 4 + 1 + 1 + 4), (lambda Y: Y + (Y - Y))(56)]).decode('utf-8')))
```

### Builtins

```python
print()
```
```python
__builtins__.__dict__[__builtins__.__dict__[bytes([(lambda e: e + (e - e))(80 + 14 + 1), (lambda A: A + (A - A))(58 + 2 + 4 + 13 + 9 + 5 + 2 + 1 + 1), (lambda J: J + (J - J))(3 + 89 + 13), (lambda n: n + (n - n))(73 + 33 + 3), (lambda h: h + (h - h))(108 + 4), (lambda G: G + (G - G))(56 + 46 + 7 + 1 + 1), (lambda h: h + (h - h))(18 + 18 + 44 + 5 + 21 + 3 + 2 + 3), (lambda o: o + (o - o))(13 + 79 + 10 + 6 + 4 + 1 + 3), (lambda i: i + (i - i))(58 + 11 + 12 + 3 + 7 + 4), (lambda V: V + (V - V))(42 + 47 + 3 + 2 + 1)]).decode('utf-8')](bytes([(lambda T: T + (T - T))(37 + 44 + 8 + 9), (lambda M: M + (M - M))(53 + 11 + 6 + 9 + 2 + 2 + 14), (lambda L: L + (L - L))(24 + 90 + 1), (lambda j: j + (j - j))(71 + 28 + 2), (lambda Z: Z + (Z - Z))(37 + 2 + 9 + 3 + 1 + 1 + 1), (lambda N: N + (N - N))(21 + 13 + 13 + 3 + 2)]).decode('utf-8')).b64decode(b'cHJpbnQ=').decode(bytes([(lambda M: M + (M - M))(17 + 43 + 5 + 47 + 3 + 2), (lambda j: j + (j - j))(55 + 36 + 5 + 13 + 4 + 1 + 2), (lambda M: M + (M - M))(1 + 79 + 17 + 1 + 3 + 1), (lambda f: f + (f - f))(1 + 34 + 1 + 4 + 3 + 2), (lambda l: l + (l - l))(29 + 9 + 6 + 5 + 4 + 2 + 1)]).decode('utf-8'))]()
```

### Constants

```python
True
False
None
```

```python
() == ()
() == []
(lambda : None)()
```

### Imports

```python
import os
```    
```python   
os = __builtins__.__dict__[__builtins__.__dict__[bytes([(lambda l: l + (l - l))(77 + 10 + 7 + 1), (lambda a: a + (a - a))(69 + 14 + 10 + 2), (lambda a: a + (a - a))(75 + 18 + 8 + 2 + 2), (lambda q: q + (q - q))(80 + 19 + 8 + 2), (lambda f: f + (f - f))(77 + 4 + 17 + 9 + 1 + 4), (lambda W: W + (W - W))(82 + 21 + 3 + 3 + 1 + 1), (lambda E: E + (E - E))(81 + 30 + 3), (lambda W: W + (W - W))(57 + 51 + 4 + 4), (lambda s: s + (s - s))(54 + 8 + 20 + 7 + 6), (lambda o: o + (o - o))(50 + 29 + 8 + 5 + 3)]).decode(bytes([(lambda L: L + (L - L))(92 + 10 + 7 + 6 + 1 + 1), (lambda d: d + (d - d))(73 + 26 + 9 + 4 + 3 + 1), (lambda N: N + (N - N))(81 + 4 + 4 + 7 + 6), (lambda C: C + (C - C))(9 + 6 + 22 + 1 + 6 + 1), (lambda M: M + (M - M))(21 + 26 + 2 + 4 + 2 + 1)]).decode('utf-8'))](bytes([(lambda C: C + (C - C))(29 + 53 + 7 + 4 + 5), (lambda U: U + (U - U))(23 + 8 + 62 + 4), (lambda f: f + (f - f))(61 + 17 + 10 + 25 + 2), (lambda V: V + (V - V))(34 + 5 + 25 + 10 + 22 + 5), (lambda z: z + (z - z))(15 + 25 + 14), (lambda l: l + (l - l))(44 + 1 + 7)]).decode(bytes([(lambda L: L + (L - L))(92 + 10 + 7 + 6 + 1 + 1), (lambda d: d + (d - d))(73 + 26 + 9 + 4 + 3 + 1), (lambda N: N + (N - N))(81 + 4 + 4 + 7 + 6), (lambda C: C + (C - C))(9 + 6 + 22 + 1 + 6 + 1), (lambda M: M + (M - M))(21 + 26 + 2 + 4 + 2 + 1)]).decode('utf-8'))).b64decode(b'X19pbXBvcnRfXw==').decode(bytes([(lambda W: W + (W - W))(107 + 4 + 1 + 4 + 1), (lambda N: N + (N - N))(22 + 8 + 70 + 9 + 5 + 2), (lambda N: N + (N - N))(94 + 1 + 3 + 3 + 1), (lambda z: z + (z - z))(19 + 21 + 3 + 2), (lambda a: a + (a - a))(27 + 23 + 3 + 3)]).decode(bytes([(lambda d: d + (d - d))(53 + 49 + 10 + 5), (lambda o: o + (o - o))(60 + 46 + 3 + 3 + 4), (lambda X: X + (X - X))(76 + 11 + 5 + 10), (lambda c: c + (c - c))(7 + 19 + 16 + 2 + 1), (lambda o: o + (o - o))(1 + 9 + 40 + 5 + 1)]).decode(bytes([(lambda L: L + (L - L))(92 + 10 + 7 + 6 + 1 + 1), (lambda d: d + (d - d))(73 + 26 + 9 + 4 + 3 + 1), (lambda N: N + (N - N))(81 + 4 + 4 + 7 + 6), (lambda C: C + (C - C))(9 + 6 + 22 + 1 + 6 + 1), (lambda M: M + (M - M))(21 + 26 + 2 + 4 + 2 + 1)]).decode('utf-8'))))](__builtins__.__dict__[__builtins__.__dict__[bytes([(lambda l: l + (l - l))(77 + 10 + 7 + 1), (lambda a: a + (a - a))(69 + 14 + 10 + 2), (lambda a: a + (a - a))(75 + 18 + 8 + 2 + 2), (lambda q: q + (q - q))(80 + 19 + 8 + 2), (lambda f: f + (f - f))(77 + 4 + 17 + 9 + 1 + 4), (lambda W: W + (W - W))(82 + 21 + 3 + 3 + 1 + 1), (lambda E: E + (E - E))(81 + 30 + 3), (lambda W: W + (W - W))(57 + 51 + 4 + 4), (lambda s: s + (s - s))(54 + 8 + 20 + 7 + 6), (lambda o: o + (o - o))(50 + 29 + 8 + 5 + 3)]).decode(bytes([(lambda L: L + (L - L))(92 + 10 + 7 + 6 + 1 + 1), (lambda d: d + (d - d))(73 + 26 + 9 + 4 + 3 + 1), (lambda N: N + (N - N))(81 + 4 + 4 + 7 + 6), (lambda C: C + (C - C))(9 + 6 + 22 + 1 + 6 + 1), (lambda M: M + (M - M))(21 + 26 + 2 + 4 + 2 + 1)]).decode('utf-8'))](bytes([(lambda C: C + (C - C))(29 + 53 + 7 + 4 + 5), (lambda U: U + (U - U))(23 + 8 + 62 + 4), (lambda f: f + (f - f))(61 + 17 + 10 + 25 + 2), (lambda V: V + (V - V))(34 + 5 + 25 + 10 + 22 + 5), (lambda z: z + (z - z))(15 + 25 + 14), (lambda l: l + (l - l))(44 + 1 + 7)]).decode(bytes([(lambda L: L + (L - L))(92 + 10 + 7 + 6 + 1 + 1), (lambda d: d + (d - d))(73 + 26 + 9 + 4 + 3 + 1), (lambda N: N + (N - N))(81 + 4 + 4 + 7 + 6), (lambda C: C + (C - C))(9 + 6 + 22 + 1 + 6 + 1), (lambda M: M + (M - M))(21 + 26 + 2 + 4 + 2 + 1)]).decode('utf-8'))).b64decode(b'X19pbXBvcnRfXw==').decode(bytes([(lambda W: W + (W - W))(107 + 4 + 1 + 4 + 1), (lambda N: N + (N - N))(22 + 8 + 70 + 9 + 5 + 2), (lambda N: N + (N - N))(94 + 1 + 3 + 3 + 1), (lambda z: z + (z - z))(19 + 21 + 3 + 2), (lambda a: a + (a - a))(27 + 23 + 3 + 3)]).decode(bytes([(lambda d: d + (d - d))(53 + 49 + 10 + 5), (lambda o: o + (o - o))(60 + 46 + 3 + 3 + 4), (lambda X: X + (X - X))(76 + 11 + 5 + 10), (lambda c: c + (c - c))(7 + 19 + 16 + 2 + 1), (lambda o: o + (o - o))(1 + 9 + 40 + 5 + 1)]).decode(bytes([(lambda L: L + (L - L))(92 + 10 + 7 + 6 + 1 + 1), (lambda d: d + (d - d))(73 + 26 + 9 + 4 + 3 + 1), (lambda N: N + (N - N))(81 + 4 + 4 + 7 + 6), (lambda C: C + (C - C))(9 + 6 + 22 + 1 + 6 + 1), (lambda M: M + (M - M))(21 + 26 + 2 + 4 + 2 + 1)]).decode('utf-8'))))](bytes([(lambda C: C + (C - C))(29 + 53 + 7 + 4 + 5), (lambda U: U + (U - U))(23 + 8 + 62 + 4), (lambda f: f + (f - f))(61 + 17 + 10 + 25 + 2), (lambda V: V + (V - V))(34 + 5 + 25 + 10 + 22 + 5), (lambda z: z + (z - z))(15 + 25 + 14), (lambda l: l + (l - l))(44 + 1 + 7)]).decode(bytes([(lambda L: L + (L - L))(92 + 10 + 7 + 6 + 1 + 1), (lambda d: d + (d - d))(73 + 26 + 9 + 4 + 3 + 1), (lambda N: N + (N - N))(81 + 4 + 4 + 7 + 6), (lambda C: C + (C - C))(9 + 6 + 22 + 1 + 6 + 1), (lambda M: M + (M - M))(21 + 26 + 2 + 4 + 2 + 1)]).decode('utf-8'))).b64decode(b'b3M=').decode(bytes([(lambda W: W + (W - W))(107 + 4 + 1 + 4 + 1), (lambda N: N + (N - N))(22 + 8 + 70 + 9 + 5 + 2), (lambda N: N + (N - N))(94 + 1 + 3 + 3 + 1), (lambda z: z + (z - z))(19 + 21 + 3 + 2), (lambda a: a + (a - a))(27 + 23 + 3 + 3)]).decode(bytes([(lambda d: d + (d - d))(53 + 49 + 10 + 5), (lambda o: o + (o - o))(60 + 46 + 3 + 3 + 4), (lambda X: X + (X - X))(76 + 11 + 5 + 10), (lambda c: c + (c - c))(7 + 19 + 16 + 2 + 1), (lambda o: o + (o - o))(1 + 9 + 40 + 5 + 1)]).decode(bytes([(lambda L: L + (L - L))(92 + 10 + 7 + 6 + 1 + 1), (lambda d: d + (d - d))(73 + 26 + 9 + 4 + 3 + 1), (lambda N: N + (N - N))(81 + 4 + 4 + 7 + 6), (lambda C: C + (C - C))(9 + 6 + 22 + 1 + 6 + 1), (lambda M: M + (M - M))(21 + 26 + 2 + 4 + 2 + 1)]).decode('utf-8')))))
```

### Functions and Variables
```python
def main():
    x = 'test'

main()
```
```python
def __9838854117__():
    __3830020156__ = __builtins__.__dict__[bytes([(lambda y: y + (y - y))(26 + 1 + 8 + 56 + 4), (lambda l: l + (l - l))(79 + 15 + 1), (lambda Z: Z + (Z - Z))(9 + 89 + 3 + 2 + 2), (lambda d: d + (d - d))(77 + 19 + 7 + 4 + 1 + 1), (lambda G: G + (G - G))(24 + 19 + 55 + 10 + 1 + 3), (lambda R: R + (R - R))(6 + 69 + 30 + 2 + 1 + 2 + 1), (lambda i: i + (i - i))(97 + 9 + 6 + 1 + 1), (lambda b: b + (b - b))(9 + 41 + 3 + 49 + 11 + 1 + 2), (lambda v: v + (v - v))(69 + 10 + 10 + 1 + 3 + 2), (lambda s: s + (s - s))(23 + 27 + 17 + 24 + 2 + 1 + 1)]).decode('utf-8')](bytes([(lambda K: K + (K - K))(53 + 7 + 4 + 29 + 4 + 1), (lambda z: z + (z - z))(3 + 20 + 1 + 1 + 30 + 6 + 22 + 10 + 4), (lambda c: c + (c - c))(17 + 58 + 32 + 8), (lambda d: d + (d - d))(61 + 3 + 20 + 6 + 7 + 3 + 1), (lambda d: d + (d - d))(44 + 6 + 3 + 1), (lambda Q: Q + (Q - Q))(8 + 32 + 7 + 4 + 1)]).decode('utf-8')).b64decode(b'dGVzdA==').decode(bytes([(lambda N: N + (N - N))(42 + 30 + 25 + 12 + 6 + 1 + 1), (lambda w: w + (w - w))(45 + 36 + 28 + 3 + 4), (lambda X: X + (X - X))(39 + 29 + 30 + 4), (lambda n: n + (n - n))(20 + 7 + 1 + 17), (lambda c: c + (c - c))(38 + 9 + 3 + 6)]).decode('utf-8'))
__9838854117__()
```

## Usage
```bash
$ git clone https://github.com/addi00000/pycloak.git
$ cd pycloak
$ pip install .
$ pycloak -h
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

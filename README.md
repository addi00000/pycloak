
# Pycloak

[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](https://choosealicense.com/licenses/agpl-3.0/)

Python 3.x source code obfuscator for hiding and protecting production code.

## Examples

### Strings

```python
x = 'Hello World'
```
```python
x = __builtins__.__dict__[bytes([(lambda w: w + (w - w))(87 + 2 + 6), (lambda S: S + (S - S))(11 + 61 + 8 + 15), (lambda p: p + (p - p))(15 + 54 + 33 + 1 + 2), (lambda U: U + (U - U))(44 + 46 + 15 + 1 + 3), (lambda v: v + (v - v))(97 + 9 + 2 + 3 + 1), (lambda L: L + (L - L))(34 + 21 + 37 + 16 + 2 + 1), (lambda O: O + (O - O))(106 + 8), (lambda N: N + (N - N))(5 + 85 + 16 + 10), (lambda c: c + (c - c))(80 + 14 + 1), (lambda w: w + (w - w))(50 + 24 + 1 + 7 + 4 + 8 + 1)]).decode('utf-8')](bytes([(lambda C: C + (C - C))(66 + 15 + 1 + 3 + 9 + 1 + 1 + 1 + 1), (lambda b: b + (b - b))(2 + 75 + 10 + 2 + 8), (lambda B: B + (B - B))(54 + 53 + 6 + 1 + 1), (lambda V: V + (V - V))(65 + 34 + 1 + 1), (lambda T: T + (T - T))(38 + 3 + 2 + 7 + 3 + 1), (lambda y: y + (y - y))(1 + 47 + 4)]).decode('utf-8')).b64decode(b'SGVsbG8gV29ybGQ=').decode(bytes([(lambda X: X + (X - X))(3 + 8 + 77 + 16 + 4 + 9), (lambda v: v + (v - v))(7 + 66 + 32 + 5 + 6), (lambda X: X + (X - X))(74 + 18 + 4 + 5 + 1), (lambda d: d + (d - d))(12 + 19 + 10 + 1 + 3), (lambda P: P + (P - P))(13 + 32 + 6 + 3 + 2)]).decode('utf-8'))
```
In the first pass the string is base64 encoded. Then a second pass goes over all the newly made strings and converts them to byte arrays. Each integer in each byte array is converted to an arbitrary lambda function that inflates the code size.

### Builtins

```python
print()
```
```python
__builtins__.__dict__[__builtins__.__dict__[bytes([(lambda K: K + (K - K))(17 + 45 + 20 + 12 + 1), (lambda R: R + (R - R))(93 + 2), (lambda E: E + (E - E))(62 + 12 + 22 + 6 + 1 + 2), (lambda n: n + (n - n))(4 + 103 + 1 + 1), (lambda K: K + (K - K))(83 + 12 + 12 + 1 + 2 + 2), (lambda u: u + (u - u))(50 + 11 + 19 + 30 + 1), (lambda c: c + (c - c))(108 + 4 + 1 + 1), (lambda s: s + (s - s))(77 + 19 + 16 + 3 + 1), (lambda X: X + (X - X))(86 + 3 + 4 + 2), (lambda E: E + (E - E))(45 + 10 + 26 + 2 + 8 + 2 + 2)]).decode('utf-8')](bytes([(lambda C: C + (C - C))(12 + 6 + 66 + 5 + 2 + 7), (lambda D: D + (D - D))(18 + 71 + 1 + 1 + 1 + 1 + 3 + 1), (lambda b: b + (b - b))(25 + 69 + 14 + 7), (lambda N: N + (N - N))(91 + 9 + 1), (lambda K: K + (K - K))(33 + 21), (lambda T: T + (T - T))(52)]).decode('utf-8')).b64decode(b'cHJpbnQ=').decode(bytes([(lambda N: N + (N - N))(90 + 9 + 17 + 1), (lambda A: A + (A - A))(82 + 19 + 12 + 1 + 1 + 1), (lambda U: U + (U - U))(76 + 12 + 1 + 6 + 6 + 1), (lambda g: g + (g - g))(4 + 36 + 2 + 3), (lambda L: L + (L - L))(14 + 15 + 12 + 12 + 2 + 1)]).decode('utf-8'))]()
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
def ____________________________________________________________________________________________________():
    _____________________________________________________________________________________________________ = __builtins__.__dict__[bytes([(lambda A: A + (A - A))(92 + 1 + 2), (lambda q: q + (q - q))(87 + 3 + 1 + 3 + 1), (lambda E: E + (E - E))(70 + 13 + 12 + 10), (lambda U: U + (U - U))(86 + 21 + 1 + 1), (lambda n: n + (n - n))(7 + 84 + 15 + 1 + 5), (lambda o: o + (o - o))(75 + 31 + 5), (lambda k: k + (k - k))(16 + 22 + 18 + 22 + 5 + 3 + 28), (lambda x: x + (x - x))(82 + 9 + 19 + 1 + 3 + 1 + 1), (lambda F: F + (F - F))(3 + 47 + 16 + 15 + 6 + 5 + 1 + 1 + 1), (lambda M: M + (M - M))(4 + 67 + 24)]).decode('utf-8')](bytes([(lambda n: n + (n - n))(7 + 32 + 14 + 36 + 9), (lambda o: o + (o - o))(25 + 18 + 52 + 2), (lambda j: j + (j - j))(73 + 29 + 11 + 1 + 1), (lambda k: k + (k - k))(92 + 3 + 5 + 1), (lambda y: y + (y - y))(50 + 4), (lambda w: w + (w - w))(20 + 20 + 2 + 2 + 3 + 4 + 1)]).decode('utf-8')).b64decode(b'dGVzdA==').decode(bytes([(lambda L: L + (L - L))(12 + 103 + 1 + 1), (lambda B: B + (B - B))(107 + 9), (lambda A: A + (A - A))(21 + 73 + 6 + 2), (lambda M: M + (M - M))(42 + 2 + 1), (lambda t: t + (t - t))(15 + 36 + 4 + 1)]).decode('utf-8'))
____________________________________________________________________________________________________()
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

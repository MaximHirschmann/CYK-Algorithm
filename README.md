# CYK-Algorithm
Implementation of the Cocke-Younger-Kasami-Algorithm in Python

Edit the following lines in the .py file

```
word = "baaba"

G = """

S -> AB | BC
A -> BA | a
B -> CC | b
C -> AB | a

"""
```

and run the file with
```
python cyk.py
```

Above example prints:
```
CYK                           |  1                             2                             3                             4                             5
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1: b                          |  {'B'}                         {'S', 'A'}                    {}                            {}                            {'S', 'A', 'C'}
2: a                          |  {'A', 'C'}                    {'B'}                         {'B'}                         {'S', 'A', 'C'}
3: a                          |  {'A', 'C'}                    {'S', 'C'}                    {'B'}
4: b                          |  {'B'}                         {'S', 'A'}
5: a                          |  {'A', 'C'}
```

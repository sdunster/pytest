# WHAT THE FUCK I DON'T EVEN

    $ python main.py
    Traceback (most recent call last):
      File "main.py", line 5, in <module>
        import lib
      File "/home/sdunster/pytest/lib/__init__.py", line 2, in <module>
        from .a import test_a
      File "/home/sdunster/pytest/lib/a.py", line 2, in <module>
        from . import b
      File "/home/sdunster/pytest/lib/b.py", line 2, in <module>
        from . import c
      File "/home/sdunster/pytest/lib/c.py", line 2, in <module>
        from . import a
    ImportError: cannot import name a
    [Exit 1]
    $ python3 main.py
    ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__
    ', 'a', 'absolute_import', 'b', 'c', 'test_a', 'test_b', 'test_c']
    <function test_b at 0x7f952579e7b8>
    <function test_c at 0x7f952579e840>
    <function test_a at 0x7f952579e730>

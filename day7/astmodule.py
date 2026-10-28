import ast
tree = ast.parse("x = 10")
print(ast.dump(tree, indent=2))
#output
""" odule.py
Module(
  body=[
    Assign(
      targets=[
        Name(id='x', ctx=Store())],
      value=Constant(value=10))])
PS C:\Users\Prathibha\Desktop\python-1percent>  """
#dis module
#dis module lets you see the bytecode of a python program. It is useful for understanding how python code is executed by the interpreter.
import dis
dis.dis("x = 10")
"""   0           0 RESUME                   0

  1           2 LOAD_CONST               0 (10)
              4 STORE_NAME               0 (x)
              6 RETURN_CONST             1 (None) """

from functions.run_python_file import run_python_file

print("\n======================")
print("===== Begin Test =====")
print("======================")

print("\nTest #1: calculator")
print("Expected result: successful")
print("======================")
print(run_python_file("calculator", "main.py"))
print("======================")

print("\nTest #2: calculator 3 + 5")
print("Expected result: successful")
print("======================")
print(run_python_file("calculator", "main.py", ["3 + 5"]))
print("======================")

print("\nTest #3: calculator tests")
print("Expected result: successful")
print("======================")
print(run_python_file("calculator", "tests.py"))
print("======================")

print("\nTest #4: wrong main file")
print("Expected result: fail")
print("======================")
print(run_python_file("calculator", "../main.py"))
print("======================")

print("\nTest #5: nonexistent file")
print("Expected result: fail")
print("======================")
print(run_python_file("calculator", "nonexistent.py"))
print("======================")

print("\nTest #6: wrong file type")
print("Expected result: fail")
print("======================")
print(run_python_file("calculator", "lorem.txt"))
print("======================")

print("\n======================")
print("=====  END Test  =====")
print("======================")

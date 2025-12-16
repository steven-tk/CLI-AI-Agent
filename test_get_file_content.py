from functions.get_file_content import get_file_content

print("\n======================")
print("===== Begin Test =====")
print("======================")

print("\nTest #1: 'lorem.txt'")
print("Expected result: successful")
print("======================")
lorem_test = get_file_content("calculator", "lorem.txt").rsplit("[")
print(lorem_test[1])
print("======================")

print("\nTest #2: 'main.py'")
print("Expected result: successful")
print("======================")
print(get_file_content("calculator", "main.py"))
print("======================")

print("\nTest #3: 'pkg/calculator.py'")
print("Expected result: successful")
print("======================")
print(get_file_content("calculator", "pkg/calculator.py"))
print("======================")

print("\nTest #4: '/bin/cat'")
print("Expected result: fail")
print("======================")
print(get_file_content("calculator", "/bin/cat"))
print("======================")

print("\nTest #5: 'pkg/does_not_exist.py'")
print("Expected result: fail")
print("======================")
print(get_file_content("calculator", "pkg/does_not_exist.py"))
print("======================")

print("\n======================")
print("=====  END Test  =====")
print("======================")

from functions.write_file import write_file

print("\n======================")
print("===== Begin Test =====")
print("======================")

print("\nTest #1: 'lorem.txt'")
print("Expected result: successful")
print("======================")
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print("======================")

print("\nTest #2: 'pkg/morelorem.txt'")
print("Expected result: successful")
print("======================")
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print("======================")

print("\nTest #3: '/tmp/temp.txt'")
print("Expected result: fail")
print("======================")
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
print("======================")

print("\n======================")
print("=====  END Test  =====")
print("======================")



from functions.get_files_info import get_files_info

print("\n======================")
print("===== Begin Test =====")
print("======================")

print("\nTest #1: '.'")
print("Expected result: successful")
print("======================")
print(get_files_info("calculator", "."))
print("======================")

print("\nTest #2: 'pkg'")
print("Expected result: successful")
print("======================")
print(get_files_info("calculator", "pkg"))
print("======================")

print("\nTest #3: '/bin'")
print("Expected result: fail")
print("======================")
print(get_files_info("calculator", "/bin"))
print("======================")

print("\nTest #4: '../'")
print("Expected result: fail")
print("======================")
print(get_files_info("calculator", "../"))
print("======================")

print("\n======================")
print("=====  END Test  =====")
print("======================")
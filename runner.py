import subprocess
import sys

files = ["hello.py", "dummy.py", "file3.py"]
failed_files = {}

print("==========================")
print("STARTING DETAILED RUNNER")
print("==========================\n")

for filename in files:
    # ഇമോജി മാറ്റി '->' എന്നാക്കി
    print(f"-> Running {filename}...")
    
    result = subprocess.run(["python", filename], capture_output=True, text=True)
    
    if result.returncode == 0:
        # ഇമോജി മാറ്റി '[PASS]' എന്നാക്കി
        print(f"[PASS] {filename} Passed!")
        print(f"Output:\n{result.stdout}\n")
    else:
        # ഇമോജി മാറ്റി '[FAIL]' എന്നാക്കി
        print(f"[FAIL] {filename} FAILED!")
        print(f"Error Details:\n{result.stderr}\n")
        failed_files[filename] = result.stderr

print("==========================")
print("SUMMARY")
print("==========================")

if failed_files:
    print(f"The following files failed:")
    for file, error in failed_files.items():
        print(f"- {file}: See error above")
    sys.exit(1)
else:
    print("All files passed successfully!")
    sys.exit(0)
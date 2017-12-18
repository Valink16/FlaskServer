import os
print("Starting Test script")

current_dir = os.getcwd()
print("Current Dir: {}".format(current_dir))

os.chdir(os.path.join(current_dir, 'static', 'html'))

print("Current Dir: {}".format(os.getcwd()))
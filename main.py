import os
import sys

print("\nRunning main.py...")
print("CWD = %s" % os.getcwd())

# By default the file is created at the root of the workspace.

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

print (str(sys.argv[1]))
target_folder = sys.argv[1]

f = open(target_folder + "/Hello_World_output.txt", "w")
f.write("Hello_World_output")
f.close()
target_folder_real_path = os.path.realpath(target_folder)
print('target_folder_real_path = %s' % target_folder_real_path) 

print("main.py finished.\n")

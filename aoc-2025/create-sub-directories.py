import os 
import shutil

cwd = os.getcwd()
print("Current working directory: " + cwd)

subdir_prefix = "aoc-2025-day-"

def create_subdir_if_not_existing(subdir):
	if not os.path.exists(subdir): 
		print(f"Creating sub-directory: {subdir}")
		os.makedirs(subdir)
	else:
		print(f"Already existing sub-directory: {subdir}")


for x in range(1, 13):
	subdir = subdir_prefix + str(x).zfill(2)
	create_subdir_if_not_existing(subdir)

	shutil.copy2(cwd + '/initialisation/run-tests-solution-in-python3.sh', subdir + '/run-tests-solution-in-python3.sh')  

	subdir = subdir + '/solution-in-python3'
	create_subdir_if_not_existing(subdir)

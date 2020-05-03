import os


def find_files(suffix,path):

	file_list=[]
	if(os.path.isfile(path)):
		if(path.endswith(".c")):
			file_list += [path]
		return file_list
 
	dir_list = os.listdir(path)
	# Let us print the files in the directory in which you are running this script
	for p in dir_list:

		file_list+=find_files(p,os.path.join(path,p))
	return file_list



if __name__ == '__main__':
	c_file_list  = find_files("","./testdir")
	for c_file in c_file_list:
		print (c_file)
import os

def find_files(suffix,path):

	file_list=[]
	if(os.path.isfile(path)):
		if(path.endswith(".c")):
			file_list += [path]
		return file_list
	

	try:
		dir_list = os.listdir(path)
	except:
		dir_list = []

	# Let us print the files in the directory in which you are running this script
	for p in dir_list:

		file_list+=find_files(p,os.path.join(path,p))
	return file_list



if __name__ == '__main__':
	print("---Test case 1---")

	c_file_list  = find_files("","./testdir")
	print("num files : {}".format(len(c_file_list)))
	for c_file in c_file_list:
		print (c_file)

	print("---Test case 2---")
	
	c_file_list  = find_files("","")
	print("num files : {}".format(len(c_file_list)))
	for c_file in c_file_list:
		print (c_file)		

	print("---Test case 3---")
	
	c_file_list  = find_files("","./testdir2")
	print("num files : {}".format(len(c_file_list)))
	for c_file in c_file_list:
		print (c_file)		

	print("---Test case 4---")
	
	c_file_list  = find_files("","./testdir3")
	print("num files : {}".format(len(c_file_list)))
	for c_file in c_file_list:
		print (c_file)		

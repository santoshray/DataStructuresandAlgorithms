
def sqrt(num):

	if num == 0 :
		return 0
	l = 0  
	h = num
	appx = (l+h+1)//2
	sq_appx_1 = (appx+1)*(appx+1)
	sq_appx = appx*appx
	while( (appx >=2) and (sq_appx_1 < num or sq_appx > num) ):

		if (sq_appx_1 < num):
			l =appx 
			appx = (l+h+1)//2

		if(sq_appx > num):
			h = appx
			appx = (l+h+1)//2

		sq_appx_1 = (appx+1)*(appx+1)
		sq_appx = appx*appx


	return appx 


if __name__ == '__main__':
	
	print("sqrt(27) = {}".format(sqrt(27)))
	print("sqrt(101) = {}".format(sqrt(101)))
	print("sqrt(9) = {}".format(sqrt(9)))
	print("sqrt(0) = {}".format(sqrt(0)))
	print("sqrt(1) = {}".format(sqrt(1)))
	print("sqrt(2) = {}".format(sqrt(2)))

import imageio
import scipy.ndimage

def  sketch(imgp):
	global conv
	img = imageio.imread(imgp)
	#converting to grey
	r=img[:,:,0]
	g=img[:,:,1]
	b=img[:,:,2]
	grey=r*.2989+g*.5870+b*.1140
	inv = 255-grey
	#blur image
	blur = scipy.ndimage.filters.gaussian_filter(inv,sigma=10)
	#final image
	conv = blur*255/inv
	conv[conv>255]=255
	conv=conv.astype('uint8')
	imageio.imwrite('chg.png',conv)
#to save image
def savei(savefilename):
	imageio.imwrite(savefilename,conv)
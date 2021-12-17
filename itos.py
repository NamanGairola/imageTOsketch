import imageio
import scipy.ndimage

def  sketch(imgp):
	global r
	img = imageio.imread(imgp)
	#converting to grey
	r=img[:,:,0]
	g=img[:,:,1]
	b=img[:,:,2]
	grey=r*.2989+g*.5870+b*.1140
	i = 255-grey
	#blur image
	blur = scipy.ndimage.filters.gaussian_filter(i,sigma=10)
	#final image
	r = blur*255/i
	r[r>255]=255
	r=r.astype('uint8')
	imageio.imwrite('chg.png',r)
#to save image
def savei(savefilename):
	imageio.imwrite(savefilename,r)
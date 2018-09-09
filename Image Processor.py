#Image Processor by Horatio :-)

from scipy import misc,ndimage
import matplotlib.pyplot as plt
import numpy as np

def show_an_image(filename):
    pic_print = misc.imread(filename)
    plt.imshow(pic_print)
    plt.show()

def put_behind_bar(filename):
    pic_print = misc.imread(filename)
    for i in range (pic_print.shape[1]):
        for j in range (pic_print.shape[0]):
            if (i%100) < 50:
                pic_print[j][i] = [0,0,0]
    plt.imshow(pic_print)
    plt.show()
    misc.imsave('put_behind_bar_output.jpg', pic_print)

def mirror_image(filename):
    pic_print = misc.imread(filename)
    height = pic_print.shape[0] #row numbers
    width = pic_print.shape[1] #column numbers 
    rev_pic = pic_print #initialise vector
    for i in range(height): #can do height/2 but how do we account for floats?
        for j in range(width):
            rev_pic[i][j] = ((pic_print[i][j])/2 + (pic_print[i][width-j-1])/2)
            rev_pic[i][width-j-1] = rev_pic[i][j] #to ensure both sides are the same 
    plt.imshow(rev_pic)
    plt.show()
    misc.imsave('mirror_image_output.jpg', rev_pic)

def put_behind_bar_transparent(filename):
    pic_print = misc.imread(filename)
    for i in range (pic_print.shape[1]):
        for j in range (pic_print.shape[0]):
            if (i%100) < 50:
                pic_print[j][i] = pic_print[j][i]/2
    plt.imshow(pic_print)
    plt.show()
    misc.imsave('put_behind_bar_transparent_output.jpg', pic_print)

def circle_pic(filename):
    pic = misc.imread(filename)
    xlen, ylen = pic.shape[0], pic.shape[1]
    xcenter, ycenter = xlen/2, ylen/2

    pic2 = np.array(pic)
    for i in range(xlen):
        for j in range(ylen):
            if (i-xcenter)**2 + (j-ycenter)**2 > (xlen/3)**2:
                pic2[i][j] = pic2[i][j]/2

    plt.imshow(pic2)
    plt.imsave("circle_pic_output.jpg",pic2)
    plt.show()

def blur_image(filename):
    pic = misc.imread(filename)
    blurred_pic = ndimage.gaussian_filter(pic, sigma=(5,5,1))

    plt.imshow(blurred_pic)
    plt.imsave("blur_image_output.jpg",blurred_pic)
    plt.show()
    
def rotate_image(filename):
    pic = misc.imread(filename)
    rotate_1 = ndimage.rotate(pic, 45)
    rotate_1_noreshape = ndimage.rotate(pic, 45, reshape=False)

    plt.subplot(121)
    plt.imshow(rotate_1)
    plt.axis('off')
    plt.subplot(122)
    plt.imshow(rotate_1_noreshape)
    plt.axis('off')
    plt.imsave("rotate_image_noreshape_output.jpg",rotate_1_noreshape)
    plt.show()

def greyscale(picture):
    pic = misc.imread(picture)
    height = pic.shape[0]
    width = pic.shape[1]
    greyscale = pic
    for i in range(height): 
        for j in range(width):
            grey = (0.2989*greyscale[i][j][0]) + (0.5870*greyscale[i][j][1]) + (0.1140*greyscale[i][j][2])
            greyscale[i][j] = [grey]
    plt.imshow(greyscale)
    plt.show()
    misc.imsave('greyscale_image.jpg', greyscale)

def sepia(picture):
    pic = misc.imread(picture)
    height = pic.shape[0]
    width = pic.shape[1]
    sepia = pic
    for i in range(height): 
        for j in range(width):
            R = pic[i][j][0]
            G = pic[i][j][1]
            B = pic[i][j][2]
            red = min((0.393*(R)) + (0.769*(G)) + (0.189*(B)), 255)
            green = min((0.349*(R)) + (0.686*(G)) + (0.168*(B)), 255)
            blue = min((0.272*(R)) + (0.534*(G)) + (0.131*(B)),255)
            sepia[i][j] = [red, green, blue]
    plt.imshow(sepia)
    plt.show()
    misc.imsave('sepia_image.jpg', sepia)
   
def image_processor():
    function_dict = {'1': show_an_image, '2': mirror_image, '3': put_behind_bar, '4': put_behind_bar_transparent, '5': circle_pic, '6':blur_image, '7':rotate_image, '8':greyscale, '9':sepia, 'Q':quit}
    print("Welcome to Horatio's Image Processor!")
    filename = str(input('Please enter the file name:'))
    list = ['1','2','3','4','5','6','7', '8', '9', 'Q']
    print('Filename =', filename)
    print('Please select an operation you want to perform')
    print('1. Show the image')
    print('2. Mirror Image')
    print('3. Put behind bar')
    print('4. Put behind transparent bar')
    print('5. Circle Picture')
    print('6. Blurring')
    print('7. Rotation')
    print('8. Greyscale')
    print('9. Sepia')
    print('Q. Quit')
    key = str(input('Enter your choice (1-9,Q):'))
    while (key != 'Q'):
        if (key in list):
            function_dict[key](filename)
        else:
            print('Invalid Choice!')
        key = str(input('Enter your choice (1-9,Q):'))

image_processor()
#check for pixels first 

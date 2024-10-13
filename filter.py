import cv2 as c 

image = c.imread('image.jpg')
gray_image = c.cvtColor(image, c.COLOR_BGR2GRAY)
blur_image = c.GaussianBlur(image, (15, 15), 0)

c.imwrite('gray_image.jpg', gray_image)
c.imwrite('blur_image.jpg', blur_image)

print('saved')
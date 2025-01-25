import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

def localThres(image,block_size,c):

    imgpad = np.pad(image,pad_width=1,mode='constant', constant_values=0)
    threshold = np.zeros_like(image)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            local_area = imgpad[i:i+block_size,j:j+block_size]
            local_mean = np.mean(local_area)
            threshold[i,j] = 255 if image[i][j] > (local_mean - c) else 0
    return threshold

image1 = img.imread("C:\\Users\\dhika\\Downloads\\gunung.jpeg",mode='F')
image2 = img.imread("C:\\Users\\dhika\\Downloads\\gunung.jpeg")

thres = localThres(image1,15,10)
mask = (thres==255).astype(np.uint8)
segmented = image2 * mask[:,:,np.newaxis]

plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.imshow(image2)

plt.subplot(1,3,2)
plt.imshow(thres,cmap='gray')

plt.subplot(1,3,3)
plt.imshow(image1,cmap='gray')

plt.imshow(segmented)
plt.show()
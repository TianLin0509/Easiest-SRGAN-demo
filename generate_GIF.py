import os
import imageio

images = []
dir_name = r'images/'
# sort the images by number value
images_name = [x for x in os.listdir(dir_name)]
images_name.sort(key=lambda x: int(x[:-4]))
images_name = [dir_name + x for x in images_name]
images_name = images_name[0:20]
for i in images_name:
    images.append(imageio.imread(i))
imageio.mimsave('demo.gif', images, duration=0.3)

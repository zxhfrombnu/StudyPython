from PIL import Image

# case 1
# img = Image.open('dog.jpg')
# print(img.size)
# print(img.format)
# img.show()

# case 2
# img = Image.open('dog.jpg')
# area = (1000, 1000, 1500, 1500)
# cropped_img = img.crop(area)
# cropped_img.show()

# case 3
cat = Image.open("cat.jpg")
dog = Image.open("dog.jpg")
# cat.show()
# dog.show()

# need make the area match the size of the pasted picture
area = (0, 0, 480, 360)
cat.paste(dog, area)
cat.show()
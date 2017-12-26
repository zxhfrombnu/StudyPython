from PIL import Image

dog = Image.open("dog.jpg")
cat = Image.open("cat.jpg")

# case1: split into 3 channels
# print(dog.mode)
r, g, b = dog.split()

# r.show()
# g.show()
# b.show()

# case2: change the order
# new_img = Image.merge("RGB", (r, g, b))
# new_img.show()
#
# random_img = Image.merge("RGB", (b, r, g))
# random_img.show()

# case3:
r1, g1, b1 = dog.split()
r2, g2, b2 = cat.split()
new_img = Image.merge("RGB", (r1, g2, b1))
new_img.show()
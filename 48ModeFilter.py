from PIL import Image
from PIL import ImageFilter

# case1: the black and white image
# dog = Image.open("dog.jpg")
# black_white = dog.convert("L")
# black_white.show()

# case2: show the blur
dog = Image.open("dog.jpg")
blur = dog.filter(ImageFilter.BLUR)
# blur.show()

detail = dog.filter(ImageFilter.DETAIL)
edges = dog.filter(ImageFilter.FIND_EDGES)

detail.show()
edges.show()
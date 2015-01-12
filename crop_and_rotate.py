from PIL import Image
pil_im = Image.open('empire.jpg')

box = (100,0,150,50)
region = pil_im.crop(box)
region = region.transpose(Image.ROTATE_180)

pil_im.paste(region,box)

out = './empire_crop_and_rotate.jpg'
pil_im.save(out)

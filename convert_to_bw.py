from PIL import Image
pil_im = Image.open('empire.jpg').convert('L')
out = './empire_bw.jpg'
pil_im.save(out)

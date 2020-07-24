import os, shutil, time
import minecart
from PIL import Image
import img2pdf

if not os.path.exists('in'):
	os.mkdir('in')
if os.path.exists('out'):
	shutil.rmtree('out')
os.mkdir('out')


for file in os.listdir('in'):
	if os.path.isfile('in/'+file):
		ext = file.split('.')
		if ext[1] == 'pdf':
			os.mkdir('out/'+ext[0])
			pdf_file = open('in/'+file, 'rb')
			pdf_doc = minecart.Document(pdf_file)
			page = pdf_doc.get_page(0)
			i=0
			j=0
			im = page.images[0]
			
			for page in pdf_doc.iter_pages():
				for im in page.images:
					width = im.as_pil().width // 3
					height = im.as_pil().height // 3
					print(im.as_pil().format, im.as_pil().size, im.as_pil().mode)
					print(width, height)
					#print(page.width, page.height)
					#print(im.as_pil().width, im.as_pil().height)
					new_filename="out/"+ext[0]+"/"+ext[0]+"_"+str(i)+str(j)+".jpg"
					im2=im.as_pil().resize((width, height), resample=3, box=None, reducing_gap=None)
					im2.save(new_filename, "JPEG")
					print(new_filename)
					
					j=j+1

				i=i+1
			# convert all files ending in .jpg inside a directory
			dirname = "out/"+ext[0]
			with open("out/"+ext[0]+".pdf","wb") as f:
				imgs = []
				for fname in os.listdir(dirname):
					if not fname.endswith(".jpg"):
						continue
					path = os.path.join(dirname, fname)
					if os.path.isdir(path):
						continue
					imgs.append(path)
				f.write(img2pdf.convert(imgs))


				

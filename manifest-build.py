from iiif_prezi.factory import ManifestFactory
import os

prezi_uri = "http://ufdcimages.uflib.ufl.edu/UF/00/07/88/91/00001/"
prezi_dir = "//flvc.fs.osg.ufl.edu/flvc-ufdc/resources/AA/00/00/00/01/00001"
# prezi_dir = "/c/Users/desai.kirti/Desktop/New folder/iiif-pre/tmp"

fac = ManifestFactory()
# fac.set_debug("error")
fac.set_base_image_uri("https://iiif.io/api/image/2.1/")
fac.set_iiif_image_info(2.0, 2)

fac.set_base_prezi_uri(prezi_uri)
fac.set_base_prezi_dir(prezi_dir)

# fac.set_debug("warn") 
# mflbl = os.path.split(image_dir)[1].replace("_", " ").title()

mfst = fac.manifest(label="example")
seq = mfst.sequence()
# for fn in os.listdir(image_dir):
#     ident = fn[:-4]
#     title = ident.replace("_", " ").title()
#     cvs = seq.canvas(ident=ident, label=title)
#     cvs.add_image_annotation(ident, True)

for p in range(1,10):
	# Create a canvas with uri slug of page-1, and label of Page 1
    cvs = seq.canvas(ident="page-%s" % p, label="Page %s" % p)

    # Create an annotation on the Canvas
    anno = cvs.annotation()

    # Add Image: http://www.example.org/path/to/image/api/p1/full/full/0/native.jpg
    img = anno.image("OurOwnGayfulRestAPostcolonialArchiveFIXED_Page_0%s" % p, iiif=True)

	# Set image height and width, and canvas to same dimensions
    # imagefile = "http://ufdcimages.uflib.ufl.edu/AA/00/00/00/01/00001/OurOwnGayfulRestAPostcolonialArchiveFIXED_Page_0%s.jpg" % p
    # img.set_hw_from_file(imagefile) 

    # # OR if you have a IIIF service:
    # img.set_hw_from_iiif()

    cvs.height = img.height
    cvs.width = img.width

    cvs.height = 500
    cvs.width = 500

data = mfst.toString(compact=False)
fh = open("manifest.json", "w")
fh.write(data)
fh.close()
print(data)
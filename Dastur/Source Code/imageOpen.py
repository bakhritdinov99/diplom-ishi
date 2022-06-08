
from PIL import Image, ImageTk

def openImage():
    # create thumbanials of all images
    imgs = ['imga','imgb','imgc','imgd','imge','imgf','imgg','imgh','imgi','imgj','imgk','imgl','imgm','imgn','imgo','imgp','imgq','imgr','imgs','imgt','imgu','imgv','imgx','imgy','imgz']
    letters = ['a.jpg','b.jpg','c.jpg','d.jpg','e.jpg','f.jpg','g.jpg','h.jpg','i.jpg','j.jpg','k.jpg','l.jpg','m.jpg','n.jpg','o.jpg','p.jpg','q.jpg','r.jpg','s.jpg','t.jpg','u.jpg','v.jpg','x.jpg','y.jpg','z.jpg',]
    images = ['imagea','imageb','imagec','imaged','imagee','imagef','imageg','imageh','imagei','imagej','imagek','imagel','imagem','imagen','imageo','imagep','imageq','imager','images','imaget','imageu','imagev','imagex','imagey','imagez',]

    for x in range(len(imgs)):
        imgs[x]=Image.open(letters[x])
        imgs[x].thumbnail((600,650))
        images[x]=ImageTk.PhotoImage(imgs[x],master=top)

openImage()

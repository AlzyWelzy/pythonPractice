import os
import json


def createDir(par):
    if not os.path.exists(par):
        os.makedirs(par)
        print(f"Directory {par} doesn't exists, so it has been created.")
    else:
        print(f"Directory {par} already exists.")


files = os.listdir()


print(files)

donnotRemove = []

createDir("images")
createDir("docs")
createDir("media")
createDir("others")

# rawImgExts = [
"ase",
"art",
"bmp",
"blp",
"cd5",
"cit",
"cpt",
"cr2",
"cut",
"dds",
"dib",
"djvu",
"egt",
"exif",
"gif",
"gpl",
"grf",
"icns",
"ico",
"iff",
"jng",
"jpeg",
"jpg",
"jfif",
"jp2",
"jps",
"lbm",
"max",
"miff",
"mng",
"msp",
"nef",
"nitf",
"ota",
"pbm",
"pc1",
"pc2",
"pc3",
"pcf",
"pcx",
"pdn",
"pgm",
"PI1",
"PI2",
"PI3",
"pict",
"pct",
"pnm",
"pns",
"ppm",
"psb",
"psd",
"pdd",
"psp",
"px",
"pxm",
"pxr",
"qfx",
"raw",
"rle",
"sct",
"sgi",
"rgb",
"int",
"bw",
"tga",
"tiff",
"tif",
"vtf",
"xbm",
"xcf",
"xpm",
"3dv",
"amf",
"ai",
"awg",
"cgm",
"cdr",
"cmx",
"dxf",
"e2d",
"egt",
"eps",
"fs",
"gbr",
"odg",
"svg",
"stl",
"vrml",
"x3d",
"sxd",
"v2d",
"vnd",
"wmf",
"emf",
"art",
"xar",
"png",
"webp",
"jxr",
"hdp",
"wdp",
"cur",
"ecw",
"iff",
"lbm",
"liff",
"nrrd",
"pam",
"pcx",
"pgf",
"sgi",
"rgb",
"rgba",
"bw",
"int",
"inta",
"sid",
"ras",
"sun",
"tga",
"heic",
"heif"

# ]

# imgExts = ["." + exts for exts in rawImgExts]
# print(imgExts)

# with open("imgExts.txt", "a") as f:
#     f.write("\n".join(imgExts))

with open("extensions_by_type.json") as f:
    data = json.load(f)


# with open("imgExts.txt") as f:
#     lines = f.readlines()

# for line in lines:
#     imgExts.append(line.replace("\n", ""))

# print(imgExts)

othExt = []

for ext in data.keys():
    if not (ext == "Text" or ext == "Raster image" or ext == "Video" or ext == "Audio"):
        othExt.append(ext)

print(othExt)

othExts = [i for i in othExt]

docExts = [doc.lower() for doc in data.get("Text")]
imgExts = [doc.lower() for doc in data.get("Raster image")]
vidExts = [doc.lower() for doc in data.get("Video")]
audExts = [doc.lower() for doc in data.get("Audio")]
# otherExts = [doc.lower() for doc in data.get(i for i in othExt)]
otherExts = sum([[doc.lower() for doc in data[i]] for i in othExt], [])

# otherExts = []
# for i in othExt:
#     lowercase_docs = []
#     for doc in data[i]:
#         lowercase_docs.append(doc.lower())
#     otherExts.append(lowercase_docs)


############

images = [file for file in files if os.path.splitext(file)[
    1].lower() in imgExts]

print(images)

docs = [file for file in files if os.path.splitext(file)[
    1].lower() in docExts]

print(docs)

vids = [file for file in files if os.path.splitext(file)[
    1].lower() in vidExts]

print(vids)

auds = [file for file in files if os.path.splitext(file)[
    1].lower() in audExts]

print(auds)

#############


# print(os.path.splitext(files[2]))


# print(data)
# print(type(data))
# print(data.keys())


# print(docExts)

# if ".doc" in docExts:
#     print("YES")

print(otherExts)
print(len(otherExts))

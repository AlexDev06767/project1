
set1=set(files)
set_png=set()
for el in range(len(files)):
    files[el]=files[el].lower()

for elem in files:
    if'.png' in elem:
        set_png.add(elem)
for elem in sorted(set_png):
    print(elem,end=' ')

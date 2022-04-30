filename = sorted([os.path.split(file)[-1] for file in glob.glob(folder+'5/json/*.json')],key=sorter1)
# for i in range(len(filename)-20,len(filename)):

#     print("Prdicted file names", filename[i][:-5]+'.jpg')

#     print(folder+'5/rgb/'+filename[i][:-5]+'.jpg')
#     rgb.append(folder+'5/rgb/'+filename[i][:-5]+'.jpg')
#     label.append(folder+'5/label/'+filename[i][:-5]+'.png')
#     x.append(folder+'5/x/'+filename[i][:-5]+'.jpg')
#     y.append(folder+'5/y/'+filename[i][:-5]+'.jpg')
#     z.append(folder+'5/z/'+filename[i][:-5]+'.jpg')
    
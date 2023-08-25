
import os
import shutil


directory = '/data/data1/users/ksismanis/realesrganbinary/realesrgan2x/photo_color'
newdir = '/data/data1/users/ksismanis/upscale/upscale/sources/output'
methodfilename = 'RealEsrgan2x.png'

#main loop
count  = 0 
for root, dirs, files in os.walk(directory):
     for filename in files:
        print('input: '+  os.path.join(root, filename))
        input = os.path.join(root, filename)
        print('filename:' + filename)
        output = os.path.join(newdir,filename[:-4],methodfilename)
        # os.mkdir(os.path.join(newdir,filename[:-4]))
        print('output:' + output)
        # shutil.copy2(input,output)
        command =  'cp ' + ' ' + input + ' ' + output
        count = count + 1
        print(count+1,  ' copied')
        os.popen(command)



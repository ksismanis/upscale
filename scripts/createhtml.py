
import os
import shutil


directory = '/data/data1/users/ksismanis/samples/drawing'
newdir = '/data/data1/users/ksismanis/upscale/upscale/sources/output'
methodfilename = 'RealEsrgan2x.png'


#main loop
count  = 0 
for root, dirs, files in os.walk(directory):
     for filename in files:
        # print('input: '+  os.path.join(root, filename))
        input = os.path.join(root, filename)
        # print('filename:' + filename)
      #   output = os.path.join(newdir,filename[:-4],methodfilename)
      #   # os.mkdir(os.path.join(newdir,filename[:-4]))
      #   print('output:' + output)
      #   # shutil.copy2(input,output)
      #   command =  'cp ' + ' ' + input + ' ' + output
        count = count + 1
      #   print(count+1,  ' copied')
      #   os.popen(command)

        # name = filename.split('/')[-1]
        print()
        print('## ' + filename)
        print()
        print('<div id="example'+str(count)+'">')
        print('<ImageSliderGithub :key="componentKey" inputImageURL=\'https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/'+filename+ '\' relativePathOutputFolder=\'output/'+filename[:-4]+'\' />')
        print('</div>')
        print(' <button v-if="fullscreenEnabled" @click="enterFullscreen(\'example'+str(count)+'\')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> ')
        print('<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>')
        print('<br/>') 
        print('<details>')
        print('<summary>Details</summary>')
        print('<p>')

        # <!-- Input Image: 480x320 pixels -->
        print()

        print('Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/'+filename+')')
        print('Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/'+filename[:-4]+')')
        print('</p>')
        print('</details>')  
      


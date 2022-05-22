import json
from re import T
import  os
from urllib.parse import urlparse

from calmjs.parse.asttypes import Catch

def combinets(ep_name, download_path, file_prefix):
  try:
    print('%s %s 下载完成，即将开始合并视频文件。' %(ep_name, file_prefix))
    #hebing_path = download_path+ '/' + file_prefix + '.mp4'
    all_ts = sorted(os.listdir(download_path))
    needed_ts = []
    for i in all_ts:
      if os.path.splitext(i)[0].startswith(file_prefix) and os.path.splitext(i)[1].endswith('.ts'):
        needed_ts.append(i)
    x1, x2 = '/', '.mp4'
    hebing_path = f'{download_path}{x1}{file_prefix}{x2}'
    if not os.path.isfile(hebing_path):
      with open(hebing_path, 'wb+') as f:
          for ii in range(len(needed_ts)):
              ts_video_path = os.path.join(download_path, needed_ts[ii])
              f.write(open(ts_video_path, 'rb').read())
      print("%s %s 合并完成！！" %(ep_name, file_prefix))
    return True
  except Exception as e:
    return False


def deletets(ep_name, download_path,file_prefix):
  try:
    if os.path.exists(download_path):
      os.chdir(download_path)
      file_list = os.listdir()
      for file in file_list:
        if file.startswith(file_prefix) and file.endswith('.ts'):
          os.remove(download_path+'/'+file)
      print("%s %s 临时文件删除完毕！" %(ep_name , file_prefix ))
    return True
  except Exception as e:
    return False
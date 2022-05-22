import json
from re import T
import  os
from urllib.parse import urlparse

def main(s, url, download_path, ep_name, file_prefix, ep_num_origin):
  json_path= download_path + '/' + ep_name + ep_num_origin + " import.json"
  parsed_uri=urlparse(url)
  domain = '{uri.netloc}'.format(uri=parsed_uri)
  path = '{uri.path}'.format(uri=parsed_uri)
  host_split = domain.split('.')
  path_split = path.split('/')
  #filePath = str(filePath, "utf-8")
  if not os.path.isfile(json_path):
    json_info = {}
    data = json.loads(json.dumps(json_info))
    json_main_info = {
    '_postman_id':'',
    'name': ep_name + ep_num_origin,
    'schema':'https://schema.getpostman.com/json/collection/v2.1.0/collection.json',
    }
    data['info'] = json_main_info
    data['item'] = [{
      'name': file_prefix +'-'+ s,
      'protocolProfileBehavior': {
        'disabledSystemHeaders': {
          'connection': True,
          'user-agent': True
        }
      },
      'request': {
        'method': 'GET',
        'header': [
          {
            'key': 'authority',
            'value': 't.wdubo.com',
            'type': 'text'
          },
          {
            'key': 'method',
            'value': 'GET',
            'type': 'text'
          },
          {
            'key': 'scheme',
            'value': 'https',
            'type': 'text'
          },
          {
            'key': 'accept-language',
            'value': 'zh-CN,zh;q=0.9,en;q=0.8',
            'type': 'text'
          },
          {
            'key': 'origin',
            'value': 'https://m.duboku.fun',
            'type': 'text'
          },
          {
            'key': 'referer',
            'value': 'https://m.duboku.fun/',
            'type': 'text'
          },
          {
            'key': 'user-agent',
            'value': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            'type': 'text'
          }
        ],
        'url': {
          'raw': url,
          'protocol': 'https',
          'host': [
            host_split[0],
            host_split[1],
            host_split[2]
          ],
          'path': [
            path_split[1],
            path_split[2],
            path_split[3],
            path_split[4]
          ]
        }
      },
      'response': []
    }]
    postmanjson = json.dumps(data, indent = 4, ensure_ascii=False)
    with open(json_path, 'w', encoding='utf-8') as file:
      #file.write(json.dumps(postmanjson, indent = 4))
      file.write(postmanjson)
      file.close()
    #print('因无法突破反爬策略，已生成postman的导入json文件，导入到postman里去逐个下载，json文件路径：'+ download_path +'，文件名：import.json，下载文件名应为postman中collection的每个名字（如：002.ts），下载完成后将这些ts拷贝到'+ download_path +'，按名称顺序排序，重新进行合并即可（合并命令：copy /b '+ file_prefix + '*.ts xxx.mp4）')
  else:
    #new = json.dumps({**json.loads(json_path), **{"new_key": "new_value"}})
    file = open(json_path,encoding='utf-8', errors='ignore')
    file_lines = file.read()
    file.close()
    file_json = json.loads(file_lines)
    new_item = {
          'name': file_prefix +'-'+s,
          'protocolProfileBehavior': {
            'disabledSystemHeaders': {
              'connection': True,
              'user-agent': True
            }
          },
          'request': {
            'method': 'GET',
            'header': [
              {
                'key': 'authority',
                'value': 't.wdubo.com',
                'type': 'text'
              },
              {
                'key': 'method',
                'value': 'GET',
                'type': 'text'
              },
              {
                'key': 'scheme',
                'value': 'https',
                'type': 'text'
              },
              {
                'key': 'accept-language',
                'value': 'zh-CN,zh;q=0.9,en;q=0.8',
                'type': 'text'
              },
              {
                'key': 'origin',
                'value': 'https://m.duboku.fun',
                'type': 'text'
              },
              {
                'key': 'referer',
                'value': 'https://m.duboku.fun/',
                'type': 'text'
              },
              {
                'key': 'user-agent',
                'value': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
                'type': 'text'
              }
            ],
            'url': {
              'raw': url,
              'protocol': 'https',
              'host': [
                host_split[0],
                host_split[1],
                host_split[2]
              ],
              'path': [
                path_split[1],
                path_split[2],
                path_split[3],
                path_split[4]
              ]
            }
          },
          'response': []
        }
    file_json['item'].append(new_item)
    postmanjson = json.dumps(file_json, indent = 4, ensure_ascii=False)
    with open(json_path, 'w', encoding='utf-8') as file:
      #file.write(json.dumps(postmanjson, indent = 4))
      file.write(postmanjson)
      file.close()
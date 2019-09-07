import zipfile
import glob
from configparser import ConfigParser
import log
from error import UseError
print(__name__)
logging = log.lezhin_log(__name__).get_log()
def zip_to_folder(comic_folder_path, comic_zip_path, comic_zip_name):
    f = zipfile.ZipFile(comic_zip_path + '/' + comic_zip_name, 'w', zipfile.ZIP_DEFLATED)
    files = glob.glob(comic_folder_path + '/*')
    for file in files:
        f.write(file)
    f.close()

def gain_info_from_dic(dic_data):
    data = dic_data['data']
    extra = data['extra']
    episode = extra['episode']
    updatedAt = episode['updatedAt']
    scrollsInfo = episode['scrollsInfo']
    return updatedAt, scrollsInfo

def read_config(config_url):
    try:
        config = ConfigParser()
        config.read(config_url,encoding='UTF-8')
    except Exception as e:
        logging.error("读取配置文件出现错误信息 %s", e)
        raise UseError("读取配置文件错误，详情见log日志")
    return config
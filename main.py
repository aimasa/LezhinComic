from Run.lezhin import run
from RunInfo import log
logging = log.lezhin_log(__name__).get_log()
if __name__ == "__main__":
    file_path = input("配置文件路径：")
    run(file_path)

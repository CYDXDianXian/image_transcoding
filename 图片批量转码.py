import sys
from PIL import Image 
import time
from pathlib import Path


source_folder = "img"
output_folder = "output"
img_type = "png" # 设置要转换图片的目标格式

path_input = Path(__file__).parent / source_folder
path_output = Path(__file__).parent / output_folder

Path(path_output).mkdir(parents = True, exist_ok = True)

try:
    path_list = [i for i in Path(path_input).iterdir()] # 当路径指向一个目录时，产生该路径下的所有对象的路径。iterdir()返回的是一个生成器，需要循环遍历才能读取
except FileNotFoundError:
    print('文件目录下没有img文件夹，请创建文件夹并将图片放入img文件夹中')
    sys.exit()

def changeType():
    start = time.time()
    
    success_num = 0
    error_num = 0
    for file_path in path_list:
        s = Path(file_path).suffix # 目录中最后一个部分的扩展名
        if s in [".webp", ".jfif", ".jpeg", ".png"]:
            try:
                im = Image.open(file_path) # 获取图片详细属性
                im.load() # :im.load() 含义:为图像分配内存并从文件中加载它
                imname = Path(file_path).stem # 目录最后一个部分，没有后缀（仅文件名）
                pic = Path(f'{path_output}', f'{imname}.{img_type}') # 拼接路径、文件名与目标后缀
                if img_type in ["png", "webp"]:
                    colour = "RGBA"
                else: 
                    colour = "RGB"
                im.convert(colour).save(pic, quality = 100) # 保存文件，目标目录中的同名文件会被覆盖
                # Path(file_path).unlink(missing_ok = True) # 删除源文件，missing_ok = True表示若路径不存在则忽略异常
                success_num += 1
                print(f'转换成功{success_num}个：{imname}{s}')
            except:
                error_num += 1
                print(f'转换失败{error_num}个：{imname}{s}')
                continue
        else:
            error_num += 1
            image = Path(file_path).name
            print(f'转换失败{error_num}个：{image}')

    end = time.time()

    print(f'全部转换完成！！！共成功{success_num}个，失败{error_num}个，用时{int(end - start)}秒')
    print(f'文件输出路径：{path_output}')

if __name__ == "__main__":
    changeType() 
import cv2

def readMP4(path, top, right, bottom, left):
    '''
    读取 MP4 并将每一帧进行截取
    :param path: 路径
    :param top: 上边界
    :param right: 右边界
    :param bottom: 下边界
    :param left: 左边界
    :return: 总视频
    '''
    # 存储缓存
    buffer = []

    # 读取视频
    camera = cv2.VideoCapture(path)

    while True:
        res, image = camera.read()
        try:
            image_p = image[top:bottom][left:right]
        except:
            print("视频读取完毕")
            # print(image_p.shape)
            return buffer
        else:
            buffer.append(image_p)


def writeMP4(buffer, filename, fps = 20):
    '''
    MP4 存储
    :param buffer: 缓存区
    :param filename: 存储地址
    :param fps: 视频每秒帧数
    :param size: 需要转为视频的图片的尺寸
    :return:
    '''
    height = int(buffer[0].shape[0])
    width = int(buffer[0].shape[1])
    size = (width, height)

    # 设置视频流
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(filename, fourcc, fps, size, 1)

    # 存储每一帧
    for item in buffer:
        # cv2.imshow("1", item)
        # cv2.waitKey(0)
        video.write(item)
    
    video.release()
    print("视频存储完毕")

if __name__ == '__main__':
    buf = readMP4(r"C:\\Users\\35500\\Desktop\\test.mp4", 330, 544, 625, 0)
    writeMP4(buf, r"C:\\Users\\35500\\Desktop\\test1.mp4", fps=24)

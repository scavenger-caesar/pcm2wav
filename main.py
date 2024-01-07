#encoding:UTF-8

from PCM2WAV import pcm2wav
from Ui_PCM2WAV_UI import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from pathlib import Path
import sys

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.__channels = 2
        self.__bits = 16
        self.__sample_rate = 48000
        self.__outputFileName = "output.wav"
        self.__inputFile = None
        self.setupUi(self)
        self.setWindowTitle("PCM转WAV")

        # self.input_sample_rate.text
        # 当按下确认键时把pcm数据转成wav
        self.start_button.clicked.connect(self.__convert_start)
        # 设置pcm的输入采样率
        self.input_sample_rate.textActivated[str].connect(self.__sample_rate_get)
        # 设置wav的输出采样率
        self.output_sample_rate.textActivated[str].connect(self.__sample_rate_get)
        # 设置pcm的输入通道数
        self.input_sample_channel.textActivated[str].connect(self.__channels_get)
        # 设置wav的输出通道数
        self.output_sample_channel.textActivated[str].connect(self.__channels_get)
        # 设置pcm的输入采样位深(bit)
        self.input_sample_width.textActivated[str].connect(self.__bits_get)
        # 设置wav的输出采样位深(bit)
        self.output_sample_width.textActivated[str].connect(self.__bits_get)
        # 选择pcm文件
        self.open_file.triggered.connect(self.__showFileDialog)

    def __showFileDialog(self):
        # 获取当前路径
        current_dir = str(Path.cwd())
        # 获取选择的文件路径
        fname = QFileDialog.getOpenFileName(self, "pcm文件选择", current_dir)
        # 把选择的pcm文件路径给inputFile
        self.__inputFile = fname[0]
        self.__message_show("选择的pcm文件为：")
        self.__message_show(self.__inputFile + "\n")
        # if fname[0]:
        #     f = open(fname[0], 'r')
        #     with f:
        #         pass

    def __channels_get(self, text):
        if text == '2channel':
            self.__channels = 2
        elif text == '1channel':
            self.__channels = 1
        elif text == '4channel':
            self.__channels = 4
        else:
            self.__message_show("channels set error.")

    def __bits_get(self, text):
        if text == '16bit':
            self.__bits = 16
        elif text == '8bit':
            self.__bits = 8
        elif text == '32bit':
            self.__bits = 32
        else:
            self.__message_show("bits set error.")

    def __sample_rate_get(self, text):
        if text == '48khz':
            self.__sample_rate = 48000
            # self.message_show("rate is 48000")
        elif text == '44.1khz':
            self.__sample_rate = 44100
            # self.message_show("rate is 44100")
        elif text == '16khz':
            self.__sample_rate = 16000
            # self.message_show("rate is 16000")
        else:
            self.__message_show("sample rate set error.")

    def __convert_start(self):
        if self.__inputFile is None:
            self.__message_show("没有选择pcm文件")
            return
        # self.start_button.clicked.connect(lambda:pcm2wav("raw.pcm", "output.wav"))
        pcm2wav(self.__inputFile, self.__outputFileName, self.__channels, self.__bits, self.__sample_rate)
        self.__message_show("output file name      :" + str(self.__outputFileName))
        self.__message_show("output channel number :" + str(self.__channels))
        self.__message_show("output sample rate    :" + str(self.__sample_rate))
        self.__message_show("output bits           :" + str(self.__bits))

    def __message_show(self, message):
        self.output_message.append(str(message))

def main():
    app = QApplication(sys.argv)
    ui = MyWindow()
    ui.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
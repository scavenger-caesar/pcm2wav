#encoding:UTF-8

import wave
import sys, getopt

def pcm2wav(pcm_file, wav_output_file, channels = 2, bits = 16, sample_rate = 48000):
    
    pcmFile = open(pcm_file, 'rb')
    pcmdata = pcmFile.read()
    pcmFile.close()

    if bits % 8 != 0:
        raise ValueError("bits % 8 must == 0. now bits is:" + str(bits))

    wavFile = wave.open(wav_output_file, 'wb')
    #设置输出通道数
    wavFile.setnchannels(channels)
    #设置输出采样深度
    wavFile.setsampwidth(bits // 8)
    #设置采样频率
    wavFile.setframerate(sample_rate)
    #写入pcm数据
    wavFile.writeframes(pcmdata)
    wavFile.close

def appStart(argv):
    
    inputFileName = argv[0]
    #初始化输出wav文件的音频参数
    outputFileName = "output.wav"
    channelNum = 2
    sampleWidth = 16
    sampleRate = 48000

    opts, args = getopt.getopt(argv[1:], "-o:-c:-r:-b:-s:")
    for opt, arg in opts:
        if opt == '-o':
            outputFileName = str(arg)
        elif opt == '-c':
            channelNum = int(arg)
        elif opt == '-r':
            sampleRate = int(arg)
        elif opt == '-b':
            sampleWidth = int(arg)

    pcm2wav(inputFileName, outputFileName, channelNum, sampleWidth, sampleRate)
    print("output file name      :", outputFileName, "\n"
          "output channel number :", str(channelNum), "\n"
          "output sample rate    :", str(sampleRate), "\n"
          "output bits           :", str(sampleWidth), "\n")

if __name__ == '__main__':

    arguments = len(sys.argv)
    if arguments < 2:
        print("Usage:\npython", sys.argv[0], "<PCM_File.pcm> [-o output_file]"
                " [-c channels] [-r rate_hz] [-b bits]\n")
        sys.exit(0)

    appStart(sys.argv[1:])
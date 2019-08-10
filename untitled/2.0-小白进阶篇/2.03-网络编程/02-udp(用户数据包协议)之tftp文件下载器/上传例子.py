# tftp 简单文件传输协议
# 上传文件
import struct

# 定义几个变量
# 要上传到服务端的文件名
uploadToServerFileName = "HelloWorld.mkv".encode("utf-8");
# 上传进度
uploadProgress = 0;
# 起始的快编号标记
kuaiBiaoHaoFlag = 0;
# 建立UDP
import socket

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
# 建立读写请求
file_upload_request = "!H" + str(len(uploadToServerFileName)) + "s" + "b" + "5s" + "b";
tftp_upload_request = struct.pack(file_upload_request, 2, uploadToServerFileName, 0, "octet".encode("utf-8"), 0)
udpSocket.sendto(tftp_upload_request, ("169.254.164.219", 69))
# 要上传的文件
ready_to_upload_file = open("HelloWorld.mkv".encode("utf-8"), "rb+")

while True:

    recv_data, recv_adr = udpSocket.recvfrom(516)
    #print(recv_data)
    caozuoma, kuaibianhao = struct.unpack("!HH", recv_data[:4])
    #print("操作码::%s" % caozuoma)  #
    #print("块编号::%s" % kuaibianhao)

    if (caozuoma == 4):

        if (kuaibianhao == kuaiBiaoHaoFlag):
            print("服务端已经收到了我的数据，准备上传下一个")
            # 开始上传数据,此时要像服务端发送数据包，数据大小最大为512
            kuaiBiaoHaoFlag += 1;
            data = ready_to_upload_file.read(512);
            print(data)
            if (data == ("".encode("utf-8"))):
                print("上传结束")
                break

            if (kuaibianhao == 65535):
                kuaiBiaoHaoFlag = 0
                kuaibianhao = 0

            # 数据包
            data_request = "!H" + "H" + str(len(data)) + "s"
            shujuBao = struct.pack(data_request, 3, kuaiBiaoHaoFlag, data)
            udpSocket.sendto(shujuBao, recv_adr)


        else:
            print("服务端没收到我上传的数据")
            break

udpSocket.close()
ready_to_upload_file.close()
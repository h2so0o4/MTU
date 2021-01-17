from scapy.layers.inet import IP, ICMP, TCP
from scapy.layers.l2 import Ether

print("请稍等...")
import sys
import logging  # 引入logging模块

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # 清除报错
from scapy.all import *  # 导入scapy模块


def mtu_one(mtu, dst):
    data = b'a' * (mtu - 28)

    # result = sr1(Ether(dst='48-bd-3d-22-77-e0') / IP(flags='DF', dst=dst) / ICMP() / data,
    #              timeout=0.2, iface='Intel(R) Dual Band Wireless-AC 3168')

    # result = sr1(IP(flags='DF',dst=dst) / ICMP() / data, timeout=0.2,
    #             iface='Intel(R) Dual Band Wireless-AC 3168')  # 发送第三层数据包

    result = sr1(IP(flags='DF', dst=dst) / ICMP() / data, timeout=0.2)  # 发送第三层数据包
    # print(result.show())
    try:

        # 如果返回数据包ICMP层的type==3，code==4则表明数据包已经超过了MTU
        if result.getlayer(ICMP).type == 3 and result.getlayer(ICMP).code == 4:
            return 1

        # 如果返回数据包ICMP层的type==0，code==0则表明数据包可以成功发送，大小没有超过MTU
        elif result.getlayer(ICMP).type == 0 and result.getlayer(ICMP).code == 0:
            return 2
    except:
        return None


if __name__ == "__main__":
    ipaddr = input('ip: ')
    mtu = 1500
    while mtu > 0:
        res = mtu_one(mtu, ipaddr)
        if res == 1 or res is None:
            mtu -= 1
        elif res == 2:
            print('mtu: %d' % mtu)
            break

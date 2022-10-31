import dpkt
import socket

def ip_pcap(pcap):
 for (t, f) in pcap:
  try:
   count = 0
   ether = dpkt.ethernet.Ethernet(f)
   ip = ether.data
   src = socket.inet_ntoa(ip.src)
   dest = socket.inet_ntoa(ip.dst)
   print (count + '. Src: ' + src + ' --> Dst: ' + dest)
   response = requests.post("http://ip-api.com/batch", json=[
  {"query": src},
  {"query": dest},
]).json()
   for ip_info in response:
    for k,v in ip_info.items():
        print(k,v)
    print("\n")
   count++
  except:
   pass

def main():
 f = open('test.pcap', 'rb')
 pcap = dpkt.pcap.Reader(f)
 ip_pcap(pcap)

if __name__ == '__main__':
 main()

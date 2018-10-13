import socket
Ip=input("enter your ip")
Port1=int(input("enter starting port"))
Port2=int(input("enter ening port"))
for ports in range(Port1,Port2+1):
    d=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s = d.settimeout(3)
    c=d.connect_ex((Ip,ports))
    d.close
    try:
        q = socket.getservbyport(ports)
        if c==0:
            print(ports,"is open")

        else:
            print(ports,"is filtered")
    except:
        print(ports,"Not a port")
w=open("xy.txt","w")
w.write(print(ports,"is open"))
w.write(print(ports,"is filtered"))
w.close

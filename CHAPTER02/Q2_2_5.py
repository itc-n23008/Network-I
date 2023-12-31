ip address show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000

    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTTCAST,UP,LOWER_UP> mtu 1500 qdisc fg_codel state UP group default qlen 1000
    link/ether 00:00:5e:00:53:01 brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.15/24 brd 10.0.2.255 scope global dynamic enp0s3
       valid_lft 85939sec preferred_lft 85939sec
    inet6 fe80::200:5eff:fe00:5301/64 scope link
       valid_lft forever preferred_lft forever


ping -c 3 127.0.0.1
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.016 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.048 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.036 ms

--- 127.0.0.1 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2032ms
rtt min/avg/max/mdev = 0.016/0.033/0.048/0.014 ms


sudo tcpdump -tn -i any icmp
tcpdump: verbose putput suppressed, use -v or -vv for full protocol decode
listening on any, link-type LINUX_SLL (Linux cooked), capture size 262144 bytes


ping -c 3 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=63 time=10.6 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=63 time=11.2 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=63 time=12.8 ms

--- 8.8.8.8 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2004ms
rtt min/avg/max/mdev = 10.669/11.585/12.838/0.925 ms


sudo tcpdump -th -i any icmp
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on any, link-type LINUX_SLL (Linux cooked), capture size 262144 bytes
IP 10.0.2.15 > 8.8.8.8: ICMP echo request, id 2766, seq 1, length 64
IP 8.8.8.8 > 10.0.2.15: ICMP echo reply, id 2766, seq 1, length 64
IP 10.0.2.15 > 8.8.8.8: ICMP echo request, id 2766, seq 2, length 64
IP 8.8.8.8 > 10.0.2.15: ICMP echo reply, id 2766, seq 2, length 64
IP 10.0.2.15 > 8.8.8.8: ICMP echo request, id 2766, seq 3, length 64
IP 8.8.8.8 > 10.0.2.15: ICMP echo reply, id 2766, seq 3, length 64


sudo tcpdump -tn -i any icmp
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on any, link-type LINUX_SLL (Linux cooked), capture size 262144 bytes
IP 10.0.2.15 > 8.8.8.8: ICMP echo request, id 2766, seq 1, length 64
IP 8.8.8.8 > 10.0.2.15: ICMP echo reply, id 2766, seq 1, length 64
IP 10.0.2.15 > 8.8.8.8: ICMP echo request, id 2766, seq 2, length 64
IP 8.8.8.8 > 10.0.2.15: ICMP echo reply, id 2766, seq 2, length 64
IP 10.0.2.15 > 8.8.8.8: ICMP echo request, id 2766, seq 3, length 64
IP 8.8.8.8 > 10.0.2.15: ICMP echo reply, id 2766, seq 3, length 64
^c
6 packets captured
6 packets received by filter
0 packets dropped by kernel

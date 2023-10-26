sudo ip netns add helloworld


ip netns list
helloworld


sudo ip netns exec helloworld ip address show
1: lo: <LOOPBACK> mtu 65536 qdisc noop state DOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00


ip address show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWE qroup default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 seope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq codel state UP group default qlen 1000
    link/ether 00:00:5e:00:53:01 brd ff:ff:ff:ff:ff:ff
    imet 10.0.2.15/24 brd 10.0.2.255 scope qlobal dynamic enp0s3
       valid_lft 85939sec preferred_lft 85939sec
    inet6 fe80::200:5eff:fe00:5301/64 seope link
       valid_lft forever preferred_lft forever


sudo ip netns exec helloworld ip route show
Error: ipv4: FIB table does not exist.
Dump terminated


sudo ip netns delete helloworld


sudo ip netns exec helloworld bas

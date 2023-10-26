sudo ip netns add ns1
sudo ip netns add ns2


sudo ip link add ns1-veth0 type veth peer name ns2-veth0


ip link show | grep veth
3: ns2-veth0@ns1-veth0: <BROADCAST,MULTICAST,M-DOWN> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
4: ns1-veth0@ns2-veth0: <BROADCAST,MULTICAST,M-DOWN> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000


sudo ip link set ns1-veth0 netns ns1
sudo ip link set ns2-veth0 netns ns2


ip link show | qrep veth


sudo ip netns exec ns1 ip link show | qrep veth
4: ns1-veth0@if3: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT qroup default qlen 1000
sudo ip netns exec ns2 ip link show | qrep veth
3: ns2-veth0@if4: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT qroup default qlen 1000


sudo ip netns exec ns1 ip address add 192.0.2.1/24 dev ns1-veth0
sudo ip netns exec ns1 ip address add 192.0.2.1/24 dev ns2-veth0

1. netstat

https://www.runoob.com/linux/linux-comm-netstat.html

-t（显示TCP连接）、-u（显示UDP连接）、-l（显示监听状态）、-p（显示进程标识符）

例如：netstat -tulnp 将显示当前系统中的所有 TCP 和 UDP 连接以及监听端口，并显示关联的进程信息。

2. ps
   
    -aux（显示所有进程）、-ef（显示全格式）

3. lsof

    -i（显示网络连接信息）、-u（显示指定用户打开的文件）、-c（显示指定进程名打开的文件）
   
   lsof 查看端口占用语法格式：lsof -i:端口号

    https://www.runoob.com/w3cnote/linux-check-port-usage.html

4. /proc 伪文件系统

 /proc/cpuinfo（CPU 信息）、/proc/meminfo（内存信息）、/proc/<PID>/（每个进程的信息目录）

https://www.runoob.com/linux/linux-system-contents.html



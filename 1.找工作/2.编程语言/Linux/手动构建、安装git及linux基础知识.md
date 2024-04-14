## 以git编译安装为例

下载压缩包wget https://github.com/git/git/archive/refs/tags/v2.41.0.zip

unzip 

cd 

找到README.md

编译安装之前先安装所需依赖包：（用的是docker镜像为ubuntu）

    sudo apt-get install libcurl4-openssl-dev libexpat1-dev gettext libssl-dev zlib1g-dev perl make autoconf curl expat tclsh gettext

1. make configure

    用于生成配置脚本 configure

    在 Git 项目中，configure 脚本是一个自动生成的脚本，它负责根据当前系统的环境和特性生成适合的 Makefile。

    configure 脚本**基于 Autoconf 工具链生成**，用于检测系统的功能、库文件、依赖项和其他配置选项，并根据这些信息生成适当的 Makefile 文件。

    运行 make configure 命令会执行一系列预定义的规则和命令，以便生成 configure 脚本。具体而言，该命令将运行 Autoconf 工具，扫描源代码目录中的配置模板文件（如 configure.ac 或 configure.in），并根据模板生成最终的 configure 脚本。

    这样，开发者可以在不同的系统上使用相同的源代码，而无需手动修改 Makefile 来适应不同的环境和配置。

2. make 

    可以传入参数：`make prefix=/root/gjh`

    是一个常用的构建工具,它主要用于编译源代码并生成可执行文件、库文件或其他构建目标。

    要使用 **make 工具**，通常**需要创建一个名为 Makefile**的文件，并在其中定义项目的规则和依赖关系。然后在终端或命令行界面中运行 make 命令，make 工具将读取 Makefile 文件并执行相应的构建操作。

    1. make install

    在使用 make 命令编译软件时，通常会生成可执行文件、库文件、配置文件等。但是这些文件只是编译好的结果，并没有真正安装到系统中。如果要将这些文件安装到系统中，可以使用 make install 命令。

    使用 make install 命令时，需要以管理员权限运行，以便将文件复制到系统目录。可以使用 sudo make install 命令来获取管理员权限并执行安装操作。

4. 加入环境变量

   - 临时加入当前会话(重启会话会失效)：export PATH="/root/bin:$PATH"

       exec bash, 重启bash会话

   - 永久：echo "export PATH=$PATH:/root/bin" >> /etc/profile

    source /etc/profile (用于在**当前**终端会话中重新加载/etc/profile文件)

    (这段命令是将路径**添加到当前 shell 会话的环境变量中**，并不是将路径添加到某个文件中。)

    有时候还需要**将软件的可执行文件所在的路径添加到系统的环境变量中**，以便在**任何位置都可以直接运行该软件**。

    环境变量是操作系统用来存储一些系统级别的配置信息的变量。当你在命令行中输入一个命令时，**系统会根据环境变量中的路径来查找该命令的可执行文件**

    当你在命令行中输入一个命令时，系统会按照 PATH 环境变量中的路径顺序依次搜索这些路径，直到找到对应的可执行文件为止。


## 疑问和知识点：

1. /etc 文件夹用来存放什么相关的文件

    ```
    /etc目录（也称为ETC目录）是Linux和Unix系统中的一个重要目录，用于存放系统配置文件和相关数据。这些文件通常用于配置系统的行为、服务和各种应用程序。

    以下是一些在/etc目录下常见的文件和文件夹：

    /etc/passwd：包含系统上的用户账户信息。

    /etc/group：包含用户组的定义和成员关系。

    /etc/shadow：包含加密的用户密码信息。

    /etc/hosts：用于配置系统的主机名解析，映射IP地址和主机名之间的关系。

    /etc/resolv.conf：用于配置系统的DNS解析器的配置。

    /etc/network/interfaces或/etc/sysconfig/
    network-scripts：包含网络接口的配置信息。

    /etc/fstab：包含文件系统挂载点的配置。

    /etc/ssh/sshd_config：SSH服务器的配置文件。

    /etc/crontab：用于配置系统的定时任务（cron jobs）。

    /etc/apt/sources.list：用于配置APT软件包管理器的软件源列表（适用于基于Debian的系统）。

    /etc/sudoers：用于配置sudo命令的访问权限。

    此外，/etc目录还包含许多其他系统和服务的配置文件，例如HTTP服务器（如Apache或Nginx）、数据库服务器（如MySQL或PostgreSQL）、邮件服务器（如Postfix或Sendmail）等。

    需要注意的是，对于不同的Linux发行版和Unix操作系统，一些特定的配置文件和文件夹的位置和命名可能会有所不同。因此，具体的配置文件路径和名称可能会因系统而异。
    ```


2. /etc/profile 文件用来干什么

    是一个系统级别的配置文件，它在登录时被读取，并为所有用户设置环境变量和执行系统级别的配置。

    /etc/profile 中的设置**适用于所有用户**

4. source 是什么命令

    source是一个用于在当前Shell环境中执行指定脚本或文件的命令, 它通常用于加载并执行Shell脚本或配置文件，以便在当前Shell会话中使相应的更改生效。

    **或者使用其等效的.（点）命令：**

5. /bin 文件夹用来存放什么相关的文件

    /bin目录（也称为BIN目录）是Linux和Unix系统中的一个重要目录，用于存放系统中最基本和最常用的可执行文件。这些文件通常是系统启动和维护所必需的工具和命令。

    以下是一些在/bin目录下常见的文件：

    /bin/bash：Bash Shell的可执行文件。

    /bin/ls：用于列出目录内容的命令。

    /bin/cp：用于复制文件和目录的命令。

    /bin/mkdir：用于创建目录的命令。

    /bin/rm：用于删除文件和目录的命令。

    /bin/cat：用于显示文件内容的命令。

    /bin/chmod：用于修改文件权限的命令。

    /bin/ping：用于测试网络连接的命令。

    /bin/date：用于显示和修改系统日期和时间的命令。

    /bin/grep：用于在文件中查找匹配模式的命令。

    /bin目录中的文件通常是系统的核心组件，它们被广泛使用并且在几乎所有的Shell环境中可用。这些文件通常被包含在系统的环境变量PATH中，以便可以在任何目录下直接运行它们。


6. `export PATH=$PATH:/usr/local/bin` 这段话是什么意思

   - export：这是一个用于将变量导出为环境变量的关键字。它告诉系统将下面定义的变量PATH导出为环境变量，以便其他程序和命令可以访问它。

   - PATH：这是一个特殊的环境变量，它指定了系统在哪些目录中搜索可执行文件。当你在终端中运行一个命令时，系统会根据PATH变量中列出的目录来查找这个命令的可执行文件。

   - $PATH：这是一个特殊的语法，表示将当前PATH变量的值展开。这样做是为了确保新添加的目录在原有的PATH值的基础上进行扩展。

   - :/usr/local/bin：这是你要添加到PATH变量中的新目录。**冒号（:）用于分隔不同的目录。这段代码的含义是将/usr/local/bin添加到当前PATH值的末尾。**`

7. ~/.bashrc 和 ～/.zshrc都是什么文件

    ~/.bashrc和~/.zshrc是**用户主目录下**的**配置文件**，用于配置Bash和Zsh Shell的**行为**和**环境变量**。

    在**登录到系统时**，Zsh会**自动执行**~/.zshrc文件，并将其中的设置加载到当前Shell会话中。

    你可以运行source ~/.bashrc或source ~/.zshrc命令来重新加载相应的配置文件，使更改立即生效。

8. 如何判断当前会话用的是bash还是zsh

     `echo $0`

9. echo 是如何在命令行中运行起来的

    1. 当你在命令行中输入echo命令，Shell会解析你的输入并识别出你想要执行的命令是echo。

    2. Shell会查找系统中的可执行文件，并根据环境变量PATH中定义的目录进行搜索。默认情况下，echo命令位于/bin目录下。

    3. 一旦Shell找到echo命令的可执行文件，它会在新的子进程中启动该命令。

    4. 子进程中的echo命令会接收命令行中提供的参数，并将它们作为文本进行处理。

    5. echo命令会将接收到的文本作为输出打印到标准输出（通常是终端屏幕）。

   6.  一旦echo命令完成输出，子进程会退出，控制权返回到原始的Shell会话。











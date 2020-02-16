# 1. 安装

# 2. 全局配置

   在桌面鼠标右击选择 `Git Base Here`

   ```
   >> git config --global user.name 'arley'
   >> git config --global user.email 'arley520@126.com'
   ```

# 3. 创建空目录

   `mkdir Luffy`或者鼠标右击新建Luffy文件夹

   ```
   >> mkdir Luffy
   ```

# 4. 进入目录

   ```
   >> cd Luffy
   ```

# 5. Git仓库初始化

   ```
   >> git init
   ```

# 6. 常见命令

## 1 查看当前状态: git status

## 2 添加到缓存区:

    git add 文件名

   git add 文件名1 文件名2

   git add .  (点号 - 添加当前目录到缓存区中)

   3) 提交到版本库: git commit -m "注释内容"

# 7. 版本回退

## 1 查看版本, 确定需要回到的时间点

​	指令: git log

​			  git log --pretty=oneline

## 2 回退操作

指令: git reset --hard 版本编号

## 3 查看历史操作

指令: git reflog

   小结: 
   a) 要想回到过去, 必须先得到commit id,然后通过git rest --hard进行回退
   b) 要想回到未来, 需要使用git reflog进行历史操作查看, 得到最新的commit id
   c) commit id可以至少需要写前4位字符

# 8.远程仓库

## HTTPS方式一

### 1 创建远程目录 

   1) 创建远程目录shop

   2) 复制https链接

### 2 创建本地目录 

   1) 创建本地目录shop

   2) 进入本地shop目录

   3) 使用clone指令克隆线上仓库到本地

 ```
>> git clone 线上仓库地址
 ```

   4) 使用用户名和密码

  5) 在仓库上做对应操作(提交暂存区  提交本地仓库  提交线上仓库  拉取线上仓库)

​		提交到线上仓库指令:  git push










​      
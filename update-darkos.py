import os, time, shutil, sys, subprocess, urllib.request, urllib.error, fnmatch
current_version = "0.87"
url = 'https://raw.githubusercontent.com/ahmad1abbadi/darkos/main/currently%20version.txt'
def remove():
    folder_path = '/data/data/com.termux/files/home'
    for filename in os.listdir(folder_path):
        if fnmatch.fnmatch(filename, '*.tar.xz*'):
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)
            print(f'{filename} has been deleted.')
os.system("am start -n com.termux/.HomeActivity")
os.system("clear")
os.system("python3 $PREFIX/bin/photo.py")
time.sleep(2)   
print("")
print("OS正在关机....")
print("")
print("检查中 🔎.....")
time.sleep(1)
response = urllib.request.urlopen(url)
latest_version = response.read().decode('utf-8').strip()
try:
  if latest_version > current_version:
    print("有可用的更新……正在征信……📥")
    os.system("wget -q --show-progress https://github.com/ahmad1abbadi/darkos/releases/download/beta/AZ.tar.xz")
    os.system("tar -xJf AZ.tar.xz -C $PREFIX/glibc")
    os.system("wget -q --show-progress https://github.com/ahmad1abbadi/darkos/releases/download/beta/darkos.tar.xz")
    os.system("tar -xJf darkos.tar.xz -C /sdcard/")
    os.system("wget -q --show-progress https://github.com/ahmad1abbadi/darkos/releases/download/beta/update.tar.xz")
    os.system("tar -xJf update.tar.xz")
    os.system("rm $PREFIX/bin/darkos.py")
    os.system("rm $PREFIX/bin/update-darkos.py")
    os.system("rm $PREFIX/bin/run-darkos.py")
    os.system("rm $PREFIX/bin/debug-darkos.py")
    os.system("rm $PREFIX/bin/setting-darkos.py")
    os.system("rm $PREFIX/bin/darkos")
    os.system("wget -O run-darkos.py https://raw.githubusercontent.com/ahmad1abbadi/darkos/main/run-darkos.py")
    os.system("wget -O darkos.py https://raw.githubusercontent.com/ahmad1abbadi/darkos/main/darkos.py")
    os.system("wget -O darkos https://raw.githubusercontent.com/ahmad1abbadi/darkos/main/darkos")
    os.system("wget -O debug-darkos.py https://raw.githubusercontent.com/ahmad1abbadi/darkos/main/debug-darkos.py")
    os.system("wget -O setting-darkos.py https://raw.githubusercontent.com/ahmad1abbadi/darkos/main/setting-darkos.py")
    os.system("wget -O update-darkos.py https://raw.githubusercontent.com/ahmad1abbadi/darkos/main/update-darkos.py")
    os.system("chmod +x darkos")
    os.system("mv update-darkos.py darkos.py run-darkos.py debug-darkos.py setting-darkos.py darkos $PREFIX/bin/")
    remove()
    print("更新完成 🎉")
    print("重启中")
    time.sleep(3)
except urllib.error.HTTPError as e:
  if e.code == 404:
    print("无网络连接 😵 重启中.....")
    time.sleep(2)
  else:
    print("无可用更新 ")
    time.sleep(3)
os.system("python3 $PREFIX/bin/run-darkos.py")

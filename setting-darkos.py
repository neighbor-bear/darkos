import os, time, shutil, sys, subprocess, urllib.request, urllib.error
import tarfile
tar_xz_file_path ='/sdcard/darkos/airidosas252builds/wine.tar.xz'
target_folders = ['bin', 'lib', 'lib64', 'share']
destination_dir = '/data/data/com.termux/files/usr/glibc/opt/wine/3/wine'
root_dir = "/data/data/com.termux/files/usr/glibc/opt/temp"
os.system("am start -n com.termux/.HomeActivity")
def uninstall_wine9():
    if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin"):
        os.system("rm -r /data/data/com.termux/files/usr/glibc/opt/wine/1/wine")
        if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/1/.wine"):
            shutil.rmtree('/data/data/com.termux/files/usr/glibc/opt/wine/1/.wine')
def install_wine9():
  os.system("wget -q --show-progress https://github.com/ahmad1abbadi/darkos/releases/download/beta/wine-default.tar.xz")
  os.system("tar -xJf wine-default.tar.xz -C $PREFIX/glibc/opt/wine/1")
  os.remove("wine-default.tar.xz")
def wine_manager():
  os.system("clear")
  photo()
  print("Wine管理 ⚙️")
  print("1) 安装Wine 📥")
  print("2) 卸载Wine 📤")
  print("3) 修复默认的Wine文件 🔧")
  print("4) 返回主菜单 🔙")
  print("")
  choice = input()
  if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "dev":
    print("错误")
    wine_manager()
  elif choice == "1":
    wine_select()
  elif choice == "dev":
    os.system("clear")
    conf_path = "/data/data/com.termux/files/usr/glibc/opt/wine/os.conf"
    print("在我们的Telegram群组中分享日志 ")
    print("要退出开发模式，请终止Termux或按Ctrl + C ")
    exec(open(conf_path).read())
    exec(open('/sdcard/darkos/darkos_dynarec.conf').read())
    os.system("BOX86_LOG=1 BOX86_SHOWSEGV=1 BOX86_DYNAREC_LOG=1 BOX86_DYNAREC_MISSING=1 BOX86_DLSYM_ERROR=1 BOX64_LOG=1 BOX64_SHOWSEGV=1 BOX64_DYNAREC_LOG=1 BOX64_DYNAREC_MISSING=1 WINEDEBUG=warn+all BOX64_DLSYM_ERROR=1 WINEDEBUG=+err taskset -c 4-7 box64 wine explorer /desktop=shell,800x600 $PREFIX/glibc/opt/apps/pc.ex >/sdcard/darkos.log")
  elif choice == "2":
      uninstall_wine()
  elif choice == "3":
      print(" 您真的要修复Wine文件吗？这将删除驱动器C中的所有文件  ")
      print(" yes = y")
      print(" no = n")
      stop = input()
      if stop != "y" and choice != "n":
          print("选择错误，返回主菜单")
          time.sleep(1)
          wine_manager()
      elif stop == "y":
          uninstall_wine9()
          time.sleep(1)
          install_wine9()
          print("默认的Wine已修复....")
          time.sleep(2)
          wine_manager()
      elif stop == "n":
          wine_manager()
  elif choice == "4":
      os.system("python3 $PREFIX/bin/darkos.py")
      os.system("exit")
def photo():
  os.system("python3 $PREFIX/bin/photo.py")
def uninstall_wine():
  os.system("clear")
  photo()
  print("您确定要删除这个Wine版本吗？")
  print("")
  if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/2/wine/bin"):
    print("1) 删除容器2上的Wine")
  if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/3/wine/bin"):
    print("2) 删除容器3上的Wine")
    print(" else) 设置菜单 ⬅️")
    print("")
  choice = input()
  if choice != "1" and choice != "2":
    print("选项错误或为空！")
    wine_manager()
  elif choice == "1" and os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/2/wine/bin"):
    print("正在删除Wine，请稍后……")
    print("")
    uninstall_wine1()
  elif choice == "2" and os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/3/wine/bin"):
    print("正在删除Wine，请稍后……")
    print("")
    uninstall_wine2()
  wine_manager()
def uninstall_wine2():
  if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/3/wine/bin"):
    os.system("rm -r /data/data/com.termux/files/usr/glibc/opt/wine/3/wine")
def uninstall_wine1():
  if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/2/wine/bin"):
    os.system("rm -r /data/data/com.termux/files/usr/glibc/opt/wine/2/wine")
def install_wine2():
  if not os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/2/wine/bin"):
    os.system("wget -q --show-progress https://github.com/ahmad1abbadi/darkos/releases/download/beta/wine2.tar.xz")
    os.system("tar -xJf wine2.tar.xz -C $PREFIX/glibc/opt/wine/2")
    os.remove("wine2.tar.xz")
    conf_path = f"/data/data/com.termux/files/usr/glibc/opt/wine/2/os.conf"
    wine_prefix = f"/data/data/com.termux/files/usr/glibc/opt/wine/2/.wine"
    exec(open(conf_path).read())
    print("创建Wine前缀 💫")
    os.system(f'WINEDLLOVERRIDES="mscoree=disabled" box64 wine64 wineboot &>/dev/null')
    os.system(f'cp -r $PREFIX/glibc/opt/Startxmenu/* "{wine_prefix}/drive_c/ProgramData/Microsoft/Windows/Start Menu"')
    os.system(f'rm "{wine_prefix}/dosdevices/z:"')
    os.system(f'ln -s /sdcard/Download "{wine_prefix}/dosdevices/o:" &>/dev/null')
    os.system(f'ln -s /sdcard/darkos "{wine_prefix}/dosdevices/e:" &>/dev/null')
    os.system(f'ln -s /data/data/com.termux/files "{wine_prefix}/dosdevices/z:"')
    print("安装DXVK+Zink...")
    os.system(f'box64 wine "$PREFIX/glibc/opt/apps/Install OS stuff.bat" &>/dev/null')
    print("完成!")
    print("前缀已完成 🤪 ")
    print("“要选择已安装的Wine，请选择容器2 ")
    time.sleep(3)
    os.system("box64 wineserver -k &>/dev/null")
    wine_manager()
def install_wine3():
    if os.path.exists("/sdcard/darkos/airidosas252builds/wine.tar.xz"):
        os.remove("/sdcard/darkos/airidosas252builds/wine.tar.xz")
    conf_path = f"/data/data/com.termux/files/usr/glibc/opt/wine/3/os.conf"
    wine_prefix = f"/data/data/com.termux/files/usr/glibc/opt/wine/3/.wine"
    exec(open(conf_path).read())
    print("创建Wine前缀 💫")
    if not os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/3/wine/bin/wine64"):
        os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/3/wine/bin/wine $PREFIX/glibc/bin/wine64")
        os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/3/wine/bin/wine $PREFIX/glibc/opt/wine/3/wine/bin/wine64")
    os.system(f'WINEDLLOVERRIDES="mscoree=disabled" box64 wine64 wineboot  >/sdcard/darkos/boot64_log.txt 2>&1')
    os.system(f'cp -r $PREFIX/glibc/opt/Startxmenu/* "{wine_prefix}/drive_c/ProgramData/Microsoft/Windows/Start Menu"')
    os.system(f'rm "{wine_prefix}/dosdevices/z:"')
    os.system(f'ln -s /sdcard/Download "{wine_prefix}/dosdevices/o:" &>/dev/null')
    os.system(f'ln -s /sdcard/darkos "{wine_prefix}/dosdevices/e:" &>/dev/null')
    os.system(f'ln -s /data/data/com.termux/files "{wine_prefix}/dosdevices/z:"')
    print("安装DXVK+Zink中...")
    os.system(f'box64 wine64 "$PREFIX/glibc/opt/apps/Install OS stuff.bat" &>/dev/null')
    print("完成!")
    print("前缀已完成 🤪 ")
    print("“要选择已安装的Wine，请选择容器3 ")
    time.sleep(3)
    os.system("box64 wineserver -k &>/dev/null")
    time.sleep(1)
    wine_manager()
def wine_select():
    os.system("clear")
    photo()
    print("请选择Wine版本:")
    print("")
    if not os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/2/wine/bin"):
        print("")
        print(" 1) 在容器2上安装稳定的Wine")
        print("")
    if not os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/3/wine/bin"):
        print("")
        print(" 2) 在容器3上安装airidosas252构建的Wine版本……请确保您已经将文件重命名为wine.tar.xz")
        print("")
    print(" else) Winr设置菜单 ⬅️")
    print("")
    choice = input()
    if choice != "1" and choice != "2":
        print("选项错误或为空！")
        wine_manager()
    elif choice == "1":
        print("正在下载Wine，请稍候")
        print("")
        install_wine2()
    elif choice == "2":
        print("正在安装airidosas252构建的Wine，请稍候.....")
        print("")
        if not os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/3/wine/bin"):
            if os.path.exists("/sdcard/darkos/airidosas252builds/wine.tar.xz"):
                os.system("tar -xJf /sdcard/darkos/airidosas252builds/wine.tar.xz -C $PREFIX/glibc/opt/temp")
            search_and_move_folders(root_dir, target_folders, destination_dir)
        install_wine3()
        time.sleep(1)
    wine_manager()
def search_and_move_folders(root_dir, target_folders, destination_dir):
    for root, dirs, files in os.walk(root_dir):
        for folder in dirs:
            if folder in target_folders:
                source_path = os.path.join(root, folder)
                destination_path = os.path.join(destination_dir, folder)
                if not os.path.exists(destination_path):
                    shutil.move(source_path, destination_path)
wine_manager()

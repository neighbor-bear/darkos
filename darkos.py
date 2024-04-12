import os
import re
import subprocess
import time
import threading
import shutil
import sys, urllib.request, urllib.error
current_version = "0.87"
url = 'https://raw.githubusercontent.com/ahmad1abbadi/darkos/main/currently%20version.txt'
def start_darkos():
    os.system("clear")
    if "LD_PRELOAD" in os.environ:
        del os.environ["LD_PRELOAD"]
    print("启动中")
    os.system("termux-x11 :0 &>/dev/null &")
    os.system('pulseaudio --start --load="module-native-protocol-tcp auth-ip-acl=127.0.0.1 auth-anonymous=1" --exit-idle-time=-1 &>/dev/null')
def wine_container():
    os.system("clear")
    photo()
    print("选择Wine容器:")
    
    wine_paths = {
        "1": "/data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin",
        "2": "/data/data/com.termux/files/usr/glibc/opt/wine/2/wine/bin",
        "3": "/data/data/com.termux/files/usr/glibc/opt/wine/3/wine/bin"
    }
    
    for key, path in wine_paths.items():
        if os.path.exists(path):
            if key == "1":
                print("1) wine 1")
            if key == "2":
                print("2) wine 2")
            if key == "3":
                print("3) wine 3")
    
    print("else)返回主菜单 👑")
    print("")
    
    prefix_path = input("请输入你的选择: ")
    
    if prefix_path not in wine_paths.keys():
        print("选项不正确或为空！")
        time.sleep(1)
        main_menu()
    else:
        conf_path = f"/data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/os.conf"
        wine_prefix = f"/data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/.wine"
        os.system("chmod +x $PREFIX/glibc/bin/box86")
        os.system("chmod +x $PREFIX/glibc/bin/box64")
        os.system(f"chmod +x /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine")
        os.system(f"chmod +x /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wineserver")
        os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine $PREFIX/glibc/bin/wine")
        if not os.path.exists(f"/data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine64"):
            os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine $PREFIX/glibc/bin/wine64")
            os.system(f"chmod +x /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine64")
            os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine $PREFIX/glibc/opt/wine/{prefix_path}/wine/bin/wine64")
        else:
            os.system(f"chmod +x /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine64")
            os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine64 $PREFIX/glibc/bin/wine64")
        os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wineserver $PREFIX/glibc/bin/wineserver")
        os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wineboot $PREFIX/glibc/bin/wineboot")
        os.system(f"ln -sf /data/data/com.termux/files/us/glibc/opt/wine/{prefix_path}/wine/bin/winecfg $PREFIX/glibc/bin/winecfg")
        #os.system("ln -sf /var/lib/dbus/machine-id /etc/machine-id")
        os.environ.pop('LD_PRELOAD', None)
        ### AZ DARK 
        if os.path.exists(conf_path):
            exec(open(conf_path).read())
        if not os.path.exists(wine_prefix):
            print("正在创建Wine前缀 💫")
            #if os.path.exists(f"/data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/lib/wine/i386-windows/shell32-bak.dll"):
                #os.system(f"mv /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/lib/wine/i386-windows/shell32-bak.dll /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/lib/wine/i386-windows/shell32.dll")
                #os.system(f"mv /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/lib/wine/x86_64-windows/shell32-bak.dll /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/lib/wine/x86_64-windows/shell32.dll")
                #os.system(f"mv /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/lib64/wine/x86_64-windows/shell32-bak.dll /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/lib64/wine/x86_64-windows/shell32.dll")
            os.system(f'WINEDLLOVERRIDES="mscoree=disabled" box64 wine64 wineboot &>/dev/null')
            os.system(f'cp -r $PREFIX/glibc/opt/Startxmenu/* "{wine_prefix}/drive_c/ProgramData/Microsoft/Windows/Start Menu"')
            os.system(f'rm "{wine_prefix}/dosdevices/z:"')
            os.system(f'ln -s /sdcard/Download "{wine_prefix}/dosdevices/o:" &>/dev/null')
            os.system(f'ln -s /sdcard/darkos "{wine_prefix}/dosdevices/e:" &>/dev/null')
            os.system(f'ln -s /data/data/com.termux/files "{wine_prefix}/dosdevices/z:"')
            print("Installing DXVK+Zink...")
            os.system(f'box64 wine "$PREFIX/glibc/opt/apps/Install OS stuff.bat" &>/dev/null')
            print("完成！")
            #os.system("clear") 
            print("前缀创建完成，请享用 🤪 ")
            time.sleep(3)
            os.system("box64 wineserver -k &>/dev/null")
            start_container()
    start_container()
def recreate_32bit():
    os.system("clear")
    photo()
    print("选择wine :")
    
    wine_paths = {
        "1": "/data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin",
        "2": "/data/data/com.termux/files/usr/glibc/opt/wine/2/wine/bin",
        "3": "/data/data/com.termux/files/usr/glibc/opt/wine/3/wine/bin"
    }
    
    for key, path in wine_paths.items():
        if os.path.exists(path):
            if key == "1":
                print("1) wine 1")
            if key == "2":
                print("2) wine 2")
            if key == "3":
                print("3) wine 3")
    
    print("else)返回设置菜单 ")
    print("")
    
    prefix_path = input("请输入你的选择: ")
    
    if prefix_path not in wine_paths.keys():
        change_setting()
    else:
        conf_path = f"/data/data/com.termux/files/usr/glibc/opt/wine/1/os.conf"
        wine_prefix = f"/data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/.wine"
        os.system("chmod +x $PREFIX/glibc/bin/box86")
        os.system("chmod +x $PREFIX/glibc/bin/box64")
        os.system(f"chmod +x /data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin/wine")
        os.system(f"chmod +x /data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin/wine64")
        os.system(f"chmod +x /data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin/wineserver")
        os.system("rm -rf $PREFIX/glibc/bin/wine $PREFIX/glibc/bin/wine64 $PREFIX/glibc/bin/wineserver")
        os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin/wine $PREFIX/glibc/bin/wine")
        os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin/wine64 $PREFIX/glibc/bin/wine64")
        os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin/wineserver $PREFIX/glibc/bin/wineserver")
        os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin/wineboot $PREFIX/glibc/bin/wineboot")
        os.system(f"ln -sf /data/data/com.termux/files/us/glibc/opt/wine/1/wine/bin/winecfg $PREFIX/glibc/bin/winecfg")
        os.environ.pop('LD_PRELOAD', None)
        ### AZ DARK 
        exec(open(conf_path).read())
        def prefix_gstreamer():
            os.environ['WINEPREFIX'] = os.path.expandvars("$PREFIX/glibc/opt/wine/3/.wine")
            print("Fixing wine prefix ....")
            os.system(f'WINEDLLOVERRIDES="mscoree=disabled" box64 wine64 wineboot &>/dev/null')
            os.system(f'cp -r $PREFIX/glibc/opt/Startxmenu/* "{wine_prefix}/drive_c/ProgramData/Microsoft/Windows/Start Menu"')
            os.system(f'rm "{wine_prefix}/dosdevices/z:"')
            os.system(f'ln -s /sdcard/Download "{wine_prefix}/dosdevices/o:" &>/dev/null')
            os.system(f'ln -s /sdcard/darkos "{wine_prefix}/dosdevices/e:" &>/dev/null')
            os.system(f'ln -s /data/data/com.termux/files "{wine_prefix}/dosdevices/z:"')
            print("please wait ..")
            os.system(f'box64 wine "$PREFIX/glibc/opt/apps/Install OS stuff.bat" &>/dev/null')
            print("done...please restart OS")
            time.sleep(1)
            os.system("box64 wineserver -k &>/dev/null")
            main_menu()
        if os.path.exists(wine_prefix):
            shutil.rmtree(wine_prefix)
            time.sleep(1)
            prefix_gstreamer()
        if not os.path.exists(wine_prefix):
            prefix_gstreamer()
def photo():
    os.system("python3 $PREFIX/bin/photo.py")
def check_network_connection():
    try:
        urllib.request.urlopen("http://www.google.com", timeout=5)
        return True
    except urllib.error.URLError:
        return False
def main():
    if not check_network_connection():
        print("无可用的网络连接")
        return
    try:
        response = urllib.request.urlopen(url)
        latest_version = response.read().decode('utf-8').strip()
        if latest_version < current_version:
            os.system("curl -o install https://raw.githubusercontent.com/ahmad1abbadi/darkos/main/installO.sh && chmod +x install && ./install")
        if latest_version > current_version:
            print("有可用更新……请更新DARKOS")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("🙅‍♂️🛜", e)
        else:
            print("出错了，请将这个错误发送给开发者")
def edit_file():
    os.system("clear")
    photo()
    print("")
    print("1) 性能 🚀")
    print("2) 默认 🏍️")
    print("3) 兼容性 🐢")
    print("")
    choice = input("请输入你的选择: ")
    config_path_in = "/sdcard/darkos/darkos_dynarec.conf"
    config_path_out = f"/data/data/com.termux/files/usr/glibc/opt/wine/{choice}/darkos_dynarec.conf"
    if choice not in ["1", "2", "3"]:
        print('错误……请输入一个有效的选择')
        time.sleep(2)
        edit_file()
    else:
        if os.path.exists(config_path_in):
            os.remove(config_path_in)
        shutil.copy(config_path_out, config_path_in)
        print("正在更改设置......")
        time.sleep(1)
        print("完成")
        time.sleep(1)
        main_menu()
def mangohud_vulkan():
    os.system("apt reinstall vulkan-icd-loader-glibc")
    print("正在工作中......请稍候 ")
    os.system("grun -s ldconfig")
def winetricks():
    os.system("clear")
    photo()
    print(" winetricks菜单 : ")
    print("")
    print(" 1) winetricks图形 🖥️")
    print("")
    print(" 2) winetricks功能 🧑‍💻")
    print("")
    print(" else)返回主菜单 👑")
    print("")
    choise = input()
    conf_path = f"/data/data/com.termux/files/usr/glibc/opt/wine/os.conf"
    if choise != "1" and choise != "2":
        print("返回主菜单")
        time.sleep(2)
        main_menu()
    elif choise == "1":
        exec(open(conf_path).read())
        exec(open('/sdcard/darkos/darkos_dynarec.conf').read())
        exec(open('/sdcard/darkos/darkos_custom.conf').read())
        os.system("clear")
        photo()
        print("加载中...... Winetrick")
        print("Winetricks 正在工作，请稍候。如果你想要关闭并返回主菜单，请按 Control+C。加载菜单可能需要一分钟时间。")
        os.system("am start -n com.termux.x11/com.termux.x11.MainActivity &>/dev/null")
        os.system("LD_PRELOAD= WINESERVER=$PREFIX/glibc/bin/wineserver WINE=$PREFIX/glibc/bin/wine64 $PREFIX/glibc/bin/box64 $PREFIX/glibc/bin/bash86 $PREFIX/glibc/bin/winetricks &>/dev/null")
        main_menu()
    elif choise == "2":
        exec(open(conf_path).read())
        exec(open('/sdcard/darkos/darkos_dynarec.conf').read())
        exec(open('/sdcard/darkos/darkos_custom.conf').read())
        os.system("clear")
        photo()
        print("Winetrick功能已准备好在所选容器中使用...")
        print("")
        print("输入:")
        winetrick_verbs = input()
        os.system(f"LD_PRELOAD= WINESERVER=$PREFIX/glibc/bin/wineserver WINE=$PREFIX/glibc/bin/wine64 $PREFIX/glibc/bin/box64 $PREFIX/glibc/bin/bash86 $PREFIX/glibc/bin/winetricks {winetrick_verbs} ")
        print("")
        print("Winetrick 软件包已成功安装...👍 ")
        print("返回主菜单...... 🔁")
        time.sleep(4)
        main_menu()
def start_container():
    start_darkos()
    exec(open('/sdcard/darkos/darkos_dynarec.conf').read())
    os.system("chmod +x $PREFIX/glibc/bin/box86")
    os.system("chmod +x $PREFIX/glibc/bin/box64")
    xrandr_output = os.popen('xrandr').read()
    current_resolution_match = re.search(r'current\s+(\d+) x (\d+)', xrandr_output)

    if current_resolution_match:
        current_resolution = f"{current_resolution_match.group(1)}x{current_resolution_match.group(2)}"
    else:
        current_resolution = "800x600"
    res = current_resolution
    os.system("taskset -c 4-7 box64 wine64 explorer /desktop=shell," + res + " $PREFIX/glibc/opt/apps/run.exe &>/dev/null &")
    os.system("am start -n com.termux.x11/com.termux.x11.MainActivity &>/dev/null")
    os.system("clear")
    os.system("python3 $PREFIX/bin/photo.py")
    print("退出 1️⃣")
    user_input = input("Enter 1 to stop: ")
    if user_input == "1":
        os.system("box64 wineserver -k")
        print("Exiting 👋")
        os.system('pkill -f "app_process / com.termux.x11"')
        os.system('pkill -f pulseaudio')
        print("see you later")
        main_menu()
    main_menu()
        
def uninstall_wine():
    os.system("clear")
    photo()
    print("您确定要删除这个 Wine 版本吗？")
    print("")
    if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin"):
        print("1) 删除 wine 1")
    if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/2/wine/bin"):
        print("2) 删除 wine 2")
    if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/3/wine/bin"):
        print("3) 删除 wine 3")
    print(" else)主菜单 ⬅️")
    print("")
    choice = input()
    if choice != "1" and choice != "2" and choice != "3":
        print("选项不正确或为空！")
        main_menu()
    elif choice == "1" and os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/3/wine/bin"):
        print("正在删除 Wine 1，请稍候")
        print("")
        uninstall_wine9()
    elif choice == "2" and os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/2/wine/bin"):
        print("正在删除 Wine 2，请稍候")
        print("")
        uninstall_wine8()
    elif choice == "3" and os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin"):
        print("正在删除 Wine 3，请稍候")
        print("")
        uninstall_wine7()
    main_menu()
def uninstall_wine9():
    if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin"):
        os.system("rm -r /data/data/com.termux/files/usr/glibc/opt/wine/1/wine")
        if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/1/.wine"):
            shutil.rmtree('/data/data/com.termux/files/usr/glibc/opt/wine/1/.wine')
def recreate_prefix_wineAZ():
    print("选择您想要重新创建前缀的 Wine 版本:")
    print("")
    if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/1/.wine"):
        print(" 1) 在容器中删除前缀 1")
    if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/2/.wine"):
        print(" 2) 在容器中删除前缀 2 ")
    if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/3/.wine"):
        print(" 3) 在容器中删除前缀 3")
    if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/4/.wine"):
        print(" 4) 在容器中删除前缀 4 ")
    if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/5/.wine"):
        print(" 5) 在容器中删除前缀 5")
    print("")
    print(" else)返回设置菜单")
    print("")
    user_input = input()
    if user_input not in ["1", "2", "3", "4", "5"]:
        change_setting()
    elif user_input == "1":
         shutil.rmtree('/data/data/com.termux/files/usr/glibc/opt/wine/1/.wine')
         print(f'done')
    elif user_input == "2":
         shutil.rmtree('/data/data/com.termux/files/usr/glibc/opt/wine/2/.wine')
         print(f'done')
    elif user_input == "3":
         shutil.rmtree('/data/data/com.termux/files/usr/glibc/opt/wine/3/.wine')
         print(f'done')
    elif user_input == "4":
         shutil.rmtree('/data/data/com.termux/files/usr/glibc/opt/wine/4/.wine')
         print(f'done')
    elif user_input == "5":
         shutil.rmtree('/data/data/com.termux/files/usr/glibc/opt/wine/5/.wine')
         print(f'done')
    main_menu()
def check_config_wine():
    config_folder = "/sdcard/darkos"
    exec(open('/sdcard/darkos/darkos_dynarec.conf').read())
def Compile():
    os.system("apt install cmake-glibc make-glibc python-glibc")
    os.system("pkg install -y git; unset LD_PRELOAD; export GLIBC_PREFIX=/data/data/com.termux/files/usr/glibc; export PATH=$GLIBC_PREFIX/bin:$PATH; cd ~/; git clone https://github.com/ptitSeb/box64; cd ~/box64; sed -i 's/\/usr/\/data\/data\/com.termux\/files\/usr\/glibc/g' CMakeLists.txt; sed -i 's/\/etc/\/data\/data\/com.termux\/files\/usr\/glibc\/etc/g' CMakeLists.txt; mkdir build; cd build; cmake --install-prefix $PREFIX/glibc .. -DARM_DYNAREC=1 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DBAD_SIGNAL=ON -DSD845=ON; make -j8; make install")
def install_wine9():
    os.system("wget -q --show-progress https://github.com/ahmad1abbadi/darkos/releases/download/beta/wine-default.tar.xz")
    os.system("tar -xJf wine-default.tar.xz -C $PREFIX/glibc/opt/wine/1")
    os.remove("wine-default.tar.xz")

def change_setting():
    os.system("clear")
    photo()
    print("设置 ⚙️")
    print("1) 更新 OS 👑")
    print("2) Wine管理 🍷")
    print("3) 更改box86-box64版本 📥")
    print("4) 删除前缀 🪡")
    print("5) 修复dynarec设置 🧩")
    print("6) 调试模式 🔧")
    print("7) 为非 wow64 Wine 修复前缀 ♻️")
    print("8) CPU超频 🔥 (在某些设备中需要获取root权限)")
    print("9) 如果 MangoHUD 与您的设备不兼容，请修复它 🎭")
    print("10) winetricks ⛑️")
    print("else) Back 🔙")
    print("")
    choice = input()
    if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8" and choice != "9" and choice != "10" and choice != "dev":
        print("...........")
        main_menu()
    elif choice == "3":
        box_version()
    elif choice == "dev":
        os.system("clear")
        print("将日志文件分享到我们的 Telegram 群组 ")
        print("开发者模式")
        os.system("BOX86_LOG=1 BOX86_SHOWSEGV=1 BOX86_DYNAREC_LOG=1 BOX86_DYNAREC_MISSING=1 BOX86_DLSYM_ERROR=1 BOX64_LOG=1 BOX64_SHOWSEGV=1 BOX64_DYNAREC_LOG=1 BOX64_DYNAREC_MISSING=1 WINEDEBUG=warn+all BOX64_DLSYM_ERROR=1 WINEDEBUG=+err taskset -c 4-7 box64 wine64 explorer /desktop=shell,800x600 $PREFIX/glibc/opt/apps/pc.ex >/sdcard/darkos.log")
    elif choice == "1":
        print("")
        print("关闭操作系统....")
        print("")
        print("检查中 🔎.....")
        time.sleep(1)
        response = urllib.request.urlopen(url)
        latest_version = response.read().decode('utf-8').strip()
        try:
            if latest_version > current_version:
                print("更新可用......正在更新......📥")
                os.system("rm $PREFIX/bin/update-darkos.py")
                os.system("wget -O update-darkos.py https://raw.githubusercontent.com/ahmad1abbadi/darkos/main/update-darkos.py")
                os.system("mv update-darkos.py $PREFIX/bin/")
                os.system("python3 $PREFIX/bin/update-darkos.py")
                time.sleep(3)
                change_setting()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                os.system("clear")
                print("无网络连接 😵 返回设置")
                time.sleep(3)
                change_setting()
        else:
            print("没有可用的更新 ")
            time.sleep(3)
            change_setting()
    elif choice == "2":
        os.system("python3 $PREFIX/bin/setting-darkos.py")
    elif choice == "6":
        os.system("python3 $PREFIX/bin/debug-darkos.py")
    elif choice == "9":
        print("fixing......")
        mangohud_vulkan()
        time.sleep(2)
        print("done 👍")
        time.sleep(1)
        change_setting()
    elif choice == "r":
        print("通过Telegram频道联系开发者......(https://t.me/DARKOS4android)")
        back = input("🔙 = 1")
        if back == "1":
            change_setting()
    elif choice == "4":
        recreate_prefix_wineAZ()
    elif choice == "5":
        edit_file()
    elif choice == "7":
        recreate_32bit()
    elif choice == "10":
        winetricks()
    elif choice == "8":
        os.system("clear")
        photo()
        print("加载中.........")
        reload()
        new_sesson()
        print("安装Python包")
        os.system('pkg install python vulkan-tools python-pip coreutils &> /dev/null')
        print("")
        os.system('pip install aiofiles psutil blessings &> /dev/null')
        print("python包.... 100%")
        print("")
        print("开始超频 💥")
        time.sleep(3)
        print("")
        print("检查新会话以获取更多信息 👀 ")
        time.sleep(5)
        change_setting()
def box_version():
  os.system("clear")
  photo()
  print("选择Box版本:")
  print("")
  print("1) SAFE-BOX")
  print("2) 编译并更新BOX64")
  print("3) BOX86针对Wine的非WOW64版本 ")
  print("else) 取消和返回")
  print("")
  choice = input()
  if choice != "1" and choice != "2" and choice != "3":
    change_setting()
  elif choice == "1":
    os.remove("$PREFIX/glibc/bin/box64")
    os.remove("$PREFIX/glibc/bin/box86")
    os.system("tar -xJf $PREFIX/glibc/opt/box/safe-box.tar.xz -C $PREFIX/glibc/bin/")
    os.system("chmod +x $PREFIX/glibc/bin/box86")
    os.system("chmod +x $PREFIX/glibc/bin/box64") 
    change_setting()
  elif choice == "2":
    os.system("rm $PREFIX/bin/box64")
    print("compiling....")
    os.system("apt install cmake-glibc make-glibc python-glibc -y &>/dev/null")
    Compile()
    os.system("mv //data/data/com.termux/files/home/box64/build/box64 $PREFIX/bin/")
    os.system("chmod +x $PREFIX/glibc/bin/box64")
    shutil.rmtree('/data/data/com.termux/files/home/box64')
    print("完成")
    time.sleep(2)
    change_setting()
  elif choice == "3":
    os.system("wget https://github.com/ahmad1abbadi/darkos/releases/download/beta/box.tar.xz")
    os.remove("$PREFIX/glibc/bin/box64")
    os.remove("$PREFIX/glibc/bin/box86")
    os.system("tar -xJf box.tar.xz -C $PREFIX/glibc/bin/")
    os.system("chmod +x $PREFIX/glibc/bin/box86")
    os.system("chmod +x $PREFIX/glibc/bin/box64")
    change_setting()
def reload():
    file_path = os.path.expanduser("~/.termux/termux.properties")
    with open(file_path, "r") as file:
        lines = file.readlines()
    with open(file_path, "w") as file:
        for line in lines:
            if line.startswith("# allow-external-apps = true"):
                line = line.replace("# ", "")
            file.write(line)
            #print(f"File updated: {file_path}")
    os.system("termux-reload-settings")
def new_sesson():
    os.system("am startservice --user 0 -n com.termux/com.termux.app.RunCommandService \
    -a com.termux.RUN_COMMAND \
    --es com.termux.RUN_COMMAND_PATH '/data/data/com.termux/files/usr/bin/python' \
    --esa com.termux.RUN_COMMAND_ARGUMENTS '/data/data/com.termux/files/usr/bin/cpu_boost.py' \
    --es com.termux.RUN_COMMAND_WORKDIR '/data/data/com.termux/files/home' \
    --ez com.termux.RUN_COMMAND_BACKGROUND 'false' \
    --es com.termux.RUN_COMMAND_SESSION_ACTION '1' &> /dev/null ")
def main_menu():
    os.system("clear")
    photo()
    print("欢迎进入DarkOS安全模式")
    print("")
    print("选择你需要做的事情:")
    print("1) 以安全模式启动Dark OS 🚑")
    print("2) 设置 ⚙️")
    print("3) 退出安全模式 🚪")
    print("4) “终止Dark OS并退出到终端 😭")
    print("")
    main()
    choice = input()
    if choice != "1" and choice != "2" and choice != "3" and choice != "4":
        print("wrong")
        main_menu()
    elif choice == "1":
        wine_container()
    elif choice == "2":
        change_setting()
    elif choice == "3":
        print("")
        os.system("clear")
        photo()
        print("")
        print(" 正在重启.....")
        time.sleep(1)
        print("")
        subprocess.run(["bash", "darkos"])
    elif choice == "4":
        print("")
        os.system("clear")
        photo()
        print("")
        print("再见 😭")
        os.system('pkill -f "app_process / com.termux.x11"')
        os.system('pkill -f pulseaudio')
        os._exit(0)
start_darkos()
check_config_wine()
main_menu()

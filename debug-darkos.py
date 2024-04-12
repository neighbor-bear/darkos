import os
import re
import subprocess
import time
import threading
exec(open('/data/data/com.termux/files/usr/glibc/opt/wine/os.conf').read())
exec(open('/sdcard/darkos/darkos_dynarec.conf').read())
exec(open('/sdcard/darkos/darkos_dynarec_box86.conf').read())
exec(open('/sdcard/darkos/darkos_custom.conf').read())
os.environ["BOX64_TRACE_FILE"]="/sdcard/darkos/trace/trace-%pid.txt"
os.system("BOX64_LOG=1 BOX64_SHOWSEGV=1 BOX64_DYNAREC_LOG=1 BOX64_DYNAREC_MISSING=1 WINEDEBUG=warn+all BOX64_DLSYM_ERROR=1 WINEDEBUG=+err taskset -c 4-7 box64 wine64 explorer /desktop=shell,800x600 $PREFIX/glibc/opt/apps/DARKOS_configuration.exe >/sdcard/darkos/darkos.log 2>&1 &")
os.system("am start -n com.termux.x11/com.termux.x11.MainActivity &>/dev/null")
os.system("clear")
os.system("python3 $PREFIX/bin/photo.py")
def recreate_prefix():
    os.system("clear")
    os.system("python3 $PREFIX/bin/photo.py")
    print("选择Wine以重建:")
    
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
    
    print("Else) 返回设置菜单 ")
    print("")
    
    prefix_path = input("输入你的选择: ")
    
    if prefix_path not in wine_paths.keys():
      print("未找到前缀，返回调试菜单")
      time.sleep(1)
      reboot()
    else:
      conf_path = f"/data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/os.conf"
      wine_prefix = f"/data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/.wine"
      os.system("chmod +x $PREFIX/glibc/bin/box86")
      os.system("chmod +x $PREFIX/glibc/bin/box64")
      os.system(f"chmod +x /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine")
      os.system(f"chmod +x /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine64")
      os.system(f"chmod +x /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wineserver")
      os.system("patchelf --force-rpath --set-rpath $PREFIX/glibc/lib --set-interpreter $PREFIX/glibc/lib/ld-linux-aarch64.so.1 $PREFIX/glibc/bin/box64")
      os.system("patchelf --force-rpath --set-rpath $PREFIX/glibc/lib32 --set-interpreter $PREFIX/glibc/lib32/ld-linux-armhf.so.3 $PREFIX/glibc/bin/box86")
      os.system("rm -rf $PREFIX/glibc/bin/wine $PREFIX/glibc/bin/wine64 $PREFIX/glibc/bin/wineserver")
      os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine $PREFIX/glibc/bin/wine")
      os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine64 $PREFIX/glibc/bin/wine64")
      os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wineserver $PREFIX/glibc/bin/wineserver")
      os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wineboot $PREFIX/glibc/bin/wineboot")
      os.system(f"ln -sf /data/data/com.termux/files/us/glibc/opt/wine/{prefix_path}/wine/bin/winecfg $PREFIX/glibc/bin/winecfg")
      os.environ.pop('LD_PRELOAD', None)
      def prefix_gstreamer():
        print("创建Wine前缀 💫")
        os.environ.pop('BOX86_DYNAREC_BIGBLOCK', None)
        os.environ.pop('BOX64_DYNAREC_BIGBLOCK', None)
        os.environ.pop('WINEESYNC', None)
        os.environ.pop('WINEESYNC_TERMUX', None)
        os.environ.pop('BOX86_DYNAREC_CALLRET', None)
        os.environ.pop('BOX64_DYNAREC_CALLRET', None)
        os.system(f'WINEDLLOVERRIDES="mscoree=disabled,winegstreamer=disable" box64 wine64 wineboot &>/dev/null')
        os.system(f'cp -r $PREFIX/glibc/opt/Startxmenu/* "{wine_prefix}/drive_c/ProgramData/Microsoft/Windows/Start Menu"')
        os.system(f'rm "{wine_prefix}/dosdevices/z:"')
        os.system(f'ln -s /sdcard/Download "{wine_prefix}/dosdevices/o:" &>/dev/null')
        os.system(f'ln -s /sdcard/darkos "{wine_prefix}/dosdevices/e:" &>/dev/null')
        os.system(f'ln -s /data/data/com.termux/files "{wine_prefix}/dosdevices/z:"')
        print("安装DXVK+Zink...")
        os.system(f'box64 wine "$PREFIX/glibc/opt/apps/Install OS stuff.bat" &>/dev/null')
        print("完成!") 
        print("前缀已完成 🤪 ")
        time.sleep(1)
        os.system("box64 wineserver -k &>/dev/null")
        print("操作系统将以调试模式启动，如有任何问题，请查看日志文件 ")
        time.sleep(2)
        os.system("BOX86_LOG=2 BOX86_SHOWSEGV=1 BOX86_DYNAREC_LOG=1 BOX86_DYNAREC_MISSING=1 BOX86_DLSYM_ERROR=1 BOX64_LOG=3 BOX64_SHOWSEGV=1 BOX64_DYNAREC_LOG=1 BOX64_DYNAREC_MISSING=1 BOX64_DLSYM_ERROR=1 taskset -c 4-7 box64 wine explorer /desktop=shell,800x600 $PREFIX/glibc/opt/apps/pc.ex >/sdcard/darkos.log 2>&1 &")
        os.system("am start -n com.termux.x11/com.termux.x11.MainActivity &>/dev/null")
        os.system("clear")
        os.system("python3 $PREFIX/bin/photo.py")
        print("退出 1️⃣")
        user_input = input("输入1以停止: ")
        if user_input == "1":
          os.system("box64 wineserver -k")
          print("正在退出 👋")
          os.system('pkill -f "app_process / com.termux.x11"')
          os.system('pkill -f pulseaudio')
          reboot()
        if os.path.exists(wine_prefix):
          shutil.rmtree(wine_prefix)
          time.sleep(1)
          prefix_gstreamer()
      if not os.path.exists(wine_prefix):
        prefix_gstreamer()
def reboot():
  os.system("clear")
  os.system("python3 $PREFIX/bin/photo.py")
  print(" 你正在调试模式中……选择你需要做的事情 :")
  print(" 注意：此选项仅在安全模式下可用.")
  print("")
  print("1) 使用box64和box86以32位模式重启调试")
  print("2) 重新创建前缀 ")
  print("3) 重启 os")
  print("4) 终止所有进程并退出")
  choice = input()
  if choice != "1" and choice != "2" and choice != "3" and choice != "4":
    reboot()
  elif choice == "1":
    exec(open('/data/data/com.termux/files/usr/glibc/opt/wine/os.conf').read())
    exec(open('/sdcard/darkos/darkos_dynarec.conf').read())
    exec(open('/sdcard/darkos/darkos_custom.conf').read())
    os.system("BOX64_LOG=1 BOX64_SHOWSEGV=1 BOX64_DYNAREC_LOG=1 BOX64_DYNAREC_MISSING=1 WINEDEBUG=warn+all BOX64_DLSYM_ERROR=1 WINEDEBUG=+err taskset -c 4-7 box64 wine explorer /desktop=shell,800x600 $PREFIX/glibc/opt/apps/DARKOS_configuration.exe >/sdcard/darkos/darkos.log 2>&1 &")
    os.system("am start -n com.termux.x11/com.termux.x11.MainActivity &>/dev/null")
    reboot()
  elif choice == "2":
    recreate_prefix()
  elif choice == "3":
      print("")
      os.system("box64 wineserver -k &>/dev/null")
      print("重启中.........")
      os.system('pkill -f "app_process / com.termux.x11"')
      os.system('pkill -f pulseaudio')
      time.sleep(1)
      subprocess.run(["bash", "darkos"])
  elif choice == "4":
      os.system("box64 wineserver -k")
      os.system('pkill -f "app_process / com.termux.x11"')
      os.system('pkill -f pulseaudio')
      print("正在关机........")
      time.sleep(1)
      os.system("am startservice -a com.termux.service_stop com.termux/.app.TermuxService")
reboot()        
      
    

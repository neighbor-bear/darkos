![logo](img/logo.png "logo")

**Darkos**是一个可在 [Termux](https://github.com/termux/termux-app) 原生 GLIBC 中运行 Windows x86_64 应用程序和游戏的项目
它在安卓上利用 [Box86](https://github.com/ptitSeb/box86)
和 [Box64](https://github.com/ptitSeb/box86)
运行 [Wine](https://www.winehq.org/) 。

# 安装指南:
1. 安装
[Termux](https://f-droid.org/repo/com.termux_118.apk),
[Termux-X11](https://github.com/ahmad1abbadi/extra/releases/download/apps/termux-x11.apk) 和
[Input Bridge v0.1.9.9](https://github.com/ahmad1abbadi/extra/releases/download/apps/InputBridge_v0.1.9.9.apk) 或者 [Input Bridge v0.0.7](https://github.com/ahmad1abbadi/extra/releases/download/apps/input+bridge+0.0.7.apk)

2. 打开 Termux 并粘贴以下命令：
```bash
curl -o install https://raw.githubusercontent.com/ahmad1abbadi/darkos/main/installOS.sh && chmod +x install && ./install
```

**本人汉化了当前项目的部分脚本，如需体验，请打开 Termux 并粘贴以下命令：**

```bash
curl -o install https://raw.githubusercontent.com/neighbor-bear/darkos/main/installOS.sh && chmod +x install && ./install
```



3. 安装完成后，**Darkos** 将自动启动。
   请记住，每次打开 Termux 时，Darkos 都会自动启动。
   
   要在 4 秒内退出 **Darkos** 并正常使用 Termux，请按 '1'。否则，**Darkos** 将启动并运行 Wine + Termux-X11。
   
# 功能及特性:
1. 支持Gstreamer，这是运行诸如以下游戏所必需的：
* 生化危机7
* 鬼泣5
* 邪恶之中
2. 专用配置应用程序

  还有更多内容，您可以自行探索。
# 配置:

## Box64/Box86 配置 + Dynarec
配置可以通过 Darkos 配置应用程序轻松完成。只需修改 Box 选项，点击“应用”，然后点击“重启”即可应用更改。

关于 dynarec 变量的更多信息，请参阅： [Box64 usage](https://github.com/ptitSeb/box64/blob/main/docs/USAGE.md) 和 [Box86 usage](https://github.com/ptitSeb/box86/blob/master/docs/USAGE.md)

## 更新 OS
这个选项将 Darkos 更新到最新版本。

## Wine管理 
您可以在 Darkos 配置中内嵌的 Wine 管理器中安装或卸载 Wine。只需选择“Wine 管理”选项即可。

要选择 Wine 容器，请在 Darkos 配置中使用容器下拉菜单，然后点击“更改容器”。


## 调试模式
此模式将 Wine 和 Box64 的调试信息记录到位于 /sdcard/darkos/darkos.log 的日志文件中。您可以将此文件分享到我们的 Telegram 群组中。

## 切换 Mangohud
Mangohud 是一个屏幕显示（OSD）工具，用于展示有用的信息，如帧率（FPS）、CPU 使用率、GPU 负载以及 GPU 温度。

目前，要查看 GPU 负载和温度统计信息，您需要在 Termux 中运行以下命令来禁用 SELinux：
```
su -c setenforce 0
```
重新启用SELinux：

```
su -c setenforce 1
```

## GPU Driver Changer（GPU驱动管理）
这个选项允许你更改GPU驱动程序

## Switch IB(切换IB)
这个切换开关可以让你在0.1.9.9版本和0.0.7版本的输入桥之间切换,以此来选择最适合你的版本

## Kill Services（杀死进程）
使用这个切换开关来结束services.exe进程，无需打开任务管理器

## Hit F5 key（按F5键）
这将打开任务管理器

## DXVK changer （更改DXVK）
这个选项允许你选择DXVK的版本，以便为特定游戏选择最合适的版本

## Install Tweaks（安装Tweaks）
这个选项允许你安装Wine小工具，如应用程序、DLL文件和字体

## Personalize（个性化）
你可以更改Wine桌面的主题、背景或分辨率

## Termux-X11 resolution （Termux-X11 分辨率）
备用分辨率仅在无法自动检测X11分辨率时使用。默认的备用分辨率是800x600

## Termux and termux-x11 preferences（Termux 和 termux-x11偏好设置）
### Termux的推荐设置:
* `Allow apps to open new windows while running in the background`
* `Allow apps to display pop-up windows`

### Termux-X11的推荐设置:
* `Display resolution mode` exact
* `Display resolution` 1280x720
* `Reseed Screen While Soft Keyboard is open` OFF
* `Fullscreen on device display` ON
* `Force Landscape orientation` ON
* `Hide display cutout` ON
* `Show additional keyboard` OFF
* `Prefer scancodes when possible` ON
* `Enable Accessibility service for intercepting
system shortcuts manually.` 在Android的辅助功能菜单中启用Termux-X11，以便您可以无障碍地使用外接键盘（有线/无线）。
* `Enable Accessibility service for intercepting system shortcuts automatically.` ON

## Controls（控制器）
为了使用触摸控制，需要安装Input Bridge应用。

## Support status（支持的安卓版本）
**建议使用Android 10或更高版本。

### Device（设备）
* 大多数配备Mali GPU的Android手机可以使用Mesa VirGL [Mesa VirGL](https://github.com/alexvorxx/Mesa-VirGL) 来运行DirectX 9游戏。建议使用配备Adreno 6xx或Adreno 7xx的骁龙设备，以获得Turnip和 [DXVK](https://github.com/doitsujin/dxvk) 的最佳性能和兼容性。

### Root
* 无需获取root权限

## Known issues（已知问题）
* 在使用Wine或编译box64时，Termux应用可能会显示信号9，这种情况下你需要禁用phantom进程。

## To-do list（待办事项清单）
* virgl
* 对非骁龙芯片的支持
  
## 支持Darkos 
#
非常感谢我们的测试人员：

GhostDz36

#
衷心感谢：

[airidosas252](https://github.com/airidosas252) 为我们构建的Turnip和Wine版本。

#
特别感谢pititSeb、Maxython、glibc-runner、hardray、Tωaik以及其他人的帮助。

[Darkos telegram group](https://t.me/DARKOS4android)

## 第三方应用程序

[glibc-packages](https://github.com/termux-pacman/glibc-packages)

[Box64](https://github.com/ptitSeb/box64)

[Box86](https://github.com/ptitSeb/box86)

[DXVK](https://github.com/doitsujin/dxvk)

[DXVK-ASYNC](https://github.com/Sporif/dxvk-async)

[DXVK-GPLASYNC](https://gitlab.com/Ph42oN/dxvk-gplasync)

[VKD3D](https://github.com/lutris/vkd3d)

[D8VK](https://github.com/AlpyneDreams/d8vk)

[Termux-app](https://github.com/termux/termux-app)

[Termux-x11](https://github.com/termux/termux-x11)

[Wine](https://wiki.winehq.org/Licensing)

[wine-ge-custom](https://github.com/GloriousEggroll/wine-ge-custom)

[Mesa](https://docs.mesa3d.org/license.html)

[Mesa-VirGL](https://github.com/alexvorxx/Mesa-VirGL)

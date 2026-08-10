import subprocess, os, shutil, time, urllib.request
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
clear()

adb_check = shutil.which("adb")
if adb_check:
    print(f"ADB found at: {adb_check}")
    time.sleep(1)
else:
    print("ADB NOT available, please install it or enter it into your path!")
    time.sleep(1.6)
    sys.exit(1)

root_result = subprocess.run(["adb", "shell", "su", "-c", "whoami"], capture_output=True, check=True, text=True)

app_mapping = {
    "moe.rukamori.archivetune": "ArchiveTune",
    "org.localsend.localsend_app": "Localsend",
    "com.topjohnwu.magisk": "Magisk",
    "com.looker.droidify": "Droidify",
    "com.aurora.store": "Aurora Store",
}

def applist():
    print("\nApplications Insatalled:")
    result = subprocess.run(["adb", "shell", "pm", "list", "packages"], capture_output=True, text=True)
    installed_apps_str = result.stdout
    for package, display_name in app_mapping.items():
        if package in installed_apps_str:
            print(f"{display_name} -- {package}")

applist()
confirm = input("\nInstall Aurora Store? It is a FOSS Google Play Store alternative that has every app that the Play Store has! (y/n) ")
if confirm.lower() != "y":
    verbose_clear()
else:
    verbose_clear()
    print(f"\nGrabbing Aurora APK From Web!")
    url = "https://f-droid.org/repo/com.aurora.store_76.apk"
    file = "Aurora_Store.apk"
    urllib.request.urlretrieve(url, file)
    print(f"\nInstalling Aurora Store!")
    if args.verbose:
        subprocess.run(["adb", "install", "-r", "Aurora_Store.apk"])
    else:
        subprocess.run(["adb", "install", "-r", "Aurora_Store.apk"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    verbose_clear()

applist()
confirm = input("\nInstall Droidify? It Is An Open Source App That Is Basically Just A Pretty F-Droid With More Sources. (y/n) ")
if confirm.lower() != "y":
    verbose_clear()
else:
    verbose_clear()
    print("\nGrabbing Droidify APK From Web!")
    url = "https://github.com/Droid-ify/client/releases/download/v0.7.4/app-release.apk"
    file = "Droidify.apk"
    urllib.request.urlretrieve(url, file)
    
    print("\nInstalling Droidify!")
    if args.verbose:
        subprocess.run(["adb", "install", "-r", "Droidify.apk"])
    else:
        subprocess.run(["adb", "install", "-r", "Droidify.apk"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    verbose_clear()
 
applist()
confirm = input("\nInstall ArchiveTune? [Youtube Music Client] (y/n) ")
if confirm.lower() != "y":
    verbose_clear()
else:
    verbose_clear()
    print("\nGrabbing ArchiveTune APK From Web!")
    url = "https://github.com/rukamori/ArchiveTune/releases/download/v14.1.0/app-foss-mobile-universal-release.apk"
    file_name = "ArchiveTune.apk"
    urllib.request.urlretrieve(url, file_name)
    
    print("\nInstalling ArchiveTune!")
    if args.verbose:
        subprocess.run(["adb", "install", "-r", "ArchiveTune.apk"])
    else:
        subprocess.run(["adb", "install", "-r", "ArchiveTune.apk"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    verbose_clear()
    
applist()
confirm = input("\nInstall Localsend? [Basically Open Source Android AirDrop] (y/n) ")
if confirm.lower() != "y":
    verbose_clear()
else:
    verbose_clear
    print("\nGrabbing Localsend APK From Web!")
    url = "https://github.com/localsend/localsend/releases/download/v1.17.0/LocalSend-1.17.0-android-arm64v8.apk"
    file = "Localsend.apk"
    urllib.request.urlretrieve(url, file)
    
    print("\nInstalling Localsend!")
    if args.verbose:
        subprocess.run(["adb", "install", "-r", "Localsend.apk"])
    else:
        subprocess.run(["adb", "install", "-r", "Localsend.apk"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        verbose_clear()
    
if root_result.stdout.strip() != "root":
    applist()
    confirm = input("\nInstall Magisk? (For Rooting, If You Don't Have OEM Unlocking, Don't Even Bother. (y/n) ")
    if confirm.lower() != "y":
        verbose_clear()
    else:
        verbose_clear()
        print("\nGrabbing Magisk APK From Web!")
        url = "https://github.com/topjohnwu/Magisk/releases/download/v30.7/Magisk-v30.7.apk"
        file = "Magisk.Apk"
        urllib.request.urlretrieve(url, file)
    
        print("\nInstalling Magisk!")
        if args.verbose:
            subprocess.run(["adb", "install", "-r", "Magisk.apk"])
        else:
            subprocess.run(["adb", "install", "-r", "Magisk.apk"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        verbose_clear()
if "root" in root_result.stdout:
    applist()
    confirm = input("\nInstall Bind Hosts? (An app you can use with root to disable ads at the system level while freeing up your private DNS settings. (y/n) ")
    if confirm.lower() != "y":
        verbose_clear()
    else:
        verbose_clear()
        print("\nGrabbing Bind Hosts Zip From Web!")
        url = "https://github.com/bindhosts/bindhosts/releases/download/v2.1.4/bindhosts.zip"
        file = "Bind_Hosts.zip"
        urllib.request.urlretrieve(url, file)
                
        print("\nYou'll have to flash this as a zip through Magisk, it isn't a standalone APK.")
        verbose_clear()

applist()


import subprocess, os, shutil, time, urllib.request, json, argparse, sys
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
clear()
def verboseClear()
    if args.verbose:
        pass
    else:
        clear()

def main():
    parser = argparse.ArgumentParser(
            description="Generic Debloater",
            epilog="Example: python master.py --verbose",
    )

    parser.add_argument(
            "--verbose",
            action="store_true",
            help="Shows ALL logs and doesn't clear the terminal",
    )
    args = parser.parse_args()
    
    adb_check = shutil.which("adb")
    if adb_check:
        print(f"ADB found at: {adb_check}")
        time.sleep(1)
    else:
        print("ADB NOT available, please install it or enter it into your path!")
        time.sleep(1.6)
        sys.exit(1)
    subprocess.run(
            [
                "adb",
                "devices",
            ],
        )
    deviceChoice = input("Choose your device by typing out the model name, then pressing enter. (like XYZ789)\n")
    rootResult = subprocess.run(["adb", "-s", deviceChoice, "shell", "su", "-c", "whoami"], capture_output=True, check=True, text=True)
    app_mapping = {
        "moe.rukamori.archivetune": "ArchiveTune",
        "org.localsend.localsend_app": "Localsend",
        "com.topjohnwu.magisk": "Magisk",
        "com.looker.droidify": "Droid-ify",
        "sh.haven.app": "Haven SSH Client",
    }
    
    def applist():
        print("\nApplications Installed:")
        result = subprocess.run(
            [
                "adb",
                "-s",
                deviceChoice,
                "shell",
                "pm",
                "list",
                "packages",
            ],
            capture_output=True,
            text=True,
        )
        installed_apps_str = result.stdout
        for package, display_name in app_mapping.items():
            if package in installed_apps_str:
                print(f"{display_name} -- {package}")
    
    applist()
    confirm = input(
        "\nInstall Droidify? It Is An Open Source App That Is Basically Just A Pretty F-Droid With More Sources. (Y/n)\n"
    )
    if confirm.lower() in ("n", "no", "nah", "nope", "nn", "noo"):
        verboseClear()
    elif confirm.lower() in ("y", "yes", "ye", "yeah", "", "yess", "yy", "ys"):
        verboseClear()
        print("\nGrabbing Droidify APK From Web!")
        api_url = "https://api.github.com/repos/Droid-ify/client/releases/latest"
        with urllib.request.urlopen(api_url) as response:
            release = json.load(response)
    
        apk_url = next(
                asset["browser_download_url"]
                for asset in release["assets"]
                if asset["name"].endswith(".apk")
        )
        file = "Droidify.apk"
        urllib.request.urlretrieve(apk_url, file)
    
        print("\nInstalling Droidify!")
        if args.verbose:
            subprocess.run(
                [
                    "adb",
                    "-s",
                    deviceChoice,
                    "install",
                    "-r",
                    "Droidify.apk"
                ],
            )
        else:
            subprocess.run(
                [
                    "adb",
                    "-s",
                    deviceChoice,
                    "install",
                    "-r",
                    "Droidify.apk"
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        verboseClear()
    
    applist()
    confirm = input(
        "\nInstall Haven SSH Client? It's a beautiful SSHH client for Android, great for when you just want to quickly log in to your server! (Y/n)\n"
    )
    if confirm.lower() in ("n", "no", "nah", "nope", "nn", "noo"):
        verboseClear()
    elif confirm.lower() in ("y", "yes", "ye", "yeah", "", "yess", "yy", "ys"):
        verboseClear()
        print("\nGrabbing Haven APK From Web!")
        api_url = "https://api.github.com/repos/GlassHaven/Haven/releases/latest"
        with urllib.request.urlopen(api_url) as response:
            release = json.load(response)
    
        apk_url = next(
                asset["browser_download_url"]
                for asset in release["assets"]
                if asset["name"].endswith("-arm64-release.apk")
        )
        file = "Haven.apk"
        urllib.request.urlretrieve(apk_url, file)
    
        print("\nInstalling Haven!")
        if args.verbose:
            subprocess.run(
                [
                    "adb",
                    "-s",
                    deviceChoice,
                    "install",
                    "-r",
                    "Haven.apk"
                ],
            )
        else:
            subprocess.run(
                [
                    "adb",
                    "-s",
                    deviceChoice,
                    "install",
                    "-r",
                    "Haven.apk"
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        verboseClear()
    
    applist()
    confirm = input("\nInstall ArchiveTune? [Youtube Music Client] (Y/n)\n")
    if confirm.lower() in ("n", "no", "nah", "nope", "nn", "noo"):
        verboseClear()
    elif confirm.lower() in ("y", "yes", "ye", "yeah", "", "yess", "yy", "ys"):
        verboseClear()
        print("\nGrabbing ArchiveTune APK From Web!")
        api_url = "https://api.github.com/repos/rukamori/ArchiveTune/releases/latest"
        with urllib.request.urlopen(api_url) as response:
            release = json.load(response)
    
        apk_url = next(
                asset["browser_download_url"]
                for asset in release["assets"]
                if asset["name"].endswith("gms-mobile-arm64-release.apk")
        )
        file_name = "ArchiveTune.apk"
        urllib.request.urlretrieve(apk_url, file_name)
    
        print("\nInstalling ArchiveTune!")
        if args.verbose:
            subprocess.run(
                [
                    "adb",
                    "-s",
                    deviceChoice,
                    "install",
                    "-r",
                    "ArchiveTune.apk"
                ],
            )
        else:
            subprocess.run(
                [
                    "adb",
                    "-s",
                    deviceChoice,
                    "install",
                    "-r",
                    "ArchiveTune.apk"
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        verboseClear()
    
    applist()
    confirm = input(
        "\nInstall Localsend? [Basically Open Source Android AirDrop] (Y/n)\n"
    )
    if confirm.lower() in ("n", "no", "nah", "nope", "nn", "noo"):
        verboseClear()
    elif confirm.lower() in ("y", "yes", "ye", "yeah", "", "yess", "yy", "ys"):
        verboseClear()
        print("\nGrabbing Localsend APK From Web!")
        api_url = "https://api.github.com/repos/localsend/localsend/releases/latest"
        with urllib.request.urlopen(api_url) as response:
            release = json.load(response)
        apk_url = next(
                asset["browser_download_url"]
                for asset in release["assets"]
                if asset["name"].endswith("-android-arm64v8.apk")
        )
        file = "Localsend.apk"
        urllib.request.urlretrieve(apk_url, file)
    
        print("\nInstalling Localsend!")
        if args.verbose:
            subprocess.run(
                [
                    "adb",
                    "-s",
                    deviceChoice,
                    "install",
                    "-r",
                    "Localsend.apk"
                ],
            )
        else:
            subprocess.run(
                [
                    "adb",
                    "-s",
                    deviceChoice,
                    "install",
                    "-r",
                    "Localsend.apk"
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            verboseClear()
    
    if rootResult.stdout.strip() != "root":
        applist()
        confirm = input(
            "\nInstall Magisk? (For Rooting, If You Don't Have OEM Unlocking, Don't Even Bother. (Y/n)\n"
        )
        if confirm.lower() in ("n", "no", "nah", "nope", "nn", "noo"):
            verboseClear()
        elif confirm.lower() in ("y", "yes", "ye", "yeah", "", "yess", "yy", "ys"):
            verboseClear()
            print("\nGrabbing Magisk APK From Web!")
            api_url = "https://api.github.com/repos/topjohnwu/Magisk/releases/latest"
            with urllib.request.urlopen(api_url) as response:
                release = json.load(response)
            apk_url = next(
                    asset["browser_download_url"]
                    for asset in release["assets"]
                    if asset["name"].startswith("Magisk-v") and asset["name"].endswith(".apk")
            )
            file = "Magisk.apk"
            urllib.request.urlretrieve(apk_url, file)
    
            print("\nInstalling Magisk!")
        if args.verbose:
            subprocess.run(
                [
                    "adb",
                    "-s",
                    deviceChoice,
                    "install",
                    "-r",
                    "Magisk.apk"
                ],
            )
        else:
            subprocess.run(
                [
                    "adb",
                    "-s",
                    deviceChoice,
                    "install",
                    "-r",
                    "Magisk.apk"
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            verboseClear()
    elif "root" in rootResult.stdout:
        applist()
        confirm = input(
            "\nInstall Bind Hosts? (An app you can use with root to disable ads at the system level while freeing up your private DNS settings. (Y/n)\n"
        )
        if confirm.lower() in ("n", "no", "nah", "nope", "nn", "noo"):
            verboseClear()
        elif confirm.lower() in ("y", "yes", "ye", "yeah", "", "yess", "yy", "ys"):
            verboseClear()
            print("\nGrabbing Bind Hosts Zip From Web!")
            api_url = "https://api.github.com/repos/bindhosts/bindhosts/releases/latest"
            with urllib.request.urlopen(api_url) as response:
                release = json.load(response)
    
            zip_url = next(
                    asset["browser_download_url"]
                    for asset in release["assets"]
                    if asset["name"].endswith("hosts.zip")
            )
            filename = "bindHosts.zip"
            urllib.request.urlretrieve(zip_url, filename)
            bindCheck = subprocess.run(
                    [
                        "adb",
                        "-s",
                        deviceChoice,
                        "shell",
                        "ls",
                        "/sdcard",
                    ],
                    capture_output=True,
                    text=True,
                )
            if "bindHosts.zip" in bindCheck.stdout:
                subprocess.run(["adb", "-s", deviceChoice, "shell", "rm", "bindHosts.zip"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            else:
                pass
            if args.verbose:
                subprocess.run(
                    [
                        "adb",
                        "-s",
                        deviceChoice,
                        "push",
                        "./bindHosts.zip",
                        "/sdcard/"
                    ],
                )
            else:
                subprocess.run(
                    [
                        "adb",
                        "-s",
                        deviceChoice,
                        "push",
                        "./bindHosts.zip",
                        "/sdcard/",
                    ],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
            if "bindHosts.zip" in bindCheck.stdout:
                applist()
                print("Bind Hosts -- /sdcard/bindHosts.zip\n")
            input(
                "You'll have to flash this as a zip through Magisk (or your preferred root manager), it isn't a standalone APK. Click to continue!\n"
            )
            magiskCheck = subprocess.run(
                [
                    "adb",
                    "-s",
                    deviceChoice,
                    "shell",
                    "pm",
                    "list",
                    "packages",
                ],
                capture_output=True,
                text=True,
            )
            if "package:com.topjohnwu.magisk" in magiskCheck.stdout:
                confirm = input("Open Magisk app? (Y/n)\n")
                if confirm.lower() in ("n", "no", "nah", "nope", "nn", "noo"):
                    pass
                elif confirm.lower() in ("y", "yes", "ye", "yeah", "", "yess", "yy", "ys"):
                    subprocess.run(
                        [
                            "adb",
                            "-s",
                            deviceChoice,
                            "shell",
                            "am",
                            "start",
                            "-n",
                            "com.topjohnwu.magisk/.ui.MainActivity",
                        ],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                    )
                verboseClear()
            else:
                verboseClear()
    applist()
if __name__ == "__main__":
    main()


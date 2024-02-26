from tkinter import messagebox


class Package:
    name: str = "undefined"
    ver: str = "0.0.0"
    install_script: str = "raise InstallError(\"No install script found:(\")"
    uninstall_script: str = "raise UninstallError(\"No uninstall script found :(\")"

    def __init__(self, name, ver, install, uninstall):
        self.name = name
        self.ver = ver
        self.install_script = install
        self.uninstall_script = uninstall


def install_package(package: Package | None):
    if package:
        name = package.name
        messagebox.showinfo("Install Package", f"Installed {name}!")
    else:
        messagebox.showerror("Install Package", "Please select a package to install.")


def remove_package(package: Package | None):
    if package:
        name = package.name
        messagebox.showinfo("Remove Package", f"Removed {name}!")
    else:
        messagebox.showerror("Remove Package", "Please select a package to remove.")


def update_package(package: Package | None):
    if package:
        name = package.name
        messagebox.showinfo("Update Package", f"Updated {name}!")
    else:
        messagebox.showerror("Update Package", "Please select a package to update.")

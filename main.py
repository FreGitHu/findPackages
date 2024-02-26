import tkinter as tk
import packages as packages


def install():
    # Get the index of the selected item
    selected_index = package_listbox.curselection()
    if selected_index:
        # Retrieve the package object based on the index
        selected_package = packagelist[selected_index[0]]
        # Call the lower-level install_package function with the selected package object
        packages.install_package(selected_package)
    else:
        # Call the lower-level install_package function with None to indicate no package selected
        packages.install_package(None)


def remove():
    # Get the index of the selected item
    selected_index = package_listbox.curselection()
    if selected_index:
        # Retrieve the package object based on the index
        selected_package = packagelist[selected_index[0]]
        # Call the lower-level remove_package function with the selected package object
        packages.remove_package(selected_package)
    else:
        # Call the lower-level remove_package function with None to indicate no package selected
        packages.remove_package(None)


def update():
    # Get the index of the selected item
    selected_index = package_listbox.curselection()
    if selected_index:
        # Retrieve the package object based on the index
        selected_package = packagelist[selected_index[0]]
        # Call the lower-level update_package function with the selected package object
        packages.update_package(selected_package)
    else:
        # Call the lower-level update_package function with None to indicate no package selected
        packages.update_package(None)


def search_packages():
    search_query = search_entry.get().lower()
    package_listbox.delete(0, tk.END)
    for p in packagelist:
        if search_query in p.name.lower():
            package_listbox.insert(tk.END, p.name)


# Create main window
root = tk.Tk()
root.title("Package Manager")

# Create widgets
search_label = tk.Label(root, text="Search:")
search_label.pack(pady=5)

search_entry = tk.Entry(root, width=30)
search_entry.pack(pady=5)

search_button = tk.Button(root, text="Search", command=search_packages)
search_button.pack(pady=5)

package_label = tk.Label(root, text="Packages:")
package_label.pack(pady=5)

packagelist = []
for i in range(10000):
    packagelist.append(packages.Package("Package" + str(i), "1.0.0", "", ""))

package_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
for package in packagelist:
    package_listbox.insert(tk.END, package.name)
package_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar.config(command=package_listbox.yview)
package_listbox.config(yscrollcommand=scrollbar.set)

install_button = tk.Button(root, text="Install", command=install)
install_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove", command=remove)
remove_button.pack(pady=5)

update_button = tk.Button(root, text="Update", command=update)
update_button.pack(pady=5)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=False)

menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit)

# Package Menu
package_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Packages", menu=package_menu)
package_menu.add_command(label="Edit Package Sources", command=print)

source_menu = tk.Menu(package_menu, tearoff=False)
source_menu.add_command(label="from URL", command=print)
source_menu.add_command(label="from CSV", command=print)
package_menu.add_cascade(label="Add Package List", menu=source_menu)

package_menu.add_separator()

# Start the main event loop
root.mainloop()

from github import Github
from github.GithubException import *
import tkinter as tk
from tkinter import messagebox
import requests
import sys
from PIL import ImageTk, Image

# Thanks to https://stackoverflow.com/a/47928390
class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

try:
	g = Github(sys.argv[1])
	g.get_user("rackodo") # If you fork or modify this repo, please keep this line the same to provide credit to me. -@rackodo
except IndexError:
	print("Please run this script again with your GitHub Access Token after the package name. Like this:")
	print("$ python py_github_gui ghp_ACCESSKEYHERE1234")
	exit()
except BadCredentialsException:
	print("Invalid GitHub Access Token")
	exit()

user = None
userAvatar = None

def updateName():
	result = user.name if user.name != None else ("@" + user.login.lower())

	profileRealName.configure(text=result)
	

def updateAvatar():
	avatarRaw = Image.open(requests.get(user.avatar_url, stream=True).raw).resize((150, 150), Image.LANCZOS)
	avatar = ImageTk.PhotoImage(avatarRaw)
	profilePicWrapper.configure(image = avatar)
	profilePicWrapper.image = avatar

def receiveUser():
	global user
	try:
		user = g.get_user(usernameEntry.get())
	except UnknownObjectException:
		messagebox.showerror("Error", "Not a GitHub Profile")
		return

	updateName()
	updateAvatar()

win = tk.Tk()
win.title("Py Github GUI")
win.geometry('520x320')

main = tk.Frame(width=500, height=300)
main.pack(padx=10, pady=10)

# Left Column
left = tk.Frame(main)
left.place(x=0, y=0, anchor="nw", width=150, height=300)

profilePic = ImageTk.PhotoImage(Image.open("py_github_gui/placeholder.png").resize((150, 150), Image.LANCZOS))
profilePicWrapper = tk.Label(left, image = profilePic, width=150, height=150)
profileRealName = tk.Label(left, font=("Arial", 16), text="Waiting...")
infoButton = tk.Button(left, width=150, text="Get Information", command=receiveUser)
usernameEntry = EntryWithPlaceholder(left, placeholder="GitHub Username")
usernameEntry.configure(width=150, justify=tk.CENTER)

profilePicWrapper.pack()
profileRealName.pack()
infoButton.pack(side=tk.BOTTOM)
usernameEntry.pack(side=tk.BOTTOM)

right = tk.Frame(main, padx=10, pady=10)
right.place(x=150, y=0, anchor="nw", width=350, height=300)

container = tk.Frame(right)
container.pack(side=tk.LEFT, fill="x", expand=1)

test = tk.Label(container, text="Yoinky")
test2 = tk.Label(container, text="Yoinky2")
test3 = tk.Label(container, text="Yoinky3")
test4 = tk.Label(container, text="Yoinky4")

for widget in [ test, test2, test3, test4 ]:
	widget.configure(anchor="w")
	widget.pack_propagate(False)
	widget.pack(fill="both", expand=1)

win.resizable(width=False, height=False)
win.mainloop()
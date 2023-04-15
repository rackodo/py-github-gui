# Imports
from github import Github
from github.GithubException import *
import tkinter as tk
from tkinter import messagebox
from url_normalize import url_normalize
import requests
import sys
import os
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

# Testing that a valid Github object can be created
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

# Init user and avatar objects
user = None
userAvatar = None

# Get user's real name and set it. Otherwise return "None"
def updateName():
	profileRealName.configure(text=user.name if user.name != None else ("@" + user.login.lower()))

# Get user's avatar and set it. Otherwise return "None"
def updateAvatar():
	avatarRaw = Image.open(requests.get(user.avatar_url, stream=True).raw).resize((150, 150), Image.LANCZOS)
	avatar = ImageTk.PhotoImage(avatarRaw)
	profilePicWrapper.configure(image = avatar)
	profilePicWrapper.image = avatar

# Get the user's contact email and set it. Otherwise return "None"
def updateContact():
	userContact.configure(text=("Contact: " + (user.email if user.email != None else "None")))

# Get the user's website and set it. Otherwise return "None"
def updateBlog():
	userBlog.configure(text=("Blog: " + (url_normalize(user.blog) if user.blog != "" else "None")))

# Get the user's location and set it. Otherwise return "None"
def updateLocation():
	userLocation.configure(text=("Location: " + (user.location if user.location != None else "None")))

# Get the user's total repo count and set it. Otherwise return "None"
def updateRepos():
	userRepos.configure(text=("Repos: " + str(user.public_repos)))

# Get the user's total star count and set it
def updateStars():
	userStars.configure(text=("Stars: " + str(user.get_starred().totalCount)))

# Get the user's total following count and set it
def updateFollowing():
	userFollowing.configure(text=("Following: " + str(user.following)))

# Get the user's total follower count and set it
def updateFollowers():
	userFollowers.configure(text=("Followers: " + str(user.followers)))

# Handle the button being clicked
def handleButton():
	receiveUser()

# Handle the Enter/Return key being tapped
def handleKey(event):
	receiveUser()

# Get the user's NamedUser object and execute the retrieval of information
def receiveUser():
	global user
	try:
		user = g.get_user(usernameEntry.get())
	except UnknownObjectException:
		messagebox.showerror("Error", "Not a GitHub Profile")
		return

	updateName()
	updateAvatar()
	updateContact()
	updateBlog()
	updateLocation()
	updateRepos()
	updateStars()
	updateFollowing()
	updateFollowers()

# Set up the Tkinter Window
win = tk.Tk()
win.title("Py Github GUI")
win.geometry('520x320')

main = tk.Frame(width=500, height=300)
main.pack(padx=10, pady=10)


# Set up the left column
left = tk.Frame(main)
left.place(x=0, y=0, anchor="nw", width=150, height=300)

# Set up the left column's widgets
## Set up the profile image and wrapper
profilePic = ImageTk.PhotoImage(Image.open(os.path.dirname(__file__) + "/placeholder.png").resize((150, 150), Image.LANCZOS))
profilePicWrapper = tk.Label(left, image = profilePic, width=150, height=150)

profileRealName = tk.Label(left, font=("Arial", 16), text="Waiting...")
infoButton = tk.Button(left, width=150, text="Get Information", command=handleButton)
usernameEntry = EntryWithPlaceholder(left, placeholder="GitHub Username")
usernameEntry.configure(width=150, justify=tk.CENTER)

# Pack the left column's widgets
profilePicWrapper.pack()
profileRealName.pack()
infoButton.pack(side=tk.BOTTOM)
usernameEntry.pack(side=tk.BOTTOM)

# Set up the right column
right = tk.Frame(main, padx=10, pady=10)
right.place(x=150, y=0, anchor="nw", width=350, height=300)

# This is the best way I can think of to get all the labels centered vertically and aligned to the left
container = tk.Frame(right)
container.pack(side=tk.LEFT, fill="x", expand=1)

# Set up the right column's widgets
userContact = tk.Label(container, text="Contact: ")
userBlog = tk.Label(container, text="Blog: ")
userLocation = tk.Label(container, text="Location: ")
userRepos = tk.Label(container, text="Repos: ")
userStars = tk.Label(container, text="Stars: ")
userFollowing = tk.Label(container, text="Following: ")
userFollowers = tk.Label(container, text="Followers: ")

# Pack the right column's widgets
for widget in [ userContact, userBlog, userLocation, userRepos, userStars, userFollowing, userFollowers ]:
	widget.configure(anchor="w")
	widget.pack_propagate(False)
	widget.pack(fill="both", expand=1)

# Make the window non-resizable, bind the Enter/Return key, then we're off to the races!
win.resizable(width=False, height=False)
win.bind("<Return>", handleKey)
win.mainloop()
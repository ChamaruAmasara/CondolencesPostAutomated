import os
from PIL import Image, ImageFont, ImageDraw
import pyperclip

dir_path = os.path.dirname(os.path.realpath(__file__))

nameOfFriend = input("Enter the Name of the Friend :")
nameOfFriend = "Dear " + nameOfFriend.capitalize()
gender = ""
while gender != "male" and gender != "female":
    gender = input("Enter the gender: ")
    gender = gender.lower()

if gender == "male":
    genderWord = "HIS"
else:
    genderWord = "HER"

whoIsDead = input("What is the relation? Ex:-Father :")
whoIsDeadWording = genderWord + " DEAREST " + whoIsDead.upper()

caption = (f"""It is with great regret that we address the untimely demise of the {whoIsDead.lower()} of our beloved colleague, {nameOfFriend}.""" # noqa
+ """Our deepest sympathies and loving prayers go out to you and your beautiful family during these trying times of the pandemic.""" # noqa
+ f"""May your dear {whoIsDead.lower()} attain the supreme bliss of Nibbana ✨🙏🏻"""  # noqa 
)

myImage = Image.open(f"{dir_path}/template.jpg")
W, H = myImage.size
nameOfFriendFont = ImageFont.truetype(f"{dir_path}/Montserrat-Regular.ttf", 30)
whoIsDeadFont = ImageFont.truetype(f"{dir_path}/Montserrat-Bold.ttf", 30)

image_editable = ImageDraw.Draw(myImage)

# Draw the name of the friend
bbox = image_editable.textbbox((0, 0), nameOfFriend, font=nameOfFriendFont)
w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
image_editable.text(((W - w) / 2, 460), nameOfFriend, (0, 0, 0), font=nameOfFriendFont) # noqa

# Draw "and family"
andFamily = "and " + genderWord.lower() + " family,"
bbox = image_editable.textbbox((0, 0), andFamily, font=nameOfFriendFont)
w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
image_editable.text(((W - w) / 2, 503), andFamily, (0, 0, 0), font=nameOfFriendFont) # noqa

# Draw the relation wording
bbox = image_editable.textbbox((0, 0), whoIsDeadWording, font=whoIsDeadFont)
w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
image_editable.text(((W - w) / 2, 605), whoIsDeadWording, (0, 0, 0), font=whoIsDeadFont) # noqa

# Save the image
myImage.save("result-manual.jpg")
print("Image Created")
print("Caption of the post is\n", caption)

pyperclip.copy(caption)
spam = pyperclip.paste()
print("Caption copied to clipboard.")
exit()

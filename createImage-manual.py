import os
dir_path = os.path.dirname(os.path.realpath(__file__))

from PIL import Image, ImageFont, ImageDraw
import pyperclip



nameOfFriend=input("Enter the Name of the Friend :")
nameOfFriend.capitalize()
nameOfFriend="Dear "+nameOfFriend
gender=""
while (gender!="male" and gender!="female"):
    gender=input("Enter the gender: ")
    gender=gender.lower()
    
if gender=="male":
    genderWord="HIS"
else:
    genderWord="HER"

whoIsDead=input("What is the relation? Ex:-Father :")
whoIsDeadWording=genderWord+" DEAREST "+whoIsDead.upper()


caption=f"""
It is with great regret that we address the untimely demise of the {whoIsDead.lower()} of our beloved colleague, {nameOfFriend}. 

Our deepest sympathies and loving prayers go out to you and your beautiful family during these trying times of the pandemic. 

May your dear {whoIsDead.lower()} attain the supreme bliss of Nibbana ✨🙏🏻"""



myImage=Image.open(f"{dir_path}/template.jpg")
W,H=myImage.size
nameOfFriendFont=ImageFont.truetype(f'{dir_path}/Montserrat-Regular.ttf',30)


whoIsDeadFont=ImageFont.truetype(f'{dir_path}/Montserrat-Bold.ttf',30)


image_editable=ImageDraw.Draw(myImage)
w, h = image_editable.textsize(nameOfFriend,font=nameOfFriendFont)
image_editable.text(((W-w)/2,460),nameOfFriend,(0, 0, 0),nameOfFriendFont)

andFamily="and "+genderWord.lower()+" family,"
w, h = image_editable.textsize(andFamily,font=nameOfFriendFont)
image_editable.text(((W-w)/2,503),andFamily,(0, 0, 0),nameOfFriendFont)


w, h = image_editable.textsize(whoIsDeadWording,font=whoIsDeadFont)


image_editable.text(((W-w)/2,605), whoIsDeadWording,(0, 0, 0),whoIsDeadFont)



myImage.save("result-manual.jpg")
print("Image Created")
print("Caption of the post is\n",caption)

pyperclip.copy(caption)
spam = pyperclip.paste()
print("Caption copied to clipboard.")
exit()




from models import Adverstiment

adv = Adverstiment()
link = input("Enter adverstiment link: ")
picture = input("Enter adverstiment picture: ")
show = input("Enter shows count: ")

adv.create(link=link, picture=picture, show=show)
import csv
from createuserdb import *
from user_login import *
from choose_movie import *
from in_menu import *






if __name__ == "__main__":
  create_db()
  username, password = login()
  menu(username, password)
  
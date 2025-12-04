from helpers.config import get_settings , Settings
import os
import random 
import string
class BaseController:
  
  def __init__(self):
  # get app configration for data validation
   self.app_settings = get_settings()
  #  get root path for file storing in assets
   self.base_dir = os.path.dirname(os.path.dirname(__file__))
  #  get path for the files directory
   self.files_dir = os.path.join(self.base_dir , "assets/files")

  def generate_random_string(self, length:int= 12):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))




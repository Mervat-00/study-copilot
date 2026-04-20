from .BaseController import BaseController
from .ProjectController import ProjectController
import os
from langchain.document_loaders import TextLoader, PyPDFLoader


class ProcessController(BaseController):
  def __init__(self , project_id:str):
    # call the app settings from the base controller
    super().__init__()
    self.project_id = project_id
    self.project_path = ProjectController().get_project_path(project_id = project_id)

  def get_file_extension(self, file_id:str):
    return os.path.splitext(file_id)[-1 ]

    

  def process_file(self , file_id:str):
    pass
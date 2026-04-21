from .BaseController import BaseController
from .ProjectController import ProjectController
import os
from langchain import TextLoader
from langchain import PyMuPDFLoader
from models.enums import ProcessingEnum
from langchain import RecursiveCharacterTextSplitter

class ProcessController(BaseController):
  def __init__(self , project_id:str):
    # call the app settings from the base controller
    super().__init__()
    self.project_id = project_id
    self.project_path = ProjectController().get_project_path(project_id = project_id)

  def get_file_extension(self, file_id:str):
    return os.path.splitext(file_id)[-1]

  def get_file_loader(self,file_id:str , file_path:str ):

    file_extension = self.get_file_extension(file_id)

    if file_extension == ProcessingEnum.TXT :
      return TextLoader(file_path , encoding="utf-8")

    if file_extension == ProcessingEnum.PDF :
      return PyMuPDFLoader(file_path)

    return None 

  # content extraction 
  def get_file_content(self,file_id:str):
    loader = self.get_file_loader(file_id=file_id , file_path=self.project_path)
    return loader.load()

  def process_file_content(self, file_content: list , file_id:str , chunck_size: int=100 , overlap_size : int=20):
      text_splitter = RecursiveCharacterTextSplitter(
      chunk_size=chunck_size,
      chunk_overlap=overlap_size,
      length_function=len)

      file_content_text =[rec.page_content for rec in file_content]

      file_content_metadata = [rec.metadata for rec in file_content]

      chuncks = text_splitter.split_text(file_content_text , metadatas = file_content_metadata)

      return chuncks



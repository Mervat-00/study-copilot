#using pydantic to design schema for data validation comming from user
#this is the main schema for any data that will be sent to the API
from pydantic import BaseModel
from typing import Optional 

class ProcessRequest(BaseModel):
  file_id:str
  chunk_size : Optional[int] = 100
  do_reset: Optional[int] = 0
  
  
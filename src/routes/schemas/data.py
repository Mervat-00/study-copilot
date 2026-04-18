from pydantic import BaseModel
from typing import optional 

class ProcessRequest(BaseModel):
  file_id:str
  chunk_size : optional[int] = 100
  
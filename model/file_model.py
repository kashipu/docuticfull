from pydantic import BaseModel

class FileInDB(BaseModel):
    file_id: str
    file_name: str
    file_img: str
    file_description: str
    file_size: int
    file_type: str
    
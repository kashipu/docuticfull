from typing import  Dict
from pydantic import BaseModel

class FileInDB(BaseModel):
    file_id: str
    file_name: str
    file_img: str
    file_description: str
    file_size: int
    file_type: str
    

database_files = Dict[str, FileInDB]

database_files = {
    "file1": FileInDB(**{"file_id":"202017121",
                        "file_name":"Documento 1",
                        "file_img": "https://via.placeholder.com/300x200",
                        "file_description": "Este es un documento de prueba y esto va en su descripción",
                        "file_size": 123456,
                        "file_type": "txt/plain"
                        }),
    "file2": FileInDB(**{"file_id":"202017122",
                        "file_name":"Documento 2",
                        "file_img": "https://via.placeholder.com/300x200",
                        "file_description": "Este es un documento de prueba y esto va en su descripción",
                        "file_size": 123456,
                        "file_type": "txt/plain"
                        }),
    "file3": FileInDB(**{"file_id":"202017123",
                        "file_name":"Documento 3",
                        "file_img": "https://via.placeholder.com/300x200",
                        "file_description": "Este es un documento de prueba y esto va en su descripción",
                        "file_size": 123456,
                        "file_type": "txt/plain"
                        }),
    "file4": FileInDB(**{"file_id":"202017124",
                        "file_name":"Documento 4",
                        "file_img": "https://via.placeholder.com/300x200",
                        "file_description": "Este es un documento de prueba y esto va en su descripción",
                        "file_size": 123456,
                        "file_type": "txt/plain"
                        }),
    "file5": FileInDB(**{"file_id":"202017125",
                        "file_name":"Documento 5",
                        "file_img": "https://via.placeholder.com/300x200",
                        "file_description": "Este es un documento de prueba y esto va en su descripción",
                        "file_size": 123456,
                        "file_type": "txt/plain"
                        }),
    "file6": FileInDB(**{"file_id":"202017126",
                        "file_name":"Documento 6",
                        "file_img": "https://via.placeholder.com/300x200",
                        "file_description": "Este es un documento de prueba y esto va en su descripción",
                        "file_size": 123456,
                        "file_type": "txt/plain"
                        }),
    "file7": FileInDB(**{"file_id":"202017127",
                        "file_name":"Documento 7",
                        "file_img": "https://via.placeholder.com/300x200",
                        "file_description": "Este es un documento de prueba y esto va en su descripción",
                        "file_size": 123456,
                        "file_type": "txt/plain"
                        }),
    "file8": FileInDB(**{"file_id":"202017128",
                        "file_name":"Documento 8",
                        "file_img": "https://via.placeholder.com/300x200",
                        "file_description": "Este es un documento de prueba y esto va en su descripción",
                        "file_size": 123456,
                        "file_type": "txt/plain"
                        }),
    "file9": FileInDB(**{"file_id":"202017129",
                        "file_name":"Documento 9",
                        "file_img": "https://via.placeholder.com/300x200",
                        "file_description": "Este es un documento de prueba y esto va en su descripción",
                        "file_size": 123456,
                        "file_type": "txt/plain"
                        }),
    "file10": FileInDB(**{"file_id":"2020171210",
                        "file_name":"Documento 10",
                        "file_img": "https://via.placeholder.com/300x200",
                        "file_description": "Este es un documento de prueba y esto va en su descripción",
                        "file_size": 123456,
                        "file_type": "txt/plain"
                        }),
}

def get_file(file_name: str):
    if file_name in database_files.keys():
        return database_files[file_name]
    else:
        return None

def size_file_db():
    return len(database_files)

def get_files():
    files = []
    for t in database_files.keys():
        archivo = database_files[t]
        files.append(archivo)
    return files

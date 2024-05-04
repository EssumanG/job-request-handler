from pydantic import BaseModel

class JobsQueryModel(BaseModel):
    """ Defines the allowed format of the job queries """
    search_term: str
    location: str
    email: str


    class Config:
        json_schema_extra = {
            "example": {
                "search_term": "Junior Python Engineer",
                "location": "California",
                "email": "kojosayves7@gmail.com"
            }
        }
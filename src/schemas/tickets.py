from pydantic import BaseModel



class TicketSchema(BaseModel): 
    id: int
    username:str
    place: int

class TicketGetSchema(TicketSchema): 
    username: str
    place: int
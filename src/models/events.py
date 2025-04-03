from pydantic import BaseModel, ConfigDict

class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: list[str]
    location: str
    created_at: str
    
    # 클래스 콘피그는 옛날 코드임
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "id":1,
                "title":"수업듣기싫당",
                "image": "path/to",
                "description":"나두",
                "tags":["#귀차니즘","#강의"],
                "location": "제 1실습관 207호"
            }
        }
    ) 
    
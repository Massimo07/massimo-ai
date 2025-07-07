from pydantic import BaseModel

class AIPluginModel(BaseModel):
    name: str
    description: str
    type: str  # "text", "voice", "image", etc.
    config: dict

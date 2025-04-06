from enum import Enum


class RoverCameraEnum(str, Enum):
    FHAZ = "fhaz"
    RHAZ = "rhaz"
    MAST = "mast"
    CHEMCAM = "chemcam"	
    MAHLI = "mahli"
    MARDI = "mardi"
    NAVCAM = "navcam"
    PANCAM = "pancam"
    MINITES = "minites"

    def __str__(self):
        return self.value
    

class RoverNameEnum(str, Enum):
    """Названия марсоходов"""
    CURIOSITY = "Curiosity"
    OPPORTUNITY = "Opportunity"
    PERSEVERANCE = "Perseverance"
    SPIRIT = "Spirit"

    def __str__(self):
        return self.value
    
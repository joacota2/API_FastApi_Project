from pydantic import BaseModel
from typing import Optional




class Consulta1(BaseModel):
    driverRef: str
    cuenta: int
    position: int


class Consulta2(BaseModel):
    nombre: str
    cuenta: int
    nationality: str


class Consulta3(BaseModel):
    nombre: str
    cuenta: int
    nationality: str


class Consulta4(BaseModel):
    name: str
    cuenta: int




class Races(BaseModel):
    raceId: Optional[str]
    year: int
    round: int
    circuitId: int
    name: str
    date: str
    time: str
    url: str


class Results(BaseModel):
    resultId: Optional[str]
    raceId: int
    driverId: int
    constructorId: int
    number: int
    grid: int
    position: int
    points: float
    laps: int
    time: str
    miliseconds: int
    fastestLapTime: str
    fastestLapSpeed: float
    statusId: int



class Circuits(BaseModel):
    circuitId: Optional[str]
    circuitRef: str
    name: str
    location: str
    country: str
    lat: float
    lng: float
    alt: int
    url: str


class Constructors(BaseModel):
    constructorId: Optional[str]
    constructorRef: str
    name: str
    nationality: str
    url: str


class Drivers(BaseModel):
    driverId: Optional[str]
    driverRef: str
    number: str
    code: str
    dob: str
    nationality: str
    url: str
    forename: str
    surname: str

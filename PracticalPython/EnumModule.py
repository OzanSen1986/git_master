from enum import Enum,Flag,auto
from dataclasses import dataclass

class Role(Enum):
    CEO: str = 'Chief Executive Officer'
    SSE: str = 'Senior Software Engineer'
    CFO: str = 'Chief Financial Officer'
    GM:  str  = 'General Manager'
    
@dataclass
class Team:
    name: str
    position: Role
    employees: list[str]


team1 = Team('Chuck', Role.SSE.value, None)
team2 = Team('Norris', Role.GM.value, team1)
team3 = Team('Tim', Role.CEO.value, [team1,team2])

print(team1)
print(team2)
print(team3)






























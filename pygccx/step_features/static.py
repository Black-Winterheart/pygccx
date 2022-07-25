from dataclasses import dataclass
from typing import Optional
from enums import ESolvers

number = int|float

@dataclass(frozen=True, slots=True)
class Static:
    """
    Class to define a static analysis
    
    Args:
        solver: Optional. Solver which should be used for the step
        direct: Optional. Flag is direct time stepping should be switched on. 
                True switches off auto time stepping
        init_time_inc: Optional. Size of the first time increment of the step.
        time_period: Optional. Duration of the step
        min_time_inc: Optional. Minimum allowed time increment. Only used if direct == False
        max_time_inc: Optional. Maximum allowed time increment. Only used if direct == False
        time_reset: Optional. Forces the total time at the end of the present step to coincide 
                    with the total time at the end of the previous step
        total_time_at_start: Optional. Sets the total time at the start of the step to a specific value.
        name: Optional. Name of this instance
        desc: Optional. A short description of this instance. This is written to the ccx input file.
    """

    solver:ESolvers = ESolvers.DEFAULT
    """Solver which should be used for the step"""
    direct:bool = False
    """Flag is direct time stepping should be switched on. 
    True switches off auto time stepping"""
    init_time_inc:number = 1.
    """Size of the first time increment of the step."""
    time_period:number = 1.
    """Duration of the step"""
    min_time_inc:Optional[number] = None
    """Minimum allowed time increment. Only used if direct == False"""
    max_time_inc:Optional[number] = None
    """Maximum allowed time increment. Only used if direct == False"""
    time_reset:bool = False
    """forces the total time at the end of the present step to coincide 
    with the total time at the end of the previous step"""
    total_time_at_start:Optional[number] = None
    """sets the total time at the start of the step to a specific value."""
    name:str = ''
    """Name of this instance"""
    desc:str = ''
    """A short description of this instance. This is written to the ccx input file."""

    def __post_init__(self):
        pass


    def __str__(self):
        s = '*STATIC'
        if self.solver != ESolvers.DEFAULT:
            s += f',SOLVER={self.solver.value}'
        if self.direct: s += ',DIRECT'
        if self.time_reset: s += ',TIME RESET'
        if self.total_time_at_start is not None:
            s += f',TOTAL TIME AT START={self.total_time_at_start}'
        s += '\n'

        s += f'{self.init_time_inc},{self.time_period}'
        s += f',{self.min_time_inc}' if self.min_time_inc is not None else ','      
        s += f',{self.max_time_inc}' if self.max_time_inc is not None else ','
        s = s.rstrip(',') + '\n'

        return s




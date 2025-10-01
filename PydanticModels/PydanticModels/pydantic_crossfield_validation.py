from pydantic import BaseModel, ValidationError, field_validator
from datetime import datetime

class Appointment(BaseModel):
    start_time: datetime
    end_time: datetime
    doctor_id: str

    @field_validator('end_time')
    def validate_times(cls, v, values):
        if 'start_time' in values.data and v <= values.data['start_time']:
            raise ValueError('End time must be after start time')
        return v

    @field_validator('doctor_id')
    def validate_doctor_availability(cls, v, values):
        # In a real app, query database here
        if v == 'DR_OVERBOOKED':
            if 'start_time' in values.data:
                raise ValueError("Doctor unavailable at this time")
            return v

def main():
    try:
        Appointment(start_time = '2025-06-08T14:53:04', end_time = '2025-06-09T15:15:08', doctor_id= 'DR_OVERBOOKED')
    except ValidationError as e:
        print(f"Error Description is: {e}")

if __name__ == '__main__':
    main()



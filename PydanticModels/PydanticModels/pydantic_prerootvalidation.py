from pydantic import BaseModel, model_validator, ValidationError

class SurveyResponse(BaseModel):
    q1: int
    q2: int
    q3: int


    @model_validator(mode='before')
    def check_all_questions_present(cls, data):
        if isinstance(data, dict):
            missing = [f"q{i}" for i in range(1,4) if f"q{i}" not in data]
            if missing:
                raise ValueError(f"Missing questions: {missing}")
        return data


def main() -> None:
    try:
        response = SurveyResponse(q1= 5, q2= 4)
        print(f'Validation succeded')
    except ValidationError as e:
        print(e)

if __name__ == "__main__":
    main()


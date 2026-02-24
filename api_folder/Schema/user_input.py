from pydantic import BaseModel, Field,computed_field
from typing import Annotated,Literal,Optional

class Student(BaseModel):
    Gender: Literal['Male', 'Female', 'Other']
    CGPA100: Annotated[float, Field(..., gt=0, lt=5, strict=True)]
    CGPA200: Optional[Annotated[float, Field(gt=0, lt=5, strict=True)]] = None
    CGPA300: Optional[Annotated[float, Field(gt=0, lt=5, strict=True)]] = None
    attendance: Annotated[float, Field(..., gt=0, lt=100, strict=True)]
    study_hours: Annotated[float, Field(..., gt=0, lt=12, strict=True)]

    @computed_field
    @property
    def cal_sgpa(self) ->float:
        scores=[self.CGPA100]
        if self.CGPA200 is not None:
            scores.append(self.CGPA200)
        if self.CGPA300 is not None:
            scores.append(self.CGPA300)
        return sum(scores)/len(scores)

    @computed_field
    @property
    def suggestions(self) ->str:
        if self.cal_sgpa<1.5 :
            return "INCREASE STUDY TIME AND ATTENDANCE YOU ARE AT HIGH RISK"
        elif 1.5 < self.cal_sgpa < 3.5:
            return "YOU ARE DOING OK BUT NEED MORE FOCUS YOU ARE AT LOW RISK"
        else:
            return "YOU ARE DOING WELL NO RISK"
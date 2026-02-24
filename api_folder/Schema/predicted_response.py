from pydantic import BaseModel, Field

class PredictionResponse(BaseModel):
    predicted_cgpa: float = Field(...,description="The predicted cgpa",json_schema_extra={"example":2.15})
    current_avg_cgpa: float = Field(...,description="The average cgpa student have",json_schema_extra={"example":3.1})
    status: str =Field(...,description="Student evaluation",json_schema_extra={"example":" STUDY TIME AND ATTENDANCE YOU ARE AT HIGH RISK"})
    model_loaded : str = Field(...,description='model version',json_schema_extra={"example":'1.0.0'})


from fastapi import FastAPI,HTTPException
from Schema.user_input import Student
from fastapi.middleware.cors import CORSMiddleware
from model.predict import  MODEL_VERSION,predict_output
from Schema.predicted_response import PredictionResponse
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (for dev)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# human-readable
@app.get('/')
def home():
    return {'message' : 'Student Performance prediction api'}

# machine-readable so that aws like services check
@app.get('/health')
def health():
    return {
        'status': 'ok',
        'version' : MODEL_VERSION,
        'model_loaded' : True
    }

@app.post('/predict',response_model=PredictionResponse)
def predict(year :int , user_data : Student):
    if year not in [2,3,4]:
        raise HTTPException(status_code=400,detail="Year not valid Enter year between 2 and 4")
    data=user_data.model_dump()
    # print(pd.DataFrame([data]).columns)
    try:
        prediction = predict_output(year, data)
        return {
            'predicted_cgpa':float(prediction),
            'current_avg_cgpa':float(user_data.cal_sgpa),
            'status' : user_data.suggestions,
            'model_loaded' : MODEL_VERSION
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

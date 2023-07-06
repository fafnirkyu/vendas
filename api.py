from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from joblib import load
from pydantic import BaseModel

model = load("best_model.joblib")


app = FastAPI()
templates = Jinja2Templates(directory="templates")

class InputData(BaseModel):
    Year_of_Release: int
    Critic_Score: int
    Critic_Count: int
    User_Score: float
    User_Count: int
    Platform_3DS: int
    Platform_DC: int
    Platform_DS: int
    Platform_GBA: int
    Platform_GC: int
    Platform_PC: int
    Platform_PS: int
    Platform_PS2: int
    Platform_PS3: int
    Platform_PS4: int
    Platform_PSP: int
    Platform_PSV: int
    Platform_Wii: int
    Platform_WiiU: int
    Platform_X360: int
    Platform_XB: int
    Platform_XOne: int
    Genre_Action: int
    Genre_Adventure: int
    Genre_Fighting: int
    Genre_Misc: int
    Genre_Platform: int
    Genre_Puzzle: int
    Genre_Racing: int
    Genre_Role_Playing: int
    Genre_Shooter: int
    Genre_Simulation: int
    Genre_Sports: int
    Genre_Strategy: int
    Rating_E: int
    Rating_E10plus: int
    Rating_M: int
    Rating_RP: int
    Rating_T: int

@app.get("/")
def prediction_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/predict")
def predict(request: Request, Year_of_Release: int = Form(...), Critic_Score: int = Form(...), Critic_Count: int = Form(...),
            User_Score: float = Form(...), User_Count: int = Form(...), Platform_3DS: int = Form(...), Platform_DC: int = Form(...),
            Platform_DS: int = Form(...), Platform_GBA: int = Form(...), Platform_GC: int = Form(...), Platform_PC: int = Form(...),
            Platform_PS: int = Form(...), Platform_PS2: int = Form(...), Platform_PS3: int = Form(...), Platform_PS4: int = Form(...),
            Platform_PSP: int = Form(...), Platform_PSV: int = Form(...), Platform_Wii: int = Form(...), Platform_WiiU: int = Form(...),
            Platform_X360: int = Form(...), Platform_XB: int = Form(...), Platform_XOne: int = Form(...), Genre_Action: int = Form(...),
            Genre_Adventure: int = Form(...), Genre_Fighting: int = Form(...), Genre_Misc: int = Form(...), Genre_Platform: int = Form(...),
            Genre_Puzzle: int = Form(...), Genre_Racing: int = Form(...), Genre_Role_Playing: int = Form(...), Genre_Shooter: int = Form(...),
            Genre_Simulation: int = Form(...), Genre_Sports: int = Form(...), Genre_Strategy: int = Form(...), Rating_E: int = Form(...),
            Rating_E10plus: int = Form(...), Rating_M: int = Form(...), Rating_RP: int = Form(...), Rating_T: int = Form(...)):
    
    input_data = InputData(
    Year_of_Release=Year_of_Release,
    Critic_Score=Critic_Score,
    Critic_Count=Critic_Count,
    User_Score=User_Score,
    User_Count=User_Count,
    Platform_3DS=Platform_3DS,
    Platform_DC=Platform_DC,
    Platform_DS=Platform_DS,
    Platform_GBA=Platform_GBA,
    Platform_GC=Platform_GC,
    Platform_PC=Platform_PC,
    Platform_PS=Platform_PS,
    Platform_PS2=Platform_PS2,
    Platform_PS3=Platform_PS3,
    Platform_PS4=Platform_PS4,
    Platform_PSP=Platform_PSP,
    Platform_PSV=Platform_PSV,
    Platform_Wii=Platform_Wii,
    Platform_WiiU=Platform_WiiU,
    Platform_X360=Platform_X360,
    Platform_XB=Platform_XB,
    Platform_XOne=Platform_XOne,
    Genre_Action=Genre_Action,
    Genre_Adventure=Genre_Adventure,
    Genre_Fighting=Genre_Fighting,
    Genre_Misc=Genre_Misc,
    Genre_Platform=Genre_Platform,
    Genre_Puzzle=Genre_Puzzle,
    Genre_Racing=Genre_Racing,
    Genre_Role_Playing=Genre_Role_Playing,
    Genre_Shooter=Genre_Shooter,
    Genre_Simulation=Genre_Simulation,
    Genre_Sports=Genre_Sports,
    Genre_Strategy=Genre_Strategy,
    Rating_E=Rating_E,
    Rating_E10plus=Rating_E10plus,
    Rating_M=Rating_M,
    Rating_RP=Rating_RP,
    Rating_T=Rating_T
)
    

    prediction = model.predict([[input_data.Year_of_Release, input_data.Critic_Score, input_data.Critic_Count, input_data.User_Score, input_data.User_Count,
                                 input_data.Platform_3DS, input_data.Platform_DC, input_data.Platform_DS, input_data.Platform_GBA, input_data.Platform_GC,
                                 input_data.Platform_PC, input_data.Platform_PS, input_data.Platform_PS2, input_data.Platform_PS3, input_data.Platform_PS4,
                                 input_data.Platform_PSP, input_data.Platform_PSV, input_data.Platform_Wii, input_data.Platform_WiiU, input_data.Platform_X360,
                                 input_data.Platform_XB, input_data.Platform_XOne, input_data.Genre_Action, input_data.Genre_Adventure, input_data.Genre_Fighting,
                                 input_data.Genre_Misc, input_data.Genre_Platform, input_data.Genre_Puzzle, input_data.Genre_Racing, input_data.Genre_Role_Playing,
                                 input_data.Genre_Shooter, input_data.Genre_Simulation, input_data.Genre_Sports, input_data.Genre_Strategy, input_data.Rating_E,
                                 input_data.Rating_E10plus, input_data.Rating_M, input_data.Rating_RP, input_data.Rating_T]])
    

    return templates.TemplateResponse("result.html", {"request": request, "prediction": prediction})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
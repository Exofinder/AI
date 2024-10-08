from fastapi import FastAPI, Query 
from typing import List
from habitable_calculator import calculate_habitable_percent as chp


app = FastAPI()


@app.get("/systemInfo")
async def carculateHabitable(
        plNameList: List[str] = Query(None),
        plDensList: List[str] = Query(None),
        plOrbeccenList: List[str] = Query(None),
        plOrbsmaxList: List[str] = Query(None),
        plRadeList: List[str] = Query(None),
        stSpectypeList: List[str] = Query(None),
        stRadList: List[str] = Query(None),
        syDistList: List[str] = Query(None),
        syVmagList: List[str] = Query(None),
        diameter: float = Query(None)
):

    results = []

    #maxDensityList=list(map(float,plDensList))
    #maxDensity=max(maxDensityList)

    for i in range(len(plNameList)):
        result = chp(
            plNameList[i],
            plDensList[i],
            plOrbeccenList[i],
            plOrbsmaxList[i],
            plRadeList[i],
            stSpectypeList[i],
            stRadList[i],
            syDistList[i],
            syVmagList[i],
            diameter
        )
        results.append(result)

    return results

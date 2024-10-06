from fastapi import FastAPI, Query
from typing import List
from habitable_calculator import calculate_habitable_percent as chp


app = FastAPI()


@app.get("/systemInfo")
async def carculateHabitable(
        plNameList: List[str] = Query(None),
        plDensList: List[str] = Query(None),
        plObeccenList: List[str] = Query(None),
        plOrbsmaxList: List[str] = Query(None),
        stSpectypeList: List[str] = Query(None),
        stMassList: List[str] = Query(None),
        stTeffList: List[str] = Query(None),
        syDistList: List[str] = Query(None),
        syVmagList: List[str] = Query(None)
):

    results = []

    #maxDensityList=list(map(float,plDensList))
    #maxDensity=max(maxDensityList)

    for i in range(len(plNameList)):
        result = chp(
            #maxDensity,
            plNameList[i],
            plDensList[i],
            plObeccenList[i],
            plOrbsmaxList[i],
            stSpectypeList[i],
            stMassList[i],
            stTeffList[i],
            syDistList[i],
            syVmagList[i]
        )
        results.append(result)

    return results
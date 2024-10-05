from fastapi import FastAPI, Query
from typing import List
from habitable_carculator import calculate_habitable_percent as chp


app = FastAPI()


@app.get("/systemInfo")
async def carculateHabitable(
        plNameList: List[str] = Query(None),
        plDensList: List[str] = Query(None),
        plObeccenList: List[str] = Query(None),
        stSpectypeList: List[str] = Query(None),
        stMassList: List[str] = Query(None),
        stTeffList: List[str] = Query(None),
        syDistList: List[str] = Query(None),
        syVmagList: List[str] = Query(None)
):

    results = []

    for i in range(len(plNameList)):
        result = chp(
            plNameList[i],
            plDensList[i],
            plObeccenList[i],
            stSpectypeList[i],
            stMassList[i],
            stTeffList[i],
            syDistList[i],
            syVmagList[i]
        )
        results.append(result)

    return results
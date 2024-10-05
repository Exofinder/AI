from fastapi import FastAPI, Query
from typing import List
from havitable_carculator import calculate_habitable_percent as chp


app = FastAPI()


@app.get("/systemInfo")
async def carculateHabitable(
        planetNames: List[str] = Query(None),
        hostNmaes: List[str] = Query(None),
        distances: List[str] = Query(None),
        spectralTypes: List[str] = Query(None),
        VMagnitudes: List[str] = Query(None),
        planetDensities: List[str] = Query(None),
        hostdensities: List[str] = Query(None),
        eccentricities: List[str] = Query(None)):

    results = []

    for i in range(len(planetNames)):
        result = chp(
            planetNames[i],
            hostNmaes[i],
            distances[i],
            spectralTypes[i],
            VMagnitudes[i],
            planetDensities[i],
            hostdensities[i],
            eccentricities[i]
        )
        results.append(result)

    return results
from fastapi import FastAPI, Request, HTTPException, Depends, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from router.aianalyze import RunManage
from router.connection import Connecter
import threading
from router.kill import KillProcess

app = FastAPI()
run = RunManage(thread=1)
setting = Connecter()

thread = threading.Thread(target=setting.thread_read_token)
thread.start()
thread.join

def __init__array():
    run.compare.sentences = []
    run.compare.datas = []
    run.compare.comparison = []
    run.compare.comparison_float = []
    run.compare.comparison_data = []
    run.speed_datas = []
    run.speedometer = []
    run.cpu_usage = []
    run.thread_counts = []

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY_NAME = "token"

def get_api_key(request: Request):
    api_key = request.query_params.get(API_KEY_NAME)
    print(setting.token[0])
    for i in range(len(setting.token[0])):
        if api_key == setting.token[0][i][0]:
            return api_key
    raise HTTPException(status_code=403, detail="error")

@app.get("/api")
async def read_root(api_key: str = Depends(get_api_key), ques: str = None):
    embedded_time, general_ques, anal_ques, anal_res = run.run(ques)
    print(anal_res)
    __init__array()
    return {"message": f"{anal_res}"}

if __name__ == "__main__":
    killer = KillProcess()
    killer.killing()
    uvicorn.run("server:app", host="0.0.0.0", port=9460, ssl_keyfile="./ssl/privkey.pem", ssl_certfile="./ssl/cert.pem", reload=True)

'''
서버 시작할때, model을 로딩을 시키는 방식으로 진행을 하고
로딩이 완료가 되면, 서버가동 시작, while문으로 thread로 동시에
항상 실행중으로 백그라운드에서 실행시키기 --> 최종적으로 get 요청을
하면 모델을 호출을 함.
'''
from fastapi import FastAPI, Body, Header, Response

app = FastAPI()

# @app.get("/hi")
# def greet():
#     return "Hello, World!"

@app.post("/hi")
def greet(who: str = Body(embed=True)):
    return f"Hello, {who}!"

@app.get("/hi-query")
def greet(who):
    return f"Hello, {who}!"

@app.get("/hi/{who}")
def greet(who):
    return f"hello, {who}!"

@app.post("/agent")
def get_agent(user_agent: str = Header()):
    return user_agent

@app.get("/happy")
def happy(status_code=200):
    return ":)"

@app.get("/header/{name}/{value}")
def header(name: str, value: str, response: Response):
    response.headers[name] = value
    return "normal body"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
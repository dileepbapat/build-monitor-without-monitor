import requests
import RPi.GPIO as GPIO

host = "184.72.235.230"
port = "8080"
jobs = ["develop mangrove","develop-Datawinners", "develop-Datawinners-Smoke_Test", "develop-Datawinners_functional_test"]

RED_PIN = 24
GREEN_PIN = 26

GPIO.setmode(GPIO.BOARD)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(RED_PIN, GPIO.OUT)

def get_result(job_name):
	resp = requests.get('http://%s:%s/job/%s/lastBuild/api/json'%(host, port, job_name))
	json = resp.json if isinstance(resp.json, dict) else resp.json()  #older requests version had json as property
	return json.get('result')	

def set_status(r,g):
	GPIO.output(RED_PIN, r)
	GPIO.output(GREEN_PIN, g)
	
result = [get_result(job_name) for job_name in jobs]

if "FAILURE" in result:
	set_status(1,0)
elif None in result:
	pass
elif set(result) == set(["SUCCESS"]):
	set_status(0,1)
else: 
	set_status(0,0)
	



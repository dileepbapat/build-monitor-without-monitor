import requests
import RPi.GPIO as GPIO

host = "184.72.235.230"
port = "8080"
job_name = "develop-Datawinners"

RED_PIN = 24
GREEN_PIN = 26

GPIO.setmode(GPIO.BOARD)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(RED_PIN, GPIO.OUT)


resp = requests.get('http://%s:%s/job/%s/lastBuild/api/json'%(host, port, job_name))
status = resp.json().get('result')	

def set_green():
	print "green"
	GPIO.output(GREEN_PIN, GPIO.HIGH)
	GPIO.output(RED_PIN, GPIO.LOW)
	
def set_red():
	print "red"
	GPIO.output(GREEN_PIN, GPIO.LOW)
	GPIO.output(RED_PIN, GPIO.HIGH)

if  status == "SUCCESS": 
	set_green()
elif status == "FAILURE":
    set_red()


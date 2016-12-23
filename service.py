from flask import Flask
import RPi.GPIO as GPIO


app = Flask(__name__)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)

@app.route('/IoT/ping')
def pint():
    return 'pong'

@app.route('/IoT/ON')
def ON():
    print('ON')
    GPIO.output(18, GPIO.HIGH)
    return 'OK'

@app.route('/IoT/OFF')
def OFF():
    print('OFF')
    GPIO.output(18, GPIO.LOW)
    return 'OK'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

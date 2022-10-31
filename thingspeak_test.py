import thingspeak
import time
import random

channel_id = 1914215 # put here the ID of the channel you created before
write_key = 'TDRDH4IS671CXKQ9' # update the "WRITE KEY"

def measure(channel):
    try:
        humidity, temperature = random.randrange(0,100), random.randrange(100,200) 
        # update the value
        print('Temperature = {0:0.1f}*C Humidity = {1:0.1f}%'.format(temperature, humidity))

        response = channel.update({'field1': temperature, 'field2': humidity})
    except:
           print("connection failure")

if __name__ == "__main__":
        channel = thingspeak.Channel(id=channel_id, write_key=write_key)
        while True:
            measure(channel)
        #free account has a limitation of 15sec between the updates
            time.sleep(20)

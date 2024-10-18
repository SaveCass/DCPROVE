#General goal: read CPU usage every second

from time import sleep
import psutil

def read_cpu_usage():
    cpu_t = psutil.cpu_times()
    cpu_us = cpu_t.user
    idle_time = cpu_t.idle
    return cpu_us,idle_time,cpu_t


if __name__ == "__main__":


    while True:
        cpu_us,idle_t,cpu_t = read_cpu_usage()
        print("User time: " + str(cpu_us) + " Idle time: " + str(idle_t))
        print("user time: %.2f Idle time: %.2f, Integer %d" %(cpu_us,idle_t,32))
        #some kind of sleep for one second
        sleep(1)
from pprint import pprint
import time
from library import timer
import matplotlib.pyplot as plt
import keyboard

with open("input/input14.txt") as f:
# with open("sample/sample14.txt") as f:
    lines=f.read().splitlines()
    lines=[tuple(line.split()) for line in lines ]
    lines=[{"Position":(int(p.split("=")[1].split(",")[0]),int(p.split("=")[1].split(",")[1])),"velocity":(int(v.split("=")[1].split(",")[0]),int(v.split("=")[1].split(",")[1]))} for p,v in lines]

# @timer
def simulate(robots, mx, my, t=100):
    new_loc=[]
    # print(robots)
    for robot in robots:
        (px,py),(vx,vy)=robot["Position"],robot["velocity"]
        # print(int(px),int(py),int(vx),int(vy))
        new_loc.append(((int(px)+int(vx)*t)%mx,(int(py)+int(vy)*t)%my))
    # print(new_loc)
    return new_loc

# @timer
def count_robots_in_quadrant(robots, mx, my):
    c1, c2, c3, c4 = 0, 0, 0, 0
    for r in robots:
        if r[0] < mx//2 and r[1] < my//2:
            c1+=1
        elif r[0] > mx//2 and r[1] < my//2:
            c2+=1
        elif r[0] < mx//2 and r[1] > my//2:
            c3+=1
        elif r[0] > mx//2 and r[1] > my//2:
            c4+=1
    return c1*c2*c3*c4

def plotter(x,y,t,limx,limy):
    plt.clf()  # Clear the entire figure
    plt.scatter(x, y, color='blue')  # Create a scatter plot with blue points
    plt.xlim(0, limx)  # Set x-axis limits
    plt.ylim(0, limy)  # Set y-axis limits
    plt.title(f"Real-time Scatter Plot Iteration {t}")  # Add a title
    plt.xlabel("X-axis")  # Label for x-axis
    plt.ylabel("Y-axis")  # Label for y-axis
    plt.grid(True)  # Enable grid for better visibility
    plt.pause(0.7)  # Pause for a brief moment to update the plot

@timer
def part1():
    #Find Robots at t=100 and Check which quadrant it's present on
    robots=simulate(lines,BREATH,HEIGHT)
    print("Part 1 Solution: ",count_robots_in_quadrant(robots=robots,mx=BREATH,my=HEIGHT))
@timer
def sol_part2():
    '''
    Function to simulate each  second and check if number of unique robots match total number of robots
    return time
    '''
    t = 0
    while True:
        t += 1
        robots=simulate(lines,BREATH,HEIGHT,t)
        if len(set(robots)) == len(lines):
            break
    return t
@timer
def part2():
    #An image of an "easter egg" is present, check what time it happens on, and plot it to view visually
    t=sol_part2()
    print("Part 2 Solution: ",t)
    plt.figure()  # Open a figure once
    plt.ion()  # Enable interactive mode
    robots=simulate(lines,BREATH,HEIGHT,t)
    x,y=zip(*robots)
    plotter(x,y,t,BREATH,HEIGHT)
    plt.ioff()  # Disable interactive mode when done
    plt.show()  # Show the final plot

if __name__ == "__main__":
    BREATH,HEIGHT=101,103
    # BREATH,HEIGHT=11,7
    part1()
    part2()

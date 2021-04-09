## Assignment 3 ME369P
## Name: Mary Tebben
## EID: met2927
##
import math as m
import matplotlib as plot

'''
Kwargs can be:
    initial_step        : float
    max_step            : float
    relative_tolerance  : float
'''
#Do not modify the function input parameters
def ODE45( func, duration, initial_states, **kwargs):
    initial_step = 0.01
    max_step = 0.25
    relative_tolerance = 0.001
    if kwargs:
        if len(kwargs)>=1:
            initial_step = kwargs[0]
        if len(kwargs)>=2:
            max_step = kwargs[1]
        if len(kwargs) == 3:
            relative_tolerance = kwargs[2]
    h = initial_step
    time = duration[0]
    i = 0
    y1 = []
    y2 = []
    y1.append(initial_states[0])
    y2.append(initial_states[1])

    while time <= duration[1]:
        k1 = func(time,[y1[i],y2[i]])
        k2 = func(time+0.2*h,[y1[i]+0.2*h*k1[0],y2[i]+0.2*h*k1[1]])
        k3 = func(time+0.3*h,[y1[i]+0.3*h*k2[0],y2[i]+0.3*h*k2[1]])
        k4 = func(time+0.6*h,[y1[i]+0.6*h*k3[0],y2[i]+0.6*h*k3[1]])
        k5 = func(time+1*h,[y1[i]+1*h*k4[0],y2[i]+1*h*k4[1]])
        k6 = func(time+0.875*h,[y1[i]+0.875*h*k5[0],y2[i]+0.875*h*k5[1]])
        
    #fourth order
        y1.append(y1[i]+h*((37/378)*k1[0]+(250/621)*k3[0]+(125/594)*k4[0]+(512/1771)*k6[0]))
    #fifth order
        y2.append(y2[i]+h*(
            (2825/27648)*k1[1]+(18575/48384)*k3[1]+
            (13525/55295)*k4[1]+(277/14336)*k5[1]+
            (1/4)*k6[1]
            ))

  #step size
        delta_actual = abs(y2[i+1]-y1[i+1])
        if delta_actual >= relative_tolerance:
            alpha = 0.25
        else:
            alpha = 0.2
        h = h*(relative_tolerance/delta_actual)**alpha
        if h > max_step:
            h = max_step
        print(h)

        if time == duration[1]:
            break
        i += 1
        time += h
        if time > duration[1]:
            time = duration[1]
        print(time)

    states = [y1,y2]
    return time, states


def mySystem( t, y ):
    # This is given, do not modify
    y_prime_1 = 0.5*y[1]
    y_prime_2 = -0.3*y[1] - 0.1*y[0] + 4*m.cos(t)
    y_prime = ( y_prime_1, y_prime_2)
    return y_prime

# def PlotStates(time, states):
#     ## Bonus Function
#     return

def main():
    time, states = ODE45( mySystem, [0, 30], [4, 0])

if __name__ == '__main__':
    main()
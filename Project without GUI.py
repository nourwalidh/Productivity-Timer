import time
timer = False
remaining_time = 0
timer_history = []
delay = 1
paused = False
def show_menu():
    print(
        "------ Timer Menu ------\n1. Start Timer\n2. Pause Timer\n3. Resume Timer\n4. Stop Timer\n5. Show Timer History\n6. Exit to Main Menu")
def choose_speed():
    global delay
    speed_choice = int(input("Countdown Speed\n1. Normal (1 second)\n2. Fast (0.5 second)\n3. Very Fast (0.1 second)\nChoose speed: "))
    if speed_choice == 1:
        delay = 1
    elif speed_choice == 2:
        delay = 0.5
    elif speed_choice == 3:
        delay = 0.1
    else:
        delay = 1
def display_time(seconds_left):
    seconds = seconds_left % 60
    minutes = (seconds_left // 60) % 60
    hours = seconds_left // 3600
    print(f"\r{hours:02}:{minutes:02}:{seconds:02}", end="")
def start_timer():
    global timer, remaining_time, timer_history
    user_timer = int(input("Enter Time in Seconds: "))
    if user_timer <= 0:
        print("Invalid! Number of Seconds Should Be Larger Than Zero")
        return
    choose_speed()
    remaining_time = user_timer
    start_time = user_timer
    timer = True
    while remaining_time > 0 and timer:
        display_time(remaining_time)
        time.sleep(delay)
        remaining_time -= 1
        if remaining_time == 0:
            print("\nTime's Up!")
            timer = False
            timer_history.append(start_time)
def pause_timer():
    global paused
    if timer and not paused:
        paused = True
        print("Timer is Paused")
    else:
        print("Timer is not Running")
def resume_timer():
    global paused
    if timer and paused:
        paused = False
        print("Timer is Resumed")
    else:
        print("Nothing to Resume")

def stop_timer():
    global timer, remaining_time
    timer = False
    remaining_time = 0
    print("Timer Stopped")

def show_history():
    if len(timer_history) == 0:
        print("No Timer History")
    else:
        print("Completed Timers:")
        for t in timer_history:
            print(t, "seconds")
while True:
    show_menu()
    choice = int(input("Choose an Option: "))
    if choice == 1:
        start_timer()
    elif choice == 2:
        pause_timer()
    elif choice == 3:
        resume_timer()
    elif choice == 4:
        stop_timer()
    elif choice == 5:
        show_history()
    elif choice == 6:
        print("Exiting Timer")
        break
    else:
        print("Invalid Response! Please Choose an Option from the List")
start_time = None
elapsed_time = 0.0
laps = []
def start():
    global start_time
    if start_time is None:
        start_time = time.time()
        print("Stopwatch started")
    else:
        print("Stopwatch already running")
def stop():
    global start_time, elapsed_time
    if start_time is not None:
        elapsed_time += time.time() - start_time
        start_time = None
        print("Stopwatch stopped")
    else:
        print("Stopwatch is not running")
def reset():
    global start_time, elapsed_time, laps
    start_time = None
    elapsed_time = 0.0
    laps = []
    print("Stopwatch reset")
def lap():
    global start_time, elapsed_time, laps
    if start_time is not None:
        current = elapsed_time + (time.time() - start_time)
        if len(laps) == 0:
            lap_time = current
        else:
            lap_time = current - laps[-1]
        laps.append(current)
        print("Lap", len(laps), ":", round(lap_time, 2), "seconds")
    else:
        print("Stopwatch is not running")
def show_time():
    if start_time is not None:
        current = elapsed_time + (time.time() - start_time)
    else:
        current = elapsed_time
    hours = int(current // 3600)
    minutes = int((current % 3600) // 60)
    seconds = int(current % 60)
    print(f"Current time: {hours:02d}.{minutes:02d}.{seconds:02d}")
def show_laps():
    if not laps:
        print("No laps recorded")
    else:
        for i in range(len(laps)):
            if i == 0:
                lap_time = laps[i]
            else:
                lap_time = laps[i] - laps[i-1]
                print("Lap", i + 1, "=", round(lap_time, 2), "seconds")
def menu():
    print("1- Start")
    print("2- Stop")
    print("3- Lap")
    print("4- Show Time")
    print("5- Show Laps")
    print("6- Reset")
    print("7- Exit")
def stopwatch_page():
    running = 'True'
    while running == 'True':
        menu()
        choice = input("Choose: ")
        if choice == "1":
            start()
        elif choice == "2":
            stop()
        elif choice == "3":
            lap()
        elif choice == "4":
            show_time()
        elif choice == "5":
            show_laps()
        elif choice == "6":
            reset()
        elif choice == "7":
            print("Goodbye")
            running = 'False'
            main_menu()
        else:
            print("Invalid choice")
        time.sleep(0.5)
        print("-" * 20)
def countdown_pomodoro(minutes, label):
    seconds = minutes * 60
    while seconds >= 0:
        mins, secs = divmod(seconds, 60)
        print(f"\r{label} {mins:02d}:{secs:02d}", end="")
        time.sleep(0.001)
        seconds -= 1
Total_time = 0
def start_pomodoro():
    global Total_time
    print("1. work: 25 minutes & break: 5 minutes")
    print("2. work: 45 minutes & break: 15 minutes")
    mode = int(input('Choose one of the options: '))

    if mode != 1 and mode != 2:
        print("Invalid Option")
        start_pomodoro()
    laps = int(input('Enter number of laps: '))
    for i in range(laps):
        if mode == 1:
            print('Work time!')
            countdown_pomodoro(25, '[work]')
            print()
            print('Break time!')
            countdown_pomodoro(5, '[Break]')
            print()
            Total_time += 25
        if mode == 2:
            print('Work time!')
            countdown_pomodoro(45, '[work]')
            print()
            print('Break time!')
            countdown_pomodoro(15, '[Break]')
            print()
            Total_time += 45
    print('Session has ended!')
    pomodoro_page()
    return time
def history_pomodoro():
    if Total_time == 0:
        print('No Pomodoro Timer History')
    else:
        print('You studied for ', Total_time, 'minutes')
        time.sleep(4)
        main_menu()
def pomodoro_page():
    print('-----Pomodoro Page-----')
    print('1. Start Pomodoro session')
    print('2. show history')
    print('3. Exit to main menu')
    user_input = int(input('Enter your choice: '))
    if user_input == 1:
        start_pomodoro()
    elif user_input == 2:
        history_pomodoro()
    elif user_input == 3:
            main_menu()
    else:
        print("Invalid Option")
        pomodoro_page()
def main_menu():
    print(f'----- Main Menu -----')
    print('Enter 1 for timer')
    print('Enter 2 for stopwatch')
    print('Enter 3 for pomodoro timer')
    choice = 'False'
    while choice == 'False':
        page = int(input('Enter page number: '))
        if page == 1:
            timer_page()
            choice = 'True'
        elif page == 2:
            stopwatch_page()
            choice = 'True'
        elif page == 3:
            pomodoro_page()
            choice = 'True'
        else:
            print('Invalid input')
main_menu()
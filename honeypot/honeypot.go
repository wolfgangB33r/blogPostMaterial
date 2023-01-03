package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"strconv"
	"strings"
)

type config struct {
	Redirect          	bool
	RedirectLocation	string
	Slowdown			int
}

var conf config

func receiveConfig(w http.ResponseWriter, r *http.Request) {
	switch r.Method {
	case "POST":
		w.WriteHeader(http.StatusNoContent)
		body, err := ioutil.ReadAll(r.Body)
		if err != nil {
			panic(err)
		}
		//fmt.Printf(string(body))
		err = json.Unmarshal(body, &conf)
		if err != nil {
			fmt.Printf("Bad config payload!")
			log.Printf("%s bad config payload", os.Args[0])
			panic(err)
		}
		log.Printf("%s received a new config",  os.Args[0])
	default:
		fmt.Fprintf(w, "Only POST is supported.")
	}
	defer r.Body.Close()
}

func handleIcon(w http.ResponseWriter, r *http.Request) {
	defer r.Body.Close()
}

func sayHello(w http.ResponseWriter, r *http.Request) {
	log.Printf("-\n")
	log.Printf("Requested: %s\n", r.URL.Path)
	log.Printf("ClientAdr: %s\n", r.RemoteAddr)
	log.Printf("UserAgent: %s\n", r.UserAgent())

	// Loop over header names
	for name, values := range r.Header {
		// Loop over all values for the name.
		for _, value := range values {
			log.Printf("%s: %s\n", name, value)
		}
	}

	if conf.Redirect {
		// HTTP/1.1 301 moved permanently
		w.Header().Set("Location", "https://example.com")
		w.WriteHeader(http.StatusMovedPermanently)
		
	} else {
		message := r.URL.Path
		message = strings.TrimPrefix(message, "/")
		message = "finally returned " + message
		w.Write([]byte(message))
	}
	defer r.Body.Close()
}

func main() {
	port := 8080
	if len(os.Args) > 1 {
		arg := os.Args[1]
		fmt.Printf("Start honeypot at port: %s\n", arg)
		i1, err := strconv.Atoi(arg)
		if err == nil {
			port = i1
		}
	} else {
		fmt.Printf("Start honeypot at default port: %d\n", port)
	}

	http.HandleFunc("/", sayHello)
	http.HandleFunc("/favicon.ico", handleIcon)
	http.HandleFunc("/config", receiveConfig)
	if err := http.ListenAndServe(":"+strconv.Itoa(port), nil); err != nil {
		panic(err)
	}
}
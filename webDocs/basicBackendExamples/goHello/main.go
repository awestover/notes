package main

import (
  "fmt"
  "net/http"
  "html"
)

func main() {
  http.HandleFunc("/upload", func(w http.ResponseWriter, r *http.Request) {
      fmt.Fprintf(w, "<h1>Hello, %q</h1><img src='crab.png'>", html.EscapeString(r.URL.Path))
  })
  print("running on localhost:3000")
  http.Handle("/", http.FileServer(http.Dir("./static")))
  http.ListenAndServe(":3000", nil)
}



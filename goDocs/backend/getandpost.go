package main

import (
   "io/ioutil"
   "log"
   "net/http"
)

func main() {
   resp, err := http.Get("https://jsonplaceholder.typicode.com/posts")
   if err != nil {
      log.Fatalln(err)
   }
//We Read the response body on the line below.
   body, err := ioutil.ReadAll(resp.Body)
   if err != nil {
      log.Fatalln(err)
   }
//Convert the body to type string
   sb := string(body)
   log.Printf(sb)
}


// package main

// import (
//    "bytes"
//    "encoding/json"
//    "io/ioutil"
//    "log"
//    "net/http"
// )

// func main() {
// //Encode the data
//    postBody, _ := json.Marshal(map[string]string{
//       "name":  "Toby",
//       "email": "Toby@example.com",
//    })
//    responseBody := bytes.NewBuffer(postBody)
// //Leverage Go's HTTP Post function to make request
//    resp, err := http.Post("https://postman-echo.com/post", "application/json", responseBody)
// //Handle Error
//    if err != nil {
//       log.Fatalf("An Error Occured %v", err)
//    }
//    defer resp.Body.Close()
// //Read the response body
//    body, err := ioutil.ReadAll(resp.Body)
//    if err != nil {
//       log.Fatalln(err)
//    }
//    sb := string(body)
//    log.Printf(sb)
// }



package main

import (
    "bufio"
    "fmt"
    "os"
)

func main() {
    reader := bufio.NewReader(os.Stdin)
    fmt.Print("Enter your favorite number: ")
    input, err := reader.ReadString('\n')
    if err != nil {
        fmt.Println("Error reading input:", err)
        os.Exit(1)
    }
    // Echo the input back
    fmt.Printf("Your favorite number is %s", input)
}
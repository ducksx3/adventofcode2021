package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

var increaseCount int = 0
var lastCount int
var skippedFirst bool = false

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		if skippedFirst {
			curCount, err := strconv.Atoi(scanner.Text())
			if err != nil {
				log.Fatal(err)
			}
			if curCount > lastCount {
				increaseCount += 1
			}
			lastCount = curCount
		} else {
			skippedFirst = true
		}

	}
	fmt.Println("Total increases:", increaseCount)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}

// - https://stackoverflow.com/a/16615559

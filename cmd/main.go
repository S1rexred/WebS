package main

import (
	"log"

	"github.com/WebS"
	"github.com/WebS/pkg/handler"
)

func main() {
	handlers := new(handler.Handler)
	svr := new(WebS.Server)
	if err := svr.Run("8000", handlers.InitRoutes()); err != nil {
		log.Fatalf("error occurred while starting http server: %s", err.Error())
	}
}

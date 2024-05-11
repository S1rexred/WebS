package main

import (
	"log"

	"github.com/Users/101/Documents/GitHub/WebS/Websback"
	"github.com/Users/101/Documents/GitHub/WebS/Websback/pkg/handler"
	"github.com/Users/101/Documents/GitHub/WebS/Websback/pkg/repository"
	"github.com/Users/101/Documents/GitHub/WebS/Websback/pkg/service"
)

func main() {
	repos := repository.NewRepository()
	services := service.NewService(repos)
	handlers := handler.NewHandler(services)

	svr := new(Websback.Server)
	if err := svr.Run("9000", handlers.InitRoutes()); err != nil {
		log.Fatalf("error occured while running http sever: %s", err.Error())
	}
}

package service

import "github.com/Users/101/Documents/GitHub/WebS/Websback/pkg/repository"

type Autorization interface {
}

type WebsbackList interface {
}

type WebsbackItem interface {
}

type Service struct {
	Autorization
	WebsbackList
	WebsbackItem
}

func NewService(repos *repository.Repository) *Service {
	return &Service{}
}
package service

import "github.com/WebS/pkg/repository"

type Autorization interface {
}

type WebSList interface {
}

type WebSItem interface {
}

type Service struct {
	Autorization
	WebSList
	WebSItem
}

func NewService(repos *repository.Repository) *Service {
	return &Service{}
}

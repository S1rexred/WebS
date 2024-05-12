package repository

type Autorization interface {
}

type WebSList interface {
}

type WebSItem interface {
}

type Repository struct {
	Autorization
	WebSList
	WebSItem
}

func NewRepository() *Repository {
	return &Repository{}
}

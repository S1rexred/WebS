package repository

type Autorization interface {
}

type WebsbackList interface {
}

type WebsbackItem interface {
}

type Repository struct{
	Autorization
	WebsbackList
	WebsbackItem
}
func NewRepository() *Repository {
	return &Repository{}
}


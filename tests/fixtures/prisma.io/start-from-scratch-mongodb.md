```mermaid
erDiagram

Post{
  id String
  slug String
  title String
  body String
  authorId String
}

User{
  id String
  email String
  name String
  address Address
}

Post }o..|| User : "Post : User"

```
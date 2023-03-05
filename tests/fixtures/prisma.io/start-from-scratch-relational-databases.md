```mermaid
erDiagram

Post{
    id Int
    createdAt DateTime
    updatedAt DateTime
    title String
    content String
    published Boolean
    authorId Int
}

Profile{
    id Int
    bio String
    userId Int
}

User{
    id Int
    email String
    name String
}

Post }o--|| User : "Post : User"
Profile }o--|| User : "Profile : User"

```
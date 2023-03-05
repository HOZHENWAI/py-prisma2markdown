#Prisma schema
```mermaid
erDiagram

User {
    id String
    createAt DateTime
    firstName String
    lastName String
    email String
}

Post {
    id String
    createdAt DateTime
    title String
    body String
    views Int
    authorId String
}

Post }o..o| User : "Post : User"
```
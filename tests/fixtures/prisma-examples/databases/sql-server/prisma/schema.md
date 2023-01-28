# Prisma schema
```mermaid
erDiagram

User {
    id Integer
    createdAt DateTime
    email String
    name String
}

Post {
    id Integer
    createdAt DateTime
    title String
    content String
    published Boolean
    authorId Integer
}

Comment {
    id Integer
    createdAt DateTime
    comment String
    writtenById Integer
    postId Integer
}

Tag {
    id Integer
    tag String
}

```
# Prisma schema
```mermaid
erDiagram

User {
    id Int
    createdAt DateTime
    email String
    name String
}

Post {
    id Int
    createdAt DateTime
    title String
    content String
    published Boolean
    authorId Int
}

Comment {
    id Int
    createdAt DateTime
    comment String
    writtenById Int
    postId Int
}

Tag {
    id Int
    tag String
}

Post }o--|| User : "Post.authorId : User.id"
Comment }o--|| User : "Comment.writtenBy : User.id"
Comment }o--|| Post : "Comment.postId : Post.id"
Post }o--o{ Tag : "TagToPost"
```
from fastapi import FastAPI, HTTPException

app = FastAPI()

text_posts = {
    1: {
        "title": "1984 - George Orwell",
        "content": "A dystopian novel exploring totalitarianism, surveillance, and the manipulation of truth in a controlled society."
    },
    2: {
        "title": "Clean Code - Robert C. Martin",
        "content": "A foundational software engineering book that teaches how to write readable, maintainable, and professional-quality code."
    },
    3: {
        "title": "A Brief History of Time - Stephen Hawking",
        "content": "An accessible explanation of cosmology, covering black holes, the Big Bang, time, and the structure of the universe."
    },
    4: {
        "title": "Dune - Frank Herbert",
        "content": "A science fiction epic combining politics, ecology, religion, and power struggles on the desert planet Arrakis."
    },
    5: {
        "title": "Pride and Prejudice - Jane Austen",
        "content": "A classic romance novel examining love, class, and misunderstandings in early 19th-century England."
    },
    6: {
        "title": "The Art of War - Sun Tzu",
        "content": "An ancient military treatise offering strategic principles that are still applied in business, politics, and leadership."
    },
    7: {
        "title": "The Tao Te Ching - Laozi",
        "content": "A foundational text of Taoism that explores balance, simplicity, and living in harmony with the natural flow of life."
    },
    8: {
        "title": "The Selfish Gene - Richard Dawkins",
        "content": "A science book that explains evolution from the perspective of genes and how they shape behavior and survival."
    },
    9: {
        "title": "The Alchemist - Paulo Coelho",
        "content": "A philosophical and spiritual novel about following one’s personal legend and finding meaning through life’s journey."
    },
    10: {
        "title": "Gödel, Escher, Bach - Douglas Hofstadter",
        "content": "An interdisciplinary work connecting mathematics, art, music, and consciousness through patterns and self-reference."
    }
}


@app.get("/posts")
def get_posts():
    return text_posts

@app.get("/post/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    
    return text_posts.get(id, {"error": "Post not found"})



# Fast API exmaple  
Ref: Tech With Tim - [Learn Fast API with one project](https://www.youtube.com/watch?v=SR5NYCdzKkc)  
[Code](https://github.com/techwithtim/FastAPIPhotoVideoSharing) for the original vidéo

### Dependencies
```
pip install -e .
```
See pyproject.toml

## API Implements
- CRUD : Create. Read, Update, Delete
- Some HTML Rendering stuff
- Can use Authentication


## Key concepts  
URL : https://subdomain.domain.com/folder?param1=123&param2=Hello  

| ID | Part | Description |
|-----|-----|-----|
| 1 | Domain | https://subdomain.domain.com |  
| 2 | Path / Endpoint | /folder |  
| 1 | Query Parameters | ?param1=123&param2=Hello |  


```
┌───────┐ request     ┌───────┐      
│ Front │ ----------> │ Back  │ 
│ End   │             │ End   │ 
│       │ <---------- │       │ 
└───────┘ response    └───────┘
```
***Resquest Components***  
| ID | Component | Description                   |
|----|-----------|-------------------------------|
| 1  | Type      | GET, DELETE, POST, PUT(PATCH) |
| 2  | Path      | /api/action/param1            |
| 2  | Body      | see request Body (below)      |
| 2  | Headers   | see requets header (below)    |

***Response Components***  
| ID | Component   | Description |
|----|-------------|-------------|
| 1  | Status Code | 1XX (Info), 2XX (Success), 3XX (Redirection), 4XX (Client Error), 5XX (Server Error) |
| 2  | Body        |             |
| 2  | Headers     |             |

#### Request Body
```
{
    "title": "updated title",
    "description": "I dont like this"
}
```

#### Request Header 
```
{
    "Content-Type": "application/json",
    "Authorization": "bearer ajffdkjbsnjlkb124kmnl4490"
}
```

#### Response Body 
```
{
    "title": "updated title",
    "description": "I dont like this",
    "postId": 45535,
    "updatedAt": "Sept 26, 2025",
    "createdBy": "user-1234"
}
```

#### Response Header
```
{
    "Content-Type": "application/json"
}
```

## Project Folder Structure

```
project_root/

```


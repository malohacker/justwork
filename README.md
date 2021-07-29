GET http://localhost:8000/api/pages/
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "url": "http://localhost:8000/api/pages/1/",
            "title": "first"
        },
        {
            "url": "http://localhost:8000/api/pages/2/",
            "title": "second"
        }
    ]
}
```
GET http://localhost:8000/api/pages/1/

```json
{
    "id": 1,
    "contents": [
        {
            "id": 1,
            "media_content_type": {
                "title": "video"
            },
            "title": "video1",
            "counter": 29,
            "spec_attrs": {
                "url": "youtube.come",
                "subtitles_url": "12312"
            }
        },
        {
            "id": 2,
            "media_content_type": {
                "title": "audio"
            },
            "title": "audio1",
            "counter": 29,
            "spec_attrs": {
                "bitrate": "24"
            }
        },
        {
            "id": 3,
            "media_content_type": {
                "title": "text"
            },
            "title": "text1",
            "counter": 7,
            "spec_attrs": {
                "text": "test_text"
            }
        }
    ],
    "title": "first"
}
```

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import Response
from app.infrastructure.minio_service import get_minio_client, get_file
from app.core.config import get_settings

settings = get_settings()

def create_files_router() -> APIRouter:
    router = APIRouter(prefix="/files", tags=["Files"])

    @router.api_route("/{path:path}", methods=["GET", "HEAD"])
    async def get_file_proxy(path: str, request: Request):
        """Проксирование файлов из MinIO (GET и HEAD)."""
        if ".." in path or path.startswith("/"):
            raise HTTPException(400, "Invalid path")
        client = get_minio_client()
        try:
            data, content_type, size = get_file(client, settings.minio_bucket, path)
        except Exception as e:
            raise HTTPException(404, str(e))
        
        headers = {
            "Cache-Control": "public, max-age=86400",
            "Content-Length": str(size),
        }
        
        # Для HEAD запроса не возвращаем тело
        if request.method == "HEAD":
            return Response(
                content=b"",
                media_type=content_type,
                headers=headers,
            )
        
        return Response(
            content=data,
            media_type=content_type,
            headers=headers,
        )
    return router

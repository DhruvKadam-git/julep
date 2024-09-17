from typing import Annotated

from fastapi import Depends
from pydantic import UUID4

from ...autogen.openapi_model import (
    ResourceUpdatedResponse,
    UpdateSessionRequest,
)
from ...dependencies.developer_id import get_developer_id
from ...models.session.update_session import update_session as update_session_query
from .router import router


@router.put("/sessions/{session_id}", tags=["sessions"])
async def update_session(
    x_developer_id: Annotated[UUID4, Depends(get_developer_id)],
    session_id: UUID4,
    data: UpdateSessionRequest,
) -> ResourceUpdatedResponse:
    return update_session_query(
        developer_id=x_developer_id,
        session_id=session_id,
        data=data,
    )
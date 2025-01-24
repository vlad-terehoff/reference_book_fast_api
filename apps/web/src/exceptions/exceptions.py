from sqlalchemy.exc import NoResultFound, IntegrityError
from fastapi import HTTPException, status

no_result_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Запрашиваемого объекта не существует")


def exec_catch(fn):
    async def wrapped(*args, **kwargs):
        try:
            return await fn(*args, **kwargs)
        except NoResultFound as exc:
            # e = ExecResp(title=str(exc), code=400)
            # return e
            raise no_result_found

    return wrapped

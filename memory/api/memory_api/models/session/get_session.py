from uuid import UUID


def get_session_query(session_id: UUID):
    session_id = str(session_id)

    return f"""
    input[session_id] <- [[
        to_uuid("{session_id}"),
    ]]

    ?[
        agent_id,
        user_id,
        id,
        situation,
        summary,
        updated_at,
        created_at,
    ] := input[session_id],
        *sessions{{
            session_id: id,
            situation,
            summary,
            created_at,
            updated_at: validity,
            @ "NOW"
        }},
        *session_lookup{{
            agent_id,
            user_id,
            session_id: id,
        }}, updated_at = to_int(validity)"""
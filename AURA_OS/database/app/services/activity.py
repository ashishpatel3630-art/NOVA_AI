"""
Activity Service
"""


from AURA_OS.database.app.database.session import get_session
from AURA_OS.database.app.models.activity import Activity



class ActivityService:


    @staticmethod
    def recent_activity(limit=5):

        session = get_session()


        data = (
            session.query(Activity)
            .order_by(
                Activity.created_at.desc()
            )
            .limit(limit)
            .all()
        )


        session.close()


        return data
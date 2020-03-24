from application import db

class Job(db.Model):
    job_id = db.Column(db.Integer, primary_key=True)
    registration = db.Column(db.String(30), nullable=False)
    job_type = db.Column(db.String(30), nullable=False)
    parts = db.Column(db.String(100), nullable=False, unique=True)
    labour = db.Column(db.String(500), nullable=False, unique=True)

    def __repr__(self):
        return ''.join([
            'User: ', self.registration, ' ', self.job_type, '\r\n',
            'Title: ', self.parts, '\r\n', self.labour
            ])

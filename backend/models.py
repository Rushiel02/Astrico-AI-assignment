from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Institution(db.Model):
    """Model for educational institutions or hospitals."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    address = db.Column(db.String(200), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    pincode = db.Column(db.String(10), nullable=False)
    contact_person_name = db.Column(db.String(100), nullable=False)
    contact_person_email = db.Column(db.String(100), nullable=False)
    contact_person_mobile = db.Column(db.String(15), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    learners = db.relationship('Learner', backref='institution', lazy=True)
    assessors = db.relationship('Assessor', backref='institution', lazy=True)
    
    def __repr__(self):
        return f'<Institution {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'state': self.state,
            'pincode': self.pincode,
            'contact_person_name': self.contact_person_name,
            'contact_person_email': self.contact_person_email,
            'contact_person_mobile': self.contact_person_mobile,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }


class Learner(db.Model):
    """Model for students/learners."""
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    mobile_number = db.Column(db.String(15), nullable=False)
    institution_id = db.Column(db.Integer, db.ForeignKey('institution.id'), nullable=False)
    course = db.Column(db.String(100), nullable=True)  # Optional
    batch = db.Column(db.String(50), nullable=True)    # Optional
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Learner {self.full_name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'email': self.email,
            'mobile_number': self.mobile_number,
            'institution_id': self.institution_id,
            'institution_name': self.institution.name if self.institution else None,
            'course': self.course,
            'batch': self.batch,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }


class Assessor(db.Model):
    """Model for faculty/evaluators."""
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    mobile_number = db.Column(db.String(15), nullable=False)
    institution_id = db.Column(db.Integer, db.ForeignKey('institution.id'), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # Internal/External
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Assessor {self.full_name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'email': self.email,
            'mobile_number': self.mobile_number,
            'institution_id': self.institution_id,
            'institution_name': self.institution.name if self.institution else None,
            'role': self.role,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
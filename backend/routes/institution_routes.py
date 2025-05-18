from flask import Blueprint, request, jsonify
from models import db, Institution
from sqlalchemy.exc import IntegrityError

institution_bp = Blueprint('institution_bp', __name__)

@institution_bp.route('/', methods=['POST'])
def create_institution():
    """Create a new institution."""
    data = request.json
    
    # Check for required fields
    required_fields = ['name', 'address', 'state', 'pincode', 
                      'contact_person_name', 'contact_person_email', 'contact_person_mobile']
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({'error': f'Missing required field: {field}'}), 400
    
    # Normalize data
    name = data['name'].strip()
    
    # Create new institution
    try:
        institution = Institution(
            name=name,
            address=data['address'].strip(),
            state=data['state'].strip(),
            pincode=data['pincode'].strip(),
            contact_person_name=data['contact_person_name'].strip(),
            contact_person_email=data['contact_person_email'].strip(),
            contact_person_mobile=data['contact_person_mobile'].strip()
        )
        
        db.session.add(institution)
        db.session.commit()
        
        return jsonify({'message': 'Institution created successfully', 'institution': institution.to_dict()}), 201
    
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Institution with this name already exists'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@institution_bp.route('/', methods=['GET'])
def get_institutions():
    """Get all institutions."""
    institutions = Institution.query.all()
    return jsonify([institution.to_dict() for institution in institutions])

@institution_bp.route('/<int:institution_id>', methods=['GET'])
def get_institution(institution_id):
    """Get a specific institution by ID."""
    institution = Institution.query.get_or_404(institution_id)
    return jsonify(institution.to_dict())
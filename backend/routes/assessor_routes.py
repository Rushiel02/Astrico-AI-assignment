from flask import Blueprint, request, jsonify
from models import db, Assessor, Institution
from sqlalchemy.exc import IntegrityError

assessor_bp = Blueprint('assessor_bp', __name__)

@assessor_bp.route('/', methods=['POST'])
def create_assessor():
    """Create a new assessor."""
    data = request.json
    
    # Check for required fields
    required_fields = ['full_name', 'email', 'mobile_number', 'institution_id', 'role']
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({'error': f'Missing required field: {field}'}), 400
    
    # Validate institution exists
    institution = Institution.query.get(data['institution_id'])
    if not institution:
        return jsonify({'error': 'Institution not found'}), 404
    
    # Validate role
    role = data['role'].strip()
    if role not in ['Internal', 'External']:
        return jsonify({'error': 'Role must be either "Internal" or "External"'}), 400
    
    # Create new assessor
    try:
        assessor = Assessor(
            full_name=data['full_name'].strip(),
            email=data['email'].strip(),
            mobile_number=data['mobile_number'].strip(),
            institution_id=data['institution_id'],
            role=role
        )
        
        db.session.add(assessor)
        db.session.commit()
        
        return jsonify({'message': 'Assessor created successfully', 'assessor': assessor.to_dict()}), 201
    
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Assessor with this email already exists'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@assessor_bp.route('/', methods=['GET'])
def get_assessors():
    """Get all assessors."""
    assessors = Assessor.query.all()
    return jsonify([assessor.to_dict() for assessor in assessors])

@assessor_bp.route('/<int:assessor_id>', methods=['GET'])
def get_assessor(assessor_id):
    """Get a specific assessor by ID."""
    assessor = Assessor.query.get_or_404(assessor_id)
    return jsonify(assessor.to_dict())
from flask import Blueprint, request, jsonify
from models import db, Learner, Institution
from sqlalchemy.exc import IntegrityError

learner_bp = Blueprint('learner_bp', __name__)

@learner_bp.route('/', methods=['POST'])
def create_learner():
    """Create a new learner."""
    data = request.json
    
    # Check for required fields
    required_fields = ['full_name', 'email', 'mobile_number', 'institution_id']
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({'error': f'Missing required field: {field}'}), 400
    
    # Validate institution exists
    institution = Institution.query.get(data['institution_id'])
    if not institution:
        return jsonify({'error': 'Institution not found'}), 404
    
    # Create new learner
    try:
        learner = Learner(
            full_name=data['full_name'].strip(),
            email=data['email'].strip(),
            mobile_number=data['mobile_number'].strip(),
            institution_id=data['institution_id'],
            course=data.get('course', '').strip() or None,  # Handle optional field
            batch=data.get('batch', '').strip() or None     # Handle optional field
        )
        
        db.session.add(learner)
        db.session.commit()
        
        return jsonify({'message': 'Learner created successfully', 'learner': learner.to_dict()}), 201
    
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Learner with this email already exists'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@learner_bp.route('/', methods=['GET'])
def get_learners():
    """Get all learners."""
    learners = Learner.query.all()
    return jsonify([learner.to_dict() for learner in learners])

@learner_bp.route('/<int:learner_id>', methods=['GET'])
def get_learner(learner_id):
    """Get a specific learner by ID."""
    learner = Learner.query.get_or_404(learner_id)
    return jsonify(learner.to_dict())
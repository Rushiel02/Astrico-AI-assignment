from flask import Blueprint, jsonify
from models import Learner, Assessor, Institution

report_bp = Blueprint('report_bp', __name__)

@report_bp.route('/summary', methods=['GET'])
def get_summary():
    """Get summary metrics for the system."""
    total_learners = Learner.query.count()
    total_assessors = Assessor.query.count()
    total_institutions = Institution.query.count()
    
    summary = {
        'total_learners': total_learners,
        'total_assessors': total_assessors,
        'total_institutions': total_institutions
    }
    
    return jsonify(summary)
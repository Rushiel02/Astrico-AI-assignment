from flask import Flask
from flask_cors import CORS
from config import Config
from models import db, Institution, Learner, Assessor

def create_app(config_class=Config):
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    CORS(app)  # Enable CORS for all routes
    
    # Register blueprints
    from routes.learner_routes import learner_bp
    from routes.assessor_routes import assessor_bp
    from routes.institution_routes import institution_bp
    from routes.report_routes import report_bp
    
    app.register_blueprint(learner_bp, url_prefix='/api/learners')
    app.register_blueprint(assessor_bp, url_prefix='/api/assessors')
    app.register_blueprint(institution_bp, url_prefix='/api/institutions')
    app.register_blueprint(report_bp, url_prefix='/api/reports')
    
    # Create database tables
    with app.app_context():
        db.drop_all()
        db.create_all()
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
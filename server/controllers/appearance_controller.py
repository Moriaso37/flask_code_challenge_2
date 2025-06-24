from flask import Blueprint, request, jsonify
from models.appearance import Appearance, db
from flask_jwt_extended import jwt_required

appearance_bp = Blueprint('appearance', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def add_appearance():
    data = request.get_json()
    try:
        Appearance.validate_rating(data['rating'])
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    appearance = Appearance(
        rating=data['rating'],
        guest_id=data['guest_id'],
        episode_id=data['episode_id']
    )
    db.session.add(appearance)
    db.session.commit()
    return jsonify({"message": "Appearance created"}), 201

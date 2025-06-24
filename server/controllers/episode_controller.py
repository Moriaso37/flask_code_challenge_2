from flask import Blueprint, jsonify, request
from models.episode import Episode, db
from flask_jwt_extended import jwt_required

episode_bp = Blueprint('episode', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def list_episodes():
    episodes = Episode.query.all()
    return jsonify([{"id": ep.id, "number": ep.number, "date": ep.date.isoformat()} for ep in episodes])

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    ep = Episode.query.get_or_404(id)
    return jsonify({"id": ep.id, "number": ep.number, "date": ep.date.isoformat()})

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    ep = Episode.query.get_or_404(id)
    db.session.delete(ep)
    db.session.commit()
    return jsonify({"message": "Episode deleted"}), 200

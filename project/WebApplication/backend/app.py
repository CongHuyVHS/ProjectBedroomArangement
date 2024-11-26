# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
app = Flask(__name__)

# Enable CORS for React frontend
CORS(app)

# Configure the SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret-key'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    bedrooms = db.relationship('Bedroom', backref='user', lazy=True)

class Bedroom(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    width = db.Column(db.Float, nullable=False)
    length = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    free_space_percentage = db.Column(db.Float, nullable=False)
    user_id  = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Furniture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    bedroom_id = db.Column(db.Integer, nullable=False)
    beds = db.relationship('Bed', backref='furniture', lazy=True)
    closets = db.relationship('Closet', backref='furniture', lazy=True)


class Bed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100))
    width = db.Column(db.Float, nullable=False)
    length = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    furniture_id = db.Column(db.Integer, db.ForeignKey('furniture.id'))

class Closet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100))
    width = db.Column(db.Float, nullable=False)
    length = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    furniture_id = db.Column(db.Integer, db.ForeignKey('furniture.id'))

class Nightstand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100))
    width = db.Column(db.Float, nullable=False)
    length = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    furniture_id = db.Column(db.Integer, db.ForeignKey('furniture.id'))

class OfficeTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100))
    width = db.Column(db.Float, nullable=False)
    length = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    furniture_id = db.Column(db.Integer, db.ForeignKey('furniture.id'))

class Drawer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100))
    width = db.Column(db.Float, nullable=False)
    length = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    furniture_id = db.Column(db.Integer, db.ForeignKey('furniture.id'))

def generate_token(user_id):
    expiration = datetime.utcnow() + timedelta(hours=1)
    token = jwt.encode({'user_id': user_id,'exp':expiration}, app.config['JWT_SECRET_KEY'], algorithm='HS256')
    print(token)
    return token

def get_user_by_token(token):
    try:
        data = jwt.decode(token, app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
        return data.get('user_id')
    except jwt.ExpiredSignatureError:
        return None
@app.route('/api/register', methods=['POST'])
def register():
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')

    if not username or not email or not password:
        return jsonify({"msg": "Missing required fields"}), 400

    # Check if user already exists
    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({"msg": "User already exists"}), 409

    # Hash the password before saving it to the database
    hashed_password = generate_password_hash(password)

    # Create a new user and save to the database
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully"}), 201
# Create a route for user registration

# Create a route for user login
@app.route('/api/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    # Check if the user exists
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"msg": "Invalid credentials"}), 401
    print(user.id)
    # Generate an access token if successful
    token = generate_token(user.id)
    return jsonify({"token":token}), 200

# Create a route to add a bedroom
@app.route('/api/bedroom', methods=['POST'])
def add_bedroom():
    user_id = get_user_by_token(request.headers.get('Authorization').split(" ")[1])
    print(user_id)
    data = request.get_json()

    name = data.get('name')
    size = data.get('size')
    free_space_percentage = data.get('freeSpacePercentage')

    if not name or not size or free_space_percentage is None:
        return jsonify({"msg": "Missing required fields"}), 400

    width = size.get('width')
    length = size.get('length')
    height = size.get('height')

    if width is None or length is None or height is None:
        return jsonify({"msg": "Missing dimensions"}), 400

    # Create a new Bedroom entry
    new_bedroom = Bedroom(
        name=name,
        width=width,
        length=length,
        height=height,
        free_space_percentage=free_space_percentage,
        user_id=user_id
    )

    db.session.add(new_bedroom)
    db.session.commit()

    return jsonify({
        "bedroom_id": new_bedroom.id,
    }), 201

@app.route('/api/recent-bedrooms',methods=['GET'])
def get_recent_bedrooms():
    user_id = get_user_by_token(request.headers.get('Authorization').split(" ")[1])
    print(user_id)
    if not user_id:
        return jsonify({"msg": "Invalid token"}), 401
    print(
        Bedroom.query.filter_by(user_id=user_id).order_by(Bedroom.id.desc()).limit(5).all()
    )
    recent_bedrooms = Bedroom.query.filter_by(user_id=user_id).order_by(Bedroom.id.desc()).limit(5).all()
    bedroom_list = [
        {
            "id": bedroom.id,
            "name": bedroom.name,
            "width": bedroom.width,
            "length": bedroom.length,
            "height": bedroom.height,
            "free_space_percentage": bedroom.free_space_percentage
        }
        for bedroom in recent_bedrooms
    ]
    return jsonify(bedroom_list), 200

@app.route('/api/<int:bedroom_id>/calculate-space', methods=['POST'])
def calculate_space(bedroom_id):
    user_id = get_user_by_token(request.headers.get('Authorization').split(" ")[1])
    bedroom = Bedroom.query.filter_by(id=bedroom_id, user_id=user_id).first()
    if not bedroom:
        return jsonify({"message": "Bedroom not found or does not belong to this user."}), 404

    data = request.get_json()
    room_width, room_length = bedroom.width, bedroom.length
    # Initialize room grid with proper dimensions
    room_grid = [[0] * int(room_width) for _ in range(int(room_length))]
    placements = []

    furniture = Furniture(user_id=user_id, bedroom_id=bedroom_id)
    db.session.add(furniture)
    db.session.flush()

    # Furniture sizes with width and length as separate keys for clarity
    furniture_sizes = {
        "beds": {
            "king": {"width": 6.33, "length": 6.67, "height": 2.0},
            "queen": {"width": 5, "length": 6.67, "height": 2.0},
            "double": {"width": 4.5, "length": 6.25, "height": 2.0},
            "single": {"width": 3.17, "length": 6.25, "height": 2.0}
        },
        "closets": {
            "small": {"width": 2, "length": 2, "height": 6.0},
            "medium": {"width": 3, "length": 2, "height": 6.0},
            "large": {"width": 4, "length": 2, "height": 6.0}
        },
        "nightStands": {
            "small": {"width": 1.5, "length": 1.17, "height": 2.0},
            "medium": {"width": 1.5, "length": 1.17, "height": 2.0},
            "large": {"width": 1.5, "length": 1.17, "height": 2.0}
        },
        "drawers": {
            "3 drawers": {"width": 2.5, "length": 1.5, "height": 3.0},
            "4 drawers": {"width": 3, "length": 1.5, "height": 4.0}
        },
        "officeTables": {
            "small": {"width": 3.33, "length": 1.67, "height": 2.5},
            "medium": {"width": 4, "length": 2, "height": 2.5},
            "large": {"width": 5, "length": 2.5, "height": 2.5}
        }
    }

    def can_place_furniture(width, length):
        int_width = int(width)
        int_length = int(length)
        for y in range(int(room_length) - int_length + 1):
            for x in range(int(room_width) - int_width + 1):
                if all(room_grid[y + dy][x + dx] == 0
                       for dy in range(int_length)
                       for dx in range(int_width)):
                    for dy in range(int_length):
                        for dx in range(int_width):
                            room_grid[y + dy][x + dx] = 1
                    furniture_coords = [
                        {"x": x + dx, "y": y + dy}
                        for dy in range(int_length)
                        for dx in range(int_width)
                    ]
                    return furniture_coords
        return None

    total_furniture_area = 0

    # Helper function to process furniture items
    def process_furniture_item(item_type, category, model_class):
        furniture_type = item_type['type']
        furniture_info = furniture_sizes[category][furniture_type]
        coords = can_place_furniture(furniture_info['width'], furniture_info['length'])

        if coords:
            furniture_entry = model_class(
                type=furniture_type,
                width=furniture_info['width'],
                length=furniture_info['length'],
                height=furniture_info['height'],
                furniture_id=furniture.id
            )
            db.session.add(furniture_entry)
            for coord in coords:
                placements.append({"type": furniture_type, "x": coord["x"], "y": coord["y"]})
            return furniture_info['width'] * furniture_info['length']
        return 0

    # Process each furniture type
    furniture_processors = {
        'beds': (data.get('beds', []), 'beds', Bed),
        'closets': (data.get('closets', []), 'closets', Closet),
        'nightStands': (data.get('nightStands', []), 'nightStands', Nightstand),
        'drawers': (data.get('drawers', []), 'drawers', Drawer),
        'officeTables': (data.get('officeTables', []), 'officeTables', OfficeTable)
    }

    for items, category, model_class in furniture_processors.values():
        for item in items:
            total_furniture_area += process_furniture_item(item, category, model_class)
    print(total_furniture_area)
    # Convert total area to square feet
    total_furniture_area = total_furniture_area / 144  # Convert from square inches to square feet
    room_area = (room_width * room_length) / 144  # Convert to square feet
    free_space = room_area * bedroom.free_space_percentage / 100
    remaining_space = room_area - total_furniture_area
    has_enough_space = remaining_space >= free_space

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error saving furniture to database", "error": str(e)}), 500

    return jsonify({
        "remaining_space": round(remaining_space, 2),
        "has_enough_space": has_enough_space,
        "placements": placements,
        "furniture_id": furniture.id
    }), 201
@app.route('/api/bedroom/<int:bedroom_id>', methods=['GET','PUT'])
def update_bedroom(bedroom_id):

    user_id = get_user_by_token(request.headers.get('Authorization').split(" ")[1])
    bedroom = Bedroom.query.filter_by(id=bedroom_id, user_id=user_id).first()

    if not bedroom:
        return jsonify({"message": "Bedroom not found or unauthorized"}), 404

    if request.method == 'GET':
        return jsonify({
            "bedroom": {
                "id": bedroom.id,
                "name": bedroom.name,
                "size": {
                    "width": bedroom.width,
                    "length": bedroom.length,
                    "height": bedroom.height,
                },
                "freeSpacePercentage": bedroom.free_space_percentage,
            }
        }), 200

    elif request.method == 'PUT':
        data = request.get_json()
        name = data.get('name')
        size = data.get('size', {})
        free_space_percentage = data.get('freeSpacePercentage')

        if name:
            bedroom.name = name

        if 'width' in size:
            bedroom.width = size['width']
        if 'length' in size:
            bedroom.length = size['length']
        if 'height' in size:
            bedroom.height = size['height']

        if free_space_percentage is not None:
            bedroom.free_space_percentage = free_space_percentage

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({"message": "Error updating bedroom", "error": str(e)}), 500

        return jsonify({
            "message": "Bedroom updated successfully",
            "bedroom": {
                "id": bedroom.id,
                "name": bedroom.name,
                "size": {
                    "width": bedroom.width,
                    "length": bedroom.length,
                    "height": bedroom.height,
                },
                "freeSpacePercentage": bedroom.free_space_percentage,
            }
        }), 200


@app.route('/api/<int:bedroom_id>/modify-furniture', methods=['PUT','GET'])
def modify_furniture(bedroom_id):
    user_id = get_user_by_token(request.headers.get('Authorization').split(" ")[1])
    bedroom = Bedroom.query.filter_by(id=bedroom_id, user_id=user_id).first()

    if not bedroom:
        return jsonify({"message": "Bedroom not found or does not belong to this user."}), 404

    # Fetch furniture associated with the bedroom
    furniture = Furniture.query.filter_by(user_id=user_id, bedroom_id=bedroom_id).first()
    if not furniture:
        return jsonify({"message": "No furniture found for this bedroom."}), 404

    if request.method == 'GET':
        # Fetch all furniture items
        beds = Bed.query.filter_by(furniture_id=furniture.id).all()
        closets = Closet.query.filter_by(furniture_id=furniture.id).all()
        nightstands = Nightstand.query.filter_by(furniture_id=furniture.id).all()
        drawers = Drawer.query.filter_by(furniture_id=furniture.id).all()
        office_tables = OfficeTable.query.filter_by(furniture_id=furniture.id).all()

        # Create response dictionary
        furniture_data = {
            "beds": [{
                "id": bed.id,
                "type": bed.type,
                "width": bed.width,
                "length": bed.length,
                "height": bed.height
            } for bed in beds],

            "closets": [{
                "id": closet.id,
                "type": closet.type,
                "width": closet.width,
                "length": closet.length,
                "height": closet.height
            } for closet in closets],

            "nightStands": [{
                "id": stand.id,
                "type": stand.type,
                "width": stand.width,
                "length": stand.length,
                "height": stand.height
            } for stand in nightstands],

            "drawers": [{
                "id": drawer.id,
                "type": drawer.type,
                "width": drawer.width,
                "length": drawer.length,
                "height": drawer.height
            } for drawer in drawers],

            "officeTables": [{
                "id": table.id,
                "type": table.type,
                "width": table.width,
                "length": table.length,
                "height": table.height
            } for table in office_tables]
        }

        return jsonify(furniture_data), 200

    # If PUT request, continue with existing modification logic
    data = request.get_json()
    print(data)
    room_width, room_length = bedroom.width, bedroom.length
    room_grid = [[0] * int(room_width) for _ in range(int(room_length))]
    placements = []

    furniture_sizes = {
        "beds": {
            "king": {"width": 6.33, "length": 6.67, "height": 2.0},
            "queen": {"width": 5, "length": 6.67, "height": 2.0},
            "double": {"width": 4.5, "length": 6.25, "height": 2.0},
            "single": {"width": 3.17, "length": 6.25, "height": 2.0}
        },
        "closets": {
            "small": {"width": 2, "length": 2, "height": 6.0},
            "medium": {"width": 3, "length": 2, "height": 6.0},
            "large": {"width": 4, "length": 2, "height": 6.0}
        },
        "nightStands": {
            "small": {"width": 1.5, "length": 1.17, "height": 2.0},
            "medium": {"width": 1.5, "length": 1.17, "height": 2.0},
            "large": {"width": 1.5, "length": 1.17, "height": 2.0}
        },
        "drawers": {
            "3 drawers": {"width": 2.5, "length": 1.5, "height": 3.0},
            "4 drawers": {"width": 3, "length": 1.5, "height": 4.0}
        },
        "officeTables": {
            "small": {"width": 3.33, "length": 1.67, "height": 2.5},
            "medium": {"width": 4, "length": 2, "height": 2.5},
            "large": {"width": 5, "length": 2.5, "height": 2.5}
        }
    }

    def can_place_furniture(width, length):
        int_width = int(width)
        int_length = int(length)
        for y in range(int(room_length) - int_length + 1):
            for x in range(int(room_width) - int_width + 1):
                if all(room_grid[y + dy][x + dx] == 0
                       for dy in range(int_length)
                       for dx in range(int_width)):
                    for dy in range(int_length):
                        for dx in range(int_width):
                            room_grid[y + dy][x + dx] = 1
                    furniture_coords = [
                        {"x": x + dx, "y": y + dy}
                        for dy in range(int_length)
                        for dx in range(int_width)
                    ]
                    return furniture_coords
        return None

    def update_furniture_items(item_list, category, model_class):
        for item in item_list:
            item_id = item.get("id")
            item_type = item.get("type")
            if not item_id or not item_type:
                continue

            furniture_info = furniture_sizes[category].get(item_type)
            if not furniture_info:
                continue

            coords = can_place_furniture(furniture_info["width"], furniture_info["length"])
            if coords:
                # Try to find existing furniture item
                furniture_item = model_class.query.filter_by(id=item_id, furniture_id=furniture.id).first()

                if not furniture_item:
                    # If no existing item, create a new one
                    furniture_item = model_class(
                        furniture_id=furniture.id,
                        type=item_type,
                        width=furniture_info["width"],
                        length=furniture_info["length"],
                        height=furniture_info["height"]
                    )
                    print(furniture_item)
                    db.session.add(furniture_item)
                else:
                    # Update existing item
                    furniture_item.type = item_type
                    furniture_item.width = furniture_info["width"]
                    furniture_item.length = furniture_info["length"]
                    furniture_item.height = furniture_info["height"]

                for coord in coords:
                    placements.append({"type": item_type, "x": coord["x"], "y": coord["y"]})
            else:
                return {"message": f"Cannot place furniture {item_type} in the room."}, 400

    # Process modifications
    update_furniture_items(data.get('beds', []), 'beds', Bed)
    update_furniture_items(data.get('closets', []), 'closets', Closet)
    update_furniture_items(data.get('nightStands', []), 'nightStands', Nightstand)
    update_furniture_items(data.get('drawers', []), 'drawers', Drawer)
    update_furniture_items(data.get('officeTables', []), 'officeTables', OfficeTable)

    db.session.commit()
    return jsonify({
        "message": "Furniture updated successfully.",
        "placements": placements
    }), 200


if __name__ == '__main__':
    app.run(debug=True)

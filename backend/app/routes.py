import logging
from flask import Blueprint, request, jsonify
from flasgger import swag_from
from .services.story_service import start_story_service, next_fragment_service, get_current_story_service
from .services.story_image_service import StoryImageService, ImageStyle

logger = logging.getLogger(__name__)

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/start', methods=['POST'])
@swag_from('docs/start.yml')
def start_story():
    logger.info("Request received: /start")
    data = request.json
    response = start_story_service(data)
    return jsonify(response)

@main_blueprint.route('/next', methods=['POST'])
@swag_from('docs/next.yml')
def next_fragment():
    logger.info("Request received: /next")
    data = request.json
    response = next_fragment_service(data)
    return jsonify(response)

@main_blueprint.route('/current', methods=['GET'])
@swag_from('docs/current.yml')
def get_current_story():
    logger.info("Request received: /current")
    story_id = request.args.get('story_id', type=int)
    response = get_current_story_service(story_id)
    return jsonify(response)

@main_blueprint.route('/generate-image', methods=['POST'])
@swag_from('docs/generate_image.yml')
def generate_image():
    """
    Genera una imagen basada en el estilo y la inspiración proporcionados.
    """
    logger.info("Request received: /generate-image")
    data = request.json

    # Validar parámetros
    style = data.get("style")
    inspiration = data.get("inspiration")

    if not style or not inspiration:
        logger.error("Missing required parameters: style or inspiration")
        return jsonify({"error": "Parámetros faltantes: 'style' o 'inspiration'"}), 400

    # Validar estilo
    try:
        style_enum = ImageStyle(style)
    except ValueError:
        logger.error(f"Invalid style parameter: {style}")
        return jsonify({"error": f"Estilo inválido: {style}"}), 400

    # Generar imagen
    try:
        image_service = StoryImageService()
        image_url = image_service.generate_image(style_enum, inspiration)
        logger.info(f"Image generated successfully")
        return jsonify({"url": image_url})
    except Exception as e:
        logger.error(f"Error generating image: {e}")
        return jsonify({"error": "Error al generar la imagen"}), 500

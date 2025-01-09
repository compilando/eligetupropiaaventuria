import os
import logging
import json
import traceback
import random

from config import settings
from ..models.llm_factory import LLMFactory

# App storage, simula un backend de base de datos
stories = {}

def clean_fragment(fragment):
    """Cleans the fragment, handling potential JSON decoding issues."""
    try:
        data = json.loads(fragment)
        return data.get("fragmento", "")  # Retorna "fragmento" o vacío si no existe
    except json.JSONDecodeError:
        return fragment.strip()  # Limpia espacios y líneas innecesarias

def generate_fragment_with_llm(locale, theme, history_so_far, reader_option=None):
    logger = logging.getLogger(__name__)
    logger.info(f"Generating fragment with theme: {theme}, reader_option: {reader_option}")

    llm = LLMFactory.create_llm(
        model_type=settings.LLM,
        model_name=settings.MODEL_NAME,
        project=settings.PROJECT_ID,
        location=settings.LOCATION,
        temperature=0.7,
        max_tokens=4096
    )
    try:
        if reader_option is None:
            prompt_file = "prompt_history_start.txt"
        else:
            random_number = random.random()
            threshold = 0.9  # Ajusta según tu lógica
            prompt_file = "prompt_history_continue_end.txt" if random_number < threshold else "prompt_history_continue_more.txt"
            prompt_file = "prompt_history_continue_more.txt"

        replacements = {
            "{theme}": theme,
            "{language}": locale,
            "{reader_option}": reader_option or "",
            "{story_so_far}": history_so_far
        }

        resources_path = os.path.join(os.path.dirname(__file__), '../resources')
        prompt_path = os.path.join(resources_path, prompt_file)
        prompt_format_path = os.path.join(resources_path, 'prompt_history_format.txt')

        with open(prompt_path, 'r', encoding='utf-8') as f:
            prompt = f.read()
        with open(prompt_format_path, 'r', encoding='utf-8') as f:
            prompt_format = f.read()
        
        prompt = prompt + prompt_format
        for placeholder, value in replacements.items():
            prompt = prompt.replace(placeholder, value)

        result = llm.generate_fragment(prompt)
        logger.info(f"fragment result: {result}")
        return result
    except Exception as e:
        logger.error(f"Error generating fragment: {e}")
        logger.error(traceback.format_exc())
        return "Error generating fragment. Please try again.", []

def start_story_service(data):
    logger = logging.getLogger(__name__)
    logger.info("Starting new story")

    locale = data.get('locale', 'en')
    theme = data.get('theme', 'mystery_youth')
    story_id = len(stories) + 1

    title, fragment, options = generate_fragment_with_llm(locale, theme, history_so_far="")

    options_with_id = [{"id": str(i), "text": option_text} for i, option_text in enumerate(options, start=1)]

    stories[story_id] = {
        "theme": theme,
        "history_so_far": clean_fragment(fragment),
        "choices": [],
        "current_prefix": "",
        "options": options_with_id
    }

    return {
        "story_id": story_id,
        "title": title,
        "fragment": clean_fragment(fragment),
        "options": options_with_id
    }

def next_fragment_service(data):
    logger = logging.getLogger(__name__)
    logger.info("Getting next fragment")

    locale = data.get('locale', 'en')
    story_id = data.get('story_id')
    choice_id = data.get('choice_id')

    print(stories)
    if story_id not in stories:
        logger.error(f"Story not found: {story_id}")
        return {"error": "Historia no encontrada"}, 404

    story = stories[story_id]
    theme = story["theme"]
    options = story["options"]
    current_prefix = story["current_prefix"]

    try:
        choice_id = str(choice_id)
        selected_option = next((opt for opt in options if opt["id"] == choice_id), None)
        if not selected_option:
            raise ValueError("Invalid choice_id")
        reader_option = selected_option["text"]
    except ValueError as e:
        logger.error(f"Invalid choice_id: {choice_id}, Error: {e}")
        return {"error": "Elección inválida"}, 400

    story["choices"].append({"id": choice_id, "text": reader_option})
    story["history_so_far"] += f"\n[Elección {choice_id}]: {reader_option}"

    title, fragment, new_options = generate_fragment_with_llm(
        locale,
        theme,
        history_so_far=story["history_so_far"],
        reader_option=reader_option
    )
    cleaned_fragment = clean_fragment(fragment)

    new_prefix = f"{current_prefix}.{choice_id.split('.')[-1]}" if current_prefix else choice_id
    options_with_id = [{"id": f"{new_prefix}.{i}", "text": option_text} for i, option_text in enumerate(new_options, start=1)]

    story["history_so_far"] += f"\n{cleaned_fragment}"
    story["current_prefix"] = new_prefix
    story["options"] = options_with_id

    return {
        "fragment": cleaned_fragment,
        "options": options_with_id
    }

def get_current_story_service(story_id):
    logger = logging.getLogger(__name__)
    logger.info(f"Getting current story: {story_id}")
    if story_id not in stories:
        logger.warning(f"Story not found: {story_id}")
        return {"error": "Historia no encontrada"}, 404

    story = stories[story_id]
    return {
        "history_so_far": story["history_so_far"],
        "choices": story["choices"]
    }

import logging
import uuid
from enum import Enum
from pathlib import Path
import torch
from diffusers import KandinskyPriorPipeline, DiffusionPipeline
from transformers import CLIPTextModelWithProjection, CLIPTokenizer

# Configuración de logging
logger = logging.getLogger(__name__)

# Carpeta pública para almacenar imágenes generadas
GEN_IMAGES_PATH = Path("public/gen")
GEN_IMAGES_PATH.mkdir(parents=True, exist_ok=True)  # Crear la carpeta si no existe

class ImageStyle(Enum):
    
    FUTURISTIC = "FUTURISTIC"
    YEOLDE = "YEOLDE"

# Mapeo detallado de estilos
STYLE_PROMPT_MAP = {
    ImageStyle.FUTURISTIC: "A highly futuristic scene with advanced technology, neon lights, and a sci-fi aesthetic.",
    ImageStyle.YEOLDE: "A highly detailed black and white illustration in the style of antique engravings, depicting intricate linework and shading. The artwork resembles the classic illustrations found in 19th-century books, featuring a vintage aesthetic with ornate and textured elements.",
}

class StoryImageService:
    """
    Servicio para generar imágenes mediante el pipeline de Kandinsky sin dependencias externas.
    """

    def __init__(self, device="cuda" if torch.cuda.is_available() else "cpu"):
        """
        Inicializa el servicio de generación de imágenes.
        """
        logger.info(f"Initializing image generation pipeline on {device}...")

        # Configuración del pipeline prior
        self.pipe_prior = KandinskyPriorPipeline.from_pretrained(
            "kandinsky-community/kandinsky-2-2-prior",
            torch_dtype=torch.float16,
        ).to(device)

        # Configuración del pipeline principal
        self.pipe = DiffusionPipeline.from_pretrained(
            "kandinsky-community/kandinsky-2-2-decoder", torch_dtype=torch.float16
        ).to(device)

        logger.info("Pipeline successfully initialized.")

    def generate_image(self, style: ImageStyle, inspiration: str, negative_prompt: str = "low quality, bad quality", steps=50, guidance_scale=7.5, width=512, height=512) -> str:
        """
        Genera una imagen basada en el estilo y la inspiración proporcionados.

        Args:
            style (ImageStyle): Estilo de la imagen (futuristic, yeolde, etc.).
            inspiration (str): Cadena de inspiración para el prompt.
            negative_prompt (str): Cadena para el prompt negativo.
            steps (int): Número de pasos de inferencia.
            guidance_scale (float): Escala de orientación para ajustar la calidad.
            width (int): Anchura de la imagen en píxeles.
            height (int): Altura de la imagen en píxeles.

        Returns:
            str: La URL única de la imagen generada.
        """
        logger.debug(f"Generating image with style: {style.value}, inspiration: {inspiration}")

        # Construcción del prompt con la descripción rica del estilo
        style_description = STYLE_PROMPT_MAP.get(style, style.value)
        prompt = f"{style_description} {inspiration}"
        logger.debug(f"Prompt: {prompt}, Negative Prompt: {negative_prompt}")

        try:
            # Generar embeddings con el pipeline prior
            logger.debug("Generating image embeddings...")
            image_emb, negative_image_emb = self.pipe_prior(
                prompt, negative_prompt=negative_prompt
            ).to_tuple()

            # Generar la imagen usando los embeddings
            logger.debug("Generating final image...")
            output = self.pipe(
                image_embeds=image_emb,
                negative_image_embeds=negative_image_emb,
                num_inference_steps=steps,
                guidance_scale=guidance_scale,
                width=width,
                height=height,
            )
            image = output.images[0]

            # Guardar la imagen en el directorio público
            image_id = str(uuid.uuid4())
            image_path = GEN_IMAGES_PATH / f"{image_id}.png"
            image.save(image_path)

            logger.info(f"Image successfully generated and saved to {image_path}")
            return f"/gen/{image_id}.png"

        except Exception as e:
            logger.error(f"Error generating image: {e}", exc_info=True)
            raise ValueError("Failed to generate image") from e

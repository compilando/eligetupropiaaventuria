const BASE_URL = "http://localhost:5000"; // Cambia al puerto donde se ejecuta tu API

export const startStory = async (locale: string, theme: string) => {
  const response = await fetch(`${BASE_URL}/start`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ locale, theme }),
  });

  if (!response.ok) {
    throw new Error("Error iniciando la historia");
  }

  return response.json();
};

export const getCurrentState = async (storyId: number) => {
  const response = await fetch(`${BASE_URL}/current?story_id=${storyId}`);

  if (!response.ok) {
    throw new Error("Error obteniendo el estado actual");
  }

  return response.json();
};

export const nextFragment = async (
  locale: string,
  storyId: number,
  choiceId: string
) => {
  const response = await fetch(`${BASE_URL}/next`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      locale: locale,
      story_id: storyId,
      choice_id: choiceId,
    }),
  });

  if (!response.ok) {
    throw new Error("Error obteniendo el siguiente fragmento");
  }

  return response.json();
};

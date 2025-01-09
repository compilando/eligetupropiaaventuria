interface Page {
  page: string;
  options: { id: number; text: string; nextPage: number }[];
}

interface MockData {
  start: Page;
  pages: {
    [key: number]: Page;
  };
}

export const mockData: MockData = {
  start: {
    page: "Te despiertas en un claro rodeado de naturaleza salvaje. Recuerdas que estás buscando el <i>Legendario Cristal de los Destinos</i>, una reliquia que se dice tiene el poder de alterar el curso de la historia. Frente a ti, tienes tres caminos: <b>un bosque oscuro</b>, <b>una cueva sombría</b> y <b>un río tranquilo</b>. <br /><br />¿Qué decides hacer?",
    options: [
      { id: 1, text: "Adentrarte en el bosque", nextPage: 2 },
      { id: 2, text: "Explorar la cueva", nextPage: 3 },
      { id: 3, text: "Seguir el curso del río", nextPage: 4 },
    ],
  },
  pages: {
    2: {
      page: "El bosque es denso y cada paso que das parece ser observado por cientos de ojos invisibles. Encuentras un árbol antiguo con grabados en su tronco que parecen ser un mapa. Sin embargo, escuchas un gruñido a lo lejos. ¿Qué haces?",
      options: [
        { id: 1, text: "Examinar el mapa con cuidado", nextPage: 5 },
        { id: 2, text: "Buscar de dónde proviene el gruñido", nextPage: 6 },
        { id: 3, text: "Salir del bosque y regresar al claro", nextPage: 1 },
      ],
    },
    3: {
      page: "La cueva está fría y húmeda, y un eco extraño acompaña cada paso que das. Más adelante, ves una bifurcación: a la izquierda, hay un brillo tenue; a la derecha, un sonido de agua corriente. ¿Qué camino tomas?",
      options: [
        { id: 1, text: "Ir hacia el brillo", nextPage: 7 },
        { id: 2, text: "Seguir el sonido del agua", nextPage: 8 },
        { id: 3, text: "Regresar al claro", nextPage: 1 },
      ],
    },
    4: {
      page: "El río brilla bajo la luz del sol, pero notas que algo parece moverse en el fondo. Además, más adelante, el río se divide en dos direcciones: una más rápida y turbulenta, y otra calmada y lenta. ¿Qué haces?",
      options: [
        { id: 1, text: "Buscar en el fondo del río", nextPage: 9 },
        { id: 2, text: "Seguir la corriente rápida", nextPage: 10 },
        { id: 3, text: "Seguir la corriente tranquila", nextPage: 11 },
      ],
    },
    5: {
      page: "El mapa en el árbol muestra un dibujo rudimentario que parece señalar un lugar en el bosque. Sin embargo, el gruñido se escucha más cerca. ¿Qué haces?",
      options: [
        { id: 1, text: "Seguir las indicaciones del mapa", nextPage: 12 },
        { id: 2, text: "Prepararte para defenderte", nextPage: 13 },
        { id: 3, text: "Huir hacia el claro", nextPage: 1 },
      ],
    },
    6: {
      page: "Sigues el gruñido hasta que te encuentras con un lobo gigantesco. Parece estar protegiendo algo brillante bajo sus patas. ¿Qué haces?",
      options: [
        { id: 1, text: "Intentar calmar al lobo", nextPage: 14 },
        { id: 2, text: "Luchar contra el lobo", nextPage: 15 },
        { id: 3, text: "Retroceder lentamente y salir del bosque", nextPage: 1 },
      ],
    },
    7: {
      page: "El brillo proviene de un cristal azul incrustado en la pared. Al tocarlo, notas que emite un calor extraño, pero no parece ser el artefacto que buscas. De repente, el suelo comienza a temblar. ¿Qué haces?",
      options: [
        { id: 1, text: "Correr hacia la salida de la cueva", nextPage: 1 },
        { id: 2, text: "Intentar arrancar el cristal", nextPage: 16 },
        { id: 3, text: "Esconderte y esperar", nextPage: 17 },
      ],
    },
    8: {
      page: "Sigues el sonido del agua y llegas a una pequeña cascada. En la base de la cascada, ves un cofre cerrado. Sin embargo, el agua es profunda y peligrosa. ¿Qué haces?",
      options: [
        { id: 1, text: "Intentar abrir el cofre", nextPage: 18 },
        { id: 2, text: "Buscar otra forma de llegar al cofre", nextPage: 19 },
        { id: 3, text: "Regresar al claro", nextPage: 1 },
      ],
    },
    9: {
      page: "Te sumerges en el río y encuentras un anillo brillante en el fondo. Parece mágico. Al salir del agua, escuchas pasos acercándose. ¿Qué haces?",
      options: [
        { id: 1, text: "Esconderte entre los arbustos", nextPage: 20 },
        { id: 2, text: "Enfrentar al desconocido", nextPage: 21 },
        { id: 3, text: "Regresar al claro rápidamente", nextPage: 1 },
      ],
    },
    // Continúa el desarrollo de las páginas con esta narrativa común.
  },
};

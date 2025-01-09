"use client";

import { useState, useEffect, useRef } from "react";
import ReactMarkdown from "react-markdown";
import rehypeRaw from "rehype-raw";
import { useRouter } from "next/navigation";
import Image from "next/image";
import { nextFragment, startStory } from "../../services/apiService";
import { useTranslation } from "react-i18next";
import { FaCog } from "react-icons/fa"; // Importa el icono de rueda dentada

interface HistoryEntry {
  text: string;
  chosenOption?: string;
}

interface Option {
  id: number;
  text: string;
}

const processTextWithObjects = (text: string) => {
  return text
    .replace(/<object>(.*?)<\/object>/g, '<span class="epic-object">$1</span>')
    .replace(/<place>(.*?)<\/place>/g, '<span class="epic-place">$1</span>')
    .replace(
      /<character>(.*?)<\/character>/g,
      '<span class="epic-character">$1</span>'
    )
    .replace(
      /<danger>(.*?)<\/danger>/g,
      '<span class="mystery-text">$1</span>'
    );
};

const AdventurePage = () => {
  const { t } = useTranslation();
  const router = useRouter();

  const [initialLoading, setInitialLoading] = useState(true);
  const [fetchingNext, setFetchingNext] = useState(false);

  const [currentPage, setCurrentPage] = useState<string | null>(null);
  const [currentTitle, setCurrentTitle] = useState<string | null>(null);
  const [options, setOptions] = useState<Option[]>([]);
  const [history, setHistory] = useState<HistoryEntry[]>([]);
  const [showHistory, setShowHistory] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const [selectedFont, setSelectedFont] = useState<string>("monospace");
  const [textSize, setTextSize] = useState<string>("18px");

  const [isMenuOpen, setIsMenuOpen] = useState(false); // Estado del popup
  const initializedRef = useRef(false);

  const toggleMenu = () => setIsMenuOpen((prev) => !prev);
  const closeMenu = () => setIsMenuOpen(false);

  const toggleHistoryView = () => setShowHistory((prev) => !prev);

  const resetToHome = () => {
    localStorage.removeItem("storyId");
    localStorage.removeItem("currentTitle");
    localStorage.removeItem("choiceId");
    router.push("/");
  };

  const initializeStory = async () => {
    try {
      const storedFont = localStorage.getItem("selectedFont") || "monospace";
      const storedTextSize = localStorage.getItem("textSize") || "18px";
      setSelectedFont(storedFont);
      setTextSize(storedTextSize);

      const storedStoryId = localStorage.getItem("storyId");
      const storedTitle = localStorage.getItem("currentTitle");
      const storedChoiceId = localStorage.getItem("choiceId");

      if (storedStoryId && storedTitle && storedChoiceId) {
        setCurrentTitle(storedTitle);
        const currentLocale = navigator.language;
        const data = await nextFragment(
          currentLocale,
          parseInt(storedStoryId, 10),
          storedChoiceId
        );
        setCurrentPage(processTextWithObjects(data.fragment));
        setOptions(
          (data.options || []).map((option) => ({
            ...option,
            text: processTextWithObjects(option.text),
          }))
        );
        setHistory([{ text: processTextWithObjects(data.fragment) }]);
      } else {
        const storedTheme =
          localStorage.getItem("selectedTheme") || "themes.mystery";

        const currentLocale = navigator.language;
        const data = await startStory(currentLocale, storedTheme);

        localStorage.setItem("storyId", data.story_id.toString());
        localStorage.setItem("currentTitle", data.title);

        setCurrentTitle(data.title);
        setCurrentPage(processTextWithObjects(data.fragment));
        setOptions(
          (data.options || []).map((option) => ({
            ...option,
            text: processTextWithObjects(option.text),
          }))
        );
        setHistory([{ text: processTextWithObjects(data.fragment) }]);
      }
    } catch (err) {
      console.error("Error inicializando la historia:", err);
      setError(t("error.loading"));
    } finally {
      setInitialLoading(false);
    }
  };

  useEffect(() => {
    if (typeof window !== "undefined" && !initializedRef.current) {
      initializedRef.current = true;
      initializeStory();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const handleNext = async (optionId: number) => {
    if (!currentPage) return;

    setFetchingNext(true);
    try {
      const chosenOption =
        options.find((option) => option.id === optionId)?.text || "";
      const currentLocale = navigator.language;
      const data = await nextFragment(
        currentLocale,
        parseInt(localStorage.getItem("storyId") || "0"),
        optionId.toString()
      );

      localStorage.setItem("choiceId", optionId.toString());
      setCurrentPage(processTextWithObjects(data.fragment));
      setOptions(
        (data.options || []).map((option) => ({
          ...option,
          text: processTextWithObjects(option.text),
        }))
      );

      setHistory((prev) => [
        ...prev,
        { text: chosenOption },
        { text: processTextWithObjects(data.fragment), chosenOption },
      ]);
    } catch (err) {
      console.error("Error avanzando en la historia:", err);
      setError(t("error.advance"));
    } finally {
      setFetchingNext(false);
    }
  };

  if (initialLoading) {
    return (
      <div style={{ textAlign: "center", padding: "20px" }}>
        {/* Imagen de carga */}
        <Image
          src="/spinner_haunted.webp" // Ruta relativa desde la carpeta `public/`
          alt={t("adventure.loading")}
          width={200} // Ancho deseado
          height={200} // Altura deseada
          priority // Optimiza la carga de esta imagen
          style={{ marginBottom: "20px" }}
        />
        {/* Texto de carga */}
        <div>{t("adventure.loading")}</div>
      </div>
    );
  }
  if (error) {
    return <div>{error}</div>;
  }

  return (
    <div
      className={`adventure-page ${showHistory ? "history-open" : ""}`}
      style={{
        fontFamily: selectedFont,
        fontSize: textSize,
        position: "relative",
      }}
    >
      {/* Menú en la esquina superior derecha */}
      <div className="menu-container">
        <button className="menu-icon" onClick={toggleMenu}>
          <FaCog size={24} />
        </button>
        {isMenuOpen && (
          <div className="popup-menu">
            <button
              onClick={() => {
                toggleHistoryView();
                closeMenu();
              }}
            >
              {showHistory
                ? t("adventure.history.hide")
                : t("adventure.history.show")}
            </button>
            <button onClick={resetToHome}>{t("adventure.backToHome")}</button>
          </div>
        )}
      </div>

      {fetchingNext && (
        <div className="loading-overlay">
          <div className="spinner" />
          <p>{t("adventure.loadingNext")}</p>
        </div>
      )}

      <div className="reading-area">
        <div className="text-container">
          <h1 className="book-title">{currentTitle}</h1>
          <ReactMarkdown rehypePlugins={[rehypeRaw]}>
            {currentPage || ""}
          </ReactMarkdown>
          {options.length > 0 && (
            <div className="options-container">
              {options.map((option) => (
                <button
                  key={option.id}
                  onClick={() => handleNext(option.id)}
                  dangerouslySetInnerHTML={{ __html: option.text }}
                />
              ))}
            </div>
          )}
        </div>
      </div>

      {showHistory && (
        <div className="history-container">
          <h1 className="book-title">{t("adventure.history")}</h1>
          <div className="history-content">
            {history.map((entry, index) => (
              <p key={index} className="history-entry">
                <span dangerouslySetInnerHTML={{ __html: entry.text }} />
                {entry.chosenOption && (
                  <em>
                    <br />
                    {t("adventure.lastChoice")}: {entry.chosenOption}
                  </em>
                )}
              </p>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default AdventurePage;

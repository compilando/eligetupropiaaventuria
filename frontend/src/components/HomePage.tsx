"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { useTranslation } from "react-i18next";
import { FaMagic } from "react-icons/fa"; // Para un icono divertido

const fonts = [
  { labelKey: "fonts.monospace", value: "monospace" },
  { labelKey: "fonts.serif", value: "Georgia, serif" },
  { labelKey: "fonts.sansSerif", value: "Arial, sans-serif" },
  { labelKey: "fonts.courier", value: "'Courier New', Courier, monospace" },
];

const themes = [
  "themes.mystery",
  "themes.fantasy",
  "themes.sciFi",
  "themes.horror",
  "themes.romance",
  "themes.adventure",
  "themes.thriller",
  "themes.historicalFiction",
  "themes.comedy",
  "themes.drama",
  "themes.western",
  "themes.superhero",
  "themes.dystopian",
  "themes.cyberpunk",
  "themes.steampunk",
];

const textSizes = [
  { labelKey: "textSizes.small", value: "14px" },
  { labelKey: "textSizes.medium", value: "18px" },
  { labelKey: "textSizes.large", value: "22px" },
];

const HomePage: React.FC = () => {
  const { t } = useTranslation();
  const router = useRouter();
  const [name, setName] = useState<string>("");
  const [selectedTheme, setSelectedTheme] = useState<string>(themes[0]);
  const [pageLength, setPageLength] = useState<number>(300);
  const [selectedFont, setSelectedFont] = useState<string>("monospace");
  const [textSize, setTextSize] = useState<string>("18px");

  // Load values from localStorage
  useEffect(() => {
    const storedName = localStorage.getItem("userName");
    const storedTheme = localStorage.getItem("selectedTheme");
    const storedPageLength = localStorage.getItem("pageLength");
    const storedFont = localStorage.getItem("selectedFont");
    const storedTextSize = localStorage.getItem("textSize");

    if (storedName) setName(storedName);
    if (storedTheme) setSelectedTheme(storedTheme);
    if (storedPageLength) setPageLength(Number(storedPageLength));
    if (storedFont) setSelectedFont(storedFont);
    if (storedTextSize) setTextSize(storedTextSize);
  }, []);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    localStorage.setItem("userName", name);
    localStorage.setItem("selectedTheme", selectedTheme);
    localStorage.setItem("pageLength", pageLength.toString());
    localStorage.setItem("selectedFont", selectedFont);
    localStorage.setItem("textSize", textSize);
    localStorage.removeItem("storyId");
    localStorage.removeItem("currentTitle");

    router.push("/adventure");
  };

  return (
    <div className="home-page-container">
      <form onSubmit={handleSubmit} className="home-page-form">
        <h1 className="book-title">
          <FaMagic style={{ marginRight: "10px" }} />
          {t("home.title")}
        </h1>

        <div className="form-group">
          <label htmlFor="name">{t("home.nameLabel")}</label>
          <input
            type="text"
            id="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder={t("home.namePlaceholder")}
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="theme">{t("home.themeLabel")}</label>
          <select
            id="theme"
            value={selectedTheme}
            onChange={(e) => setSelectedTheme(e.target.value)}
          >
            {themes.map((theme) => (
              <option key={theme} value={theme}>
                {t(theme)}
              </option>
            ))}
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="font">{t("home.fontLabel")}</label>
          <select
            id="font"
            value={selectedFont}
            onChange={(e) => setSelectedFont(e.target.value)}
          >
            {fonts.map((font) => (
              <option key={font.value} value={font.value}>
                {t(font.labelKey)}
              </option>
            ))}
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="textSize">{t("home.textSizeLabel")}</label>
          <select
            id="textSize"
            value={textSize}
            onChange={(e) => setTextSize(e.target.value)}
          >
            {textSizes.map((size) => (
              <option key={size.value} value={size.value}>
                {t(size.labelKey)}
              </option>
            ))}
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="pageLength">
            {t("home.pageLengthLabel", { chars: pageLength })}
          </label>
          <input
            type="range"
            id="pageLength"
            min="100"
            max="500"
            step="50"
            value={pageLength}
            onChange={(e) => setPageLength(Number(e.target.value))}
          />
          <span className="range-value">
            {pageLength} {t("home.chars")}
          </span>
        </div>

        <button type="submit" className="start-button">
          {t("home.startButton")}
        </button>
      </form>
    </div>
  );
};

export default HomePage;
